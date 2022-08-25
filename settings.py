import json


class Settings(object):
    @classmethod
    def load_settings(cls: type) -> None:
        with open('Meatpi_Settings.json', 'r') as fp:
            cls.settings=json.load(fp)
            
    @classmethod
    def store_settings(cls: type) -> None:
        with open('Meatpi_Settings.json', 'w') as fp:
            json.dump(cls.settings, fp)
            
    @classmethod
    def init_settings(cls: type) -> None:
        try:
            cls.load_settings()
        except FileNotFoundError:
            cls.settings = cls.ask_user_settings()
            cls.update_settings()
    name = ['声音','报错重启','已关闭此设置','功能时差','用户名']
    
    @staticmethod
    def ask_settings() -> list:
        return [1,1,-1,0.6,input('Please input your username (will be saved):')]
        
    @classmethod
    def ask_and_update_single_settings(cls, idx) -> None:
        idx-=1
        print(cls.name[idx])
        print('目前状态:',cls.settings[idx])
        if idx!=4: cls.settings[idx] = input('输入新值:')
        else: cls.settings[idx] = int(input('输入新值:'))
        
        
