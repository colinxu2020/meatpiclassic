import os

if os.name == 'nt':
    nowin=False

    import winsound

    def clear():
        os.system('cls')
else:
    nowin=True
    
    def clear():
        os.system('clear')
    class winsound(object):
        @staticmethod
        def Beep(*arg, **kwarg):
            pass
        @staticmethod
        def PlaySound(*arg, **kwarg):
            pass
        @staticmethod
        def MessageBeep(*arg, **kwarg):
            pass

        SND_FILENAME=0
        SND_ALIAS=0
        SND_LOOP=0
        SND_MEMORY=0
        SND_PURGE=0
        SND_ASYNC=0
        SND_NODEFAULT=0
        SND_NOSTOP=0
        SND_NOWAIT=0

        MB_ICONASTERISK=0
        MB_ICONEXCLAMATION=0
        MB_ICONHAND=0
        MB_ICONQUESTION=0
        MB_OK=0
