# 无法独立使用，建议配合IPython等成熟的REPL进行操作
import socket
import pickle
import enum
import dataclasses


class SpecialMessage(enum.Enum):
    closeconnect = enum.auto()
    getallvar = enum.auto()

@dataclasses.dataclass
class GetVarMessage():
    key: str
    
@dataclasses.dataclass
class SetVarMessage():
    key: str
    obj: object
    
@dataclasses.dataclass
class ExecCommandMessage():
    command:str
    
@dataclasses.dataclass
class ExceptionWrapper():
    exc: Exception


class ReplServer():
    def __init__(self, vars, address='127.0.0.1', port=3311, setvarcallback=lambda key,obj,vars:None, execcommandcallback=lambda resp,vars:None):
        self.sock=socket.socket()
        self.sock.bind((address,port))
        self.sock.listen(1)
        self.vars=vars
        self.setvarcallback=setvarcallback
        self.execcommandcallback=execcommandcallback
        self.closed=False
       
    def wait_forever(self):
        while not self.closed:
            conn,addr=self.sock.accept()
            try:
                while not self.closed:
                    content=conn.recv(8192)
                    self.doevent(pickle.loads(content),conn)
            except EOFError:
                pass
            conn.close()
           
    def close(self):
        self.closed=True
        self.sock.close()
        
    def doevent(self,ent,conn):
        try:
            if isinstance(ent,SpecialMessage):
                if ent==SpecialMessage.closeconnect:
                    self.close()
                if ent==SpecialMessage.getallvar:
                    conn.send(pickle.dumps(self.vars))
            elif isinstance(ent,GetVarMessage):
                conn.send(pickle.dumps(self.vars[ent.key]))
            elif isinstance(ent,SetVarMessage):
                self.vars[ent.key]=ent.obj
                self.setvarcallback(ent.key,self.vars[ent.key],self.vars)  # 调用回调
            elif isinstance(ent,ExecCommandMessage):
                try:
                    resp=eval(ent.command,self.vars)
                except SyntaxError:
                    resp=exec(ent.command,self.vars)
                self.execcommandcallback(resp,self.vars)
                conn.send(pickle.dumps(resp))
            else:
                print('Recv message:',ent)
        except Exception as exc:
            conn.send(pickle.dumps(ExceptionWrapper(exc)))

def parse_resp(resp):
    if isinstance(resp, ExceptionWrapper):
        if isinstance(resp.exc, KeyError):
            raise AttributeError
        else:
            raise resp.exc
    return resp

class VarsManger():
    def __init__(self, sock):
        self._sock=sock
    def __getattr__(self, key):
        if key.startswith('__') or key=='_sock':
            return object.__getattr__(self,key)
        else:
            self._sock.send(pickle.dumps(GetVarMessage(key)))
            return parse_resp(pickle.loads(self._sock.recv(8192)))
    def __setattr__(self,key,obj):
        if key.startswith('__') or key=='_sock':
            return object.__setattr__(self,key,obj)
        else:
            self._sock.send(pickle.dumps(SetVarMessage(key,obj)))
        

class ReplClient():
    def __init__(self, address, port):
        self.sock=socket.socket()
        self.sock.connect((address,port))
        self.vars=VarsManger(self.sock)
    
    def exec_command(self,command):
        self.sock.send(pickle.dumps(ExecCommandMessage(command)))
        return parse_resp(pickle.loads(self.sock.recv(8192)))
        
    