import json
import os

import datautil


PACKED=0

if PACKED:
    config_path=f'{os.environ["USERPROFILE"]}\\meatpi_settings.db'
else:
    config_path='settings.db'

class Settings(object):
    
    @classmethod
    def load_settings(cls: type) -> None:
        # 这个函数为了向下兼容被保留
        pass
            
    @classmethod
    def store_settings(cls: type) -> None:
        # 这个函数为了向下兼容被保留
        pass
            
    @classmethod
    def init_settings(cls: type) -> None:
        if cls.settings.get('version',0)<1:
            cls.settings._dict = cls.ask_settings()
            cls.settings.store()

    name = {
        'auto_restart':'报错重启',
        'delay':'功能时差',
        'username':'用户名'
     }
    settings = datautil.SyncDict(config_path)
    
    @staticmethod
    def ask_settings() -> dict:
        return {
            'auto_restart':int(input('是否启用报错自动重启？')),
            'delay':float(input('请输入功能时差：')),
            'username':input('请输入用户名:'),
            'version':1
        }
        
