"""
数据工具箱
暂时不被任何模块使用，之后会把一些曾经被删除的功能（e.g. 文件存储）加回来。
一些地图等二进制数据日后可能也会使用这个库。
"""

import pickle
import pickletools
import collections

# --- 基础pickle功能 --- #

def dumps(obj):
    return pickletools.optimize(pickle.dumps(obj))

def dump(fp,obj):
    fp.write(dumps(obj))
    
def loads(str):
    return pickle.loads(str)
    
def load(fp):
    return loads(fp.read())
    
# --- 高级功能 --- #

class SyncDict(object):
    """基于这个类创建的字典会自动与对应文件同步，用完以后记得调用close()。"""
    def store(self):
        self.reflush_fileobject()
        dump(self.fileobject,self._dict)
        
    def reflush_fileobject(self):
        self.fileobject.truncate()
    
    def __init__(self,filename):
        tmpdict={}
        try:
            fileobject=open(filename,'rb')
            tmpdict=load(fileobject)
            fileobject.close()
        except FileNotFoundError:
            pass
        fileobject=open(filename,"wb")
        self.filename=filename
        self.fileobject=fileobject
        self._dict=tmpdict
        self.reflush_fileobject()
        self.store()
        
    def __setitem__(self,key,value):
        self._dict[key]=value
        self.store()
        
    def __getitem__(self,key):
        return self._dict[key]
        
    def close(self):
        self.fileobject.close()
        
    def __del__(self):
        try:
            self.close()
        except Exception:
            pass
            