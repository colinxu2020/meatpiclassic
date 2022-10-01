from __future__ import annotations

import dataclasses
import types

@dataclasses.dataclass
class Node:
    cur: int
    childrens: list[Node]
    
    def find(self, tg: Node):
         for i in self.childrens:
             if i.cur==tg:
                 return i
         raise ValueError
                 
    
class CategoryMetaClass(type):
    def __new__(cls,name,bases,attrs):
        attrs['__functions__']=[]
        for itm in attrs.values():
             if isinstance(itm,types.FunctionType):
                 attrs['__functions__'].append(itm)
        obj=type.__new__(cls, name,bases,attrs)
        return obj
    
class BaseCategory(object, metaclass=CategoryMetaClass):
    pass
    
root=Node(BaseCategory,[])