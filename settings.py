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
            cls.settings = cls.ask_settings()
            cls.update_settings()

    name = ['报错重启','功能时差','用户名']
    
    @staticmethod
    def ask_settings() -> list:
        return [int(input('是否启用报错自动重启？')),float(input('请输入功能时差：')),input('请输入用户名:')]
        
    @classmethod
    def ask_and_update_single_settings(cls, idx) -> None:
        idx-=1
        print(cls.name[idx])
        print('目前状态:',cls.settings[idx])
        if idx==2: cls.settings[idx] = input('输入新值:')
        if idx==1: cls.settings[idx] = float(input('输入新值:'))
        else: cls.settings[idx] = int(input('输入新值:'))
        

        
