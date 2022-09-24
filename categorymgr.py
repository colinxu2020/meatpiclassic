import pathlib
from importlib import import_module

import categorybase as base


def load(obj: type):
    mro=list(obj.__mro__)[1:-1][::-1]
    if mro[0]!=base.BaseCategory:
        raise TypeError
    del mro[0]
        
    cur=base.root
    for i in mro:
        if not isinstance(i,base.CategoryMetaClass):
            continue
        try:
            cur=cur.find(i)
        except ValueError:
            cur.childrens.append(base.Node(i, []))
            cur=cur.childrens[-1]
    
    cur.childrens.append(base.Node(obj.__mro__[0], []))
    
def _search(path):
    for i in path.glob('*'):
        if i.name=='__pycache__':
            continue
        if i.is_dir():
            _search(i)
        else:
            mod=import_module(i.as_posix().replace('/','.')[:-3])
            for j in dir(mod):
                if isinstance(getattr(mod,j),type):
                    load(getattr(mod,j))
                
def search():
    root=pathlib.Path(r'.\categories')
    _search(root)
    