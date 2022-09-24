from __future__ import annotations

import dataclasses

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
    pass
    
class BaseCategory(object, metaclass=CategoryMetaClass):
    pass
    
root=Node(BaseCategory,[])