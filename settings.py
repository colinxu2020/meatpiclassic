import json
import os


PACKED=1

if PACKED:
    config_path=f'{os.environ["USERPROFILE"]}\\Meatpi_Settings.json'
else:
    config_path='Meatpi_Settings.json'

class Settings(object):
    
    @classmethod
    def load_settings(cls: type) -> None:
        with open(config_path, 'r') as fp:
            cls.settings=json.load(fp)
        if not isinstance(cls.settings,dict) or cls.settings.get('version',0)<1:
            raise FileNotFoundError
            
    @classmethod
    def store_settings(cls: type) -> None:
        with open(config_path, 'w') as fp:
            json.dump(cls.settings, fp)
            
    @classmethod
    def init_settings(cls: type) -> None:
        try:
            cls.load_settings()
        except FileNotFoundError:
            cls.settings = cls.ask_settings()
            cls.store_settings()

    name = {
        'auto_restart':'报错重启',
        'delay':'功能时差',
        'username':'用户名'
     }
    
    @staticmethod
    def ask_settings() -> list:
        return {
            'auto_restart':int(input('是否启用报错自动重启？')),
            'delay':float(input('请输入功能时差：')),
            'username':input('请输入用户名:'),
            'version':1
        }
        
