import time as tm
import os
import webbrowser
import traceback
import math
import keyword
import types
import datetime

from settings import Settings
import crossplatform
import categorymgr as cgmgr
import repllib
import categorybase as cgbase
	

COPYRIGHT= 'CopyrightÂ© 2020-2022 dgncx Org.\nCopyrightÂ© 2020-2022 a9754610_team.\nAll Rights Reserved.\n\n'
        
print('\nInitializing your personal settings...')
    
Settings.init_settings()
crossplatform.clear()
tm.sleep(Settings.settings['delay'])



def isprimebad(k):
    if k==1:
        return 0
    else:
        res = 1
        for i in range(2,k):
            if k%i == 0:
                res = 0
        return res


def ok(now,s):
    if len(s) != 3 or s[0] < 'A' or s[0] > 'I' or int(s[1:]) < 1 or int(s[1:]) > 11 or s == 'D06':
        return 0
    elif now[0] == s[0] and int(s[1:])>int(now[1:]) and not (now[0] == 'D' and int(s[1:])>6>int(now[1:])):
        return 1
    elif now[1:] == s[1:] and ord(now[0])>ord(s[0]) and not (now[1:] == '06' and ord(now[0])>ord('D')>ord(s[0])):
        return 1
    elif ord(now[0])+int(now[1:]) == ord(s[0])+int(s[1:]) and ord(now[0])>ord(s[0]) and not (ord(s[0])+int(s[1:]) == ord('D')+6 and int(s[1:])>6>int(now[1:])):
        return 1
    else:
        return 0


def ok2(now,s):
    if len(s) != 3 or s[0] < 'A' or s[0] > 'K' or int(s[1:]) < 1 or int(s[1:]) > 13 or s == 'D08' or s == 'I03':
        return 0
    elif now[0] == s[0] and int(s[1:])>int(now[1:]) and not(now[0] == 'D' and int(s[1:])>8>int(now[1:])) and not(now[0] == 'I' and int(s[1:])>3>int(now[1:])):
        return 1
    elif now[1:] == s[1:] and ord(now[0])>ord(s[0]) and not(now[1:] == '08' and ord(now[0])>ord('D')>ord(s[0])) and not(now[1:] == '03' and ord(now[0])>ord('I')>ord(s[0])):
        return 1
    elif ord(now[0])+int(now[1:]) == ord(s[0])+int(s[1:]) and ord(now[0])>ord(s[0]) and not(ord(s[0])+int(s[1:])==ord('D')+8 and int(s[1:])>8>int(now[1:])) and not(ord(s[0])+int(s[1:])==ord('I')+3 and int(s[1:])>3>int(now[1:])):
        return 1
    else:
        return 0


def gcd(a,b):
    if a == 1 or b == 1:
        return 1
    elif a == 0 or b == 0:
        return max(a,b)
    else:
        return gcd(b,a%b)



def ins(s,key):
    s2 = fff(int(s),3)
    ls = []
    a = 0
    for i in s2:
        if i in ['0','1']:
            a = a * 10 + int(i)
        elif i == '2':
            a = (int(str(a),base=2) - int(key[3:])) / (int(key[:3])+1)
            a = int(a)
            ls.append(a)
            a = 0
    return ls


def show(tm):
    print()
    print('ć­¤ĺŠźč?˝ć­Łĺś¨ć–˝ĺ·Ąä¸­')
    print()
    tm.sleep(Settings.settings['delay'])
new_map_for_developers = [[]
,[\
[1,1,1,1,1,1,1,1,1,1,1],\
[1,0,0,0,0,0,0,0,0,0,1],\
[1,0,0,0,0,0,0,0,0,0,1],\
[1,0,0,0,0,0,0,0,0,0,1],\
[1,0,0,0,0,0,0,0,0,0,1],\
[1,0,0,0,0,0,0,0,0,0,1],\
[1,0,0,0,0,0,0,0,0,0,1],\
[1,0,0,0,0,0,0,0,0,0,1],\
[1,1,1,1,1,1,1,1,1,1,1]]
]
hfms = [\
[\
[1,1,1,1,1,1,1,1,1,1,1],\
[1,0,1,1,1,0,0,0,0,0,1],\
[1,0,0,0,1,0,0,1,1,1,1],\
[1,0,1,0,0,0,0,0,0,0,1],\
[1,0,1,0,1,0,1,1,0,0,1],\
[1,0,0,0,0,0,0,0,0,0,1],\
[1,0,1,1,1,1,1,1,1,0,1],\
[1,0,0,0,0,0,0,0,0,0,1],\
[1,1,1,1,1,1,1,1,1,1,1]]\
,[\
[1,1,1,1,1,1,1,1,1,1,1],\
[1,0,1,0,0,0,0,0,0,0,1],\
[1,0,0,0,1,0,0,0,0,0,1],\
[1,0,1,0,1,0,1,0,1,0,1],\
[1,0,1,0,0,0,1,0,1,0,1],\
[1,0,0,0,0,0,0,0,1,0,1],\
[1,0,0,0,0,1,0,0,1,0,1],\
[1,0,1,1,1,1,0,0,0,0,1],\
[1,1,1,1,1,1,1,1,1,1,1]]
]
players = [[5,6],[1,1]]
boxes = [[2,6],[6,7]]
targs = [[1,1],[6,3]]


def playhf(tm):
    ops = ['w','a','s','d']
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    print('stages:%d'%(len(hfms)))
    for mp in hfms:
        stage = hfms.index(mp)
        tm.sleep(Settings.settings['delay'])
        crossplatform.clear()
        tm.sleep(Settings.settings['delay'])
        player = players[stage]
        box = boxes[stage]
        targ = targs[stage]
        boxfn = 0
        while not(boxfn) or player != targ:
            crossplatform.clear()
            print("STAGE <%d>"%(stage+1))
            for i in range(9):
                for j in range(11):
                    s = ''
                    if [i,j] == player:
                        s = 'i'
                    elif not(boxfn) and [i,j] == box:
                        s = '@'
                    elif [i,j] == targ:
                        s = 'O'
                    elif mp[i][j]:
                        s = '#'
                    else:
                        s = '.'
                    print(s,end='')
                print()
            op = input('Operation:')
            while op not in ops:
                op = input('ERROR Please try again:')
            dirx = dx[ops.index(op)]
            diry = dy[ops.index(op)]
            onx = player[0]+dirx
            ony = player[1]+diry
            if boxfn and targ == [onx,ony]:
                player = [onx,ony]
                continue
            if mp[onx][ony]:
                continue
            elif box != [onx,ony]:
                player = [onx,ony]
            elif mp[onx+dirx][ony+diry]:
                continue
            else:
                player = [onx,ony]
                box = [onx+dirx,ony+diry]
            if box == targ:
                boxfn = 1


def main():
    crossplatform.winsound.Beep(400,600)
    shf = 0
    do21 = 0
    ss = 'ćśŞč®ľç˝®ć•°ćŤ®'
    cgmgr.search()
    while True:
        cur=cgbase.root
        while isinstance(cur,cgbase.Node):
            print('ćś¬çş§ĺ?«ĺŠźč?˝ĺ?—čˇ¨ďĽš')
            subclasscount=len(cur.childrens)
            for idx,itm in enumerate(cur.childrens):
                print(1+idx,': ',itm.cur.__doc__)
            idx=0
            rawidxmap=[]
            for rawidx,itm in enumerate(dir(cur.cur)):
                if isinstance(getattr(cur.cur,itm),types.FunctionType) and not itm.startswith('_') and getattr(cur.cur,itm) in cur.cur.__functions__:
                    print(1+subclasscount+idx,': ',getattr(cur.cur,itm).__doc__)
                    rawidxmap.append(rawidx)
                    idx+=1
            inp=int(input('čŻ·é€‰ć‹©ďĽš'))-1
            if inp==-1:
                print('ĺ·˛ĺ?ŻĺŠ¨Meatpič°?čŻ•ćŽ§ĺ?¶ĺŹ°')
                print('čŻ·ä˝żç”¨repllibĺ…łé—­č°?čŻ•ćŽ§ĺ?¶ĺŹ°')
                print('čŻ·ĺś¨ä»»ä˝•REPLä¸­ĺŻĽĺ…Ąrepllibĺş“ĺŹ‘é€?č°?čŻ•äżˇć?Ż')
                repl=repllib.ReplServer(globals(),'127.0.0.1',9987)
                try:
                    repl.wait_forever()
                finally:
                    repl.close()
            elif inp<subclasscount:
                cur=cur.childrens[inp]
            elif inp>=subclasscount+len(rawidxmap):	
                print('čľ“ĺ…Ąć— ć•?')
                tm.sleep(Settings.settings['delay'])
                return
            else:
                cur=getattr(cur.cur,dir(cur.cur)[rawidxmap[inp-subclasscount]])
        
        cur()
            
        
        """        run52 = 0
        print('*^'*36+'*')
        print('<',tm.asctime(tm.localtime(tm.time())),'>')
        print('ć¬˘čżŽä˝żç”¨PSCCOçš„meatĎ€ â€”â€”â€”â€”a97')
        print('meatĎ€2ĺ‘¨ĺą´ĺ·˛ĺ?°ďĽ?')
        print('''
-> 1.č®ˇç®—ç±»ĺŠźč?˝
-> 2.ĺ·Ąĺ…·ç±»ĺŠźč?˝
-> 3.ć¸¸ć?Źç±»ĺŠźč?˝''')
        if shf == 0:
            print('-> 4.?????????')
        else:
            print('-> 4.č±Şvançš„ĺ°Źć¸¸ć?Źâ€śćŽ¨ç®±ĺ­?â€ťďĽ?ďĽ?ďĽ?')
        bm = input('''ĺˇ«ć­Łçˇ®çš„ĺşŹĺŹ· ĺ¦‚ 3ďĽš''')
        crossplatform.clear()
        if bm == '1':
            print(r'''---> 01.ć™®é€šč®ˇç®—ĺ™¨
---> 02.č´¨ć•°ĺ?¤ć–­ĺ™¨,ĺŚ…ć‹¬ä»Ąä¸‹ĺŠźč?˝ďĽš
---> -> 1.čľ“ĺ‡şä¸€ĺ?°ĺ‡ ä»Ąĺ†…çš„č´¨ć•°
---> -> 2.čľ“ĺ‡şä»Žä¸€ä¸Şć•°ĺ?°ĺŹ¦ä¸€ä¸Şć•°çš„č´¨ć•°
---> -> 3.ĺ?¤ć–­ä¸€ä¸Şć•°ć?Żä¸Ťć?Żč´¨ć•°
---> 03.ç­‰ĺ·®ć•°ĺ?—ć±‚ĺ’Ś
---> 04.ĺŚ–ç®€ĺ?†ć•°
---> 07.ćś€ĺ°Źĺ…¬ĺ€Ťć•°
---> 08.ç®—24
---> 12.ćś€ĺ¤§ĺ…¬ĺ› ć•°
---> 13.č§ŁäşŚĺ…?ä¸€ć¬ˇć–ąç¨‹
---> 14.č§Łä¸€ĺ…?äşŚć¬ˇć–ąç¨‹
---> 15.č´¨ĺ› ć•°ĺ?†č§Ł
---> 20.č®ˇç®—Ď€
---> 31.č®ˇç®—ĺąłĺť‡ć•°
---> 33.ĺ¸•ć–ŻĺŤˇä¸‰č§’ĺ˝˘''')
        if bm == '2':
            print(r'''---> 05.ĺŤ?čż›ĺ?¶ĺŹ?ĺ‡ čż›ĺ?¶
---> 06.ĺ‡ čż›ĺ?¶ĺŹ?ĺŤ?čż›ĺ?¶
---> 16.ç”źć??ĺ‹ľč‚ˇć•°
---> 17.ĺŠ ĺŻ†ć–‡ćś¬(ä¸Ťĺ®‰ĺ…¨)
---> 18.č§ŁĺŻ†ć–‡ćś¬(ä¸Ťĺ®‰ĺ…¨)
---> 19.ç”»ĺż?
---> 22.ç”»ćťż
---> 25.ć›´ć”ąć?–ćźĄçś‹ć•°ćŤ®(ĺŹŻäżťĺ­?ä¸şć–‡ä»¶)
---> 28.č®ˇć—¶ĺ™¨
---> 30.ç”źć??éšŹćśşć•°
---> 36.ä˝śč€…çš„čŻť
---> 37.ä¸Šç˝‘
---> 39.ĺť‘ç˘źć¸¸ć?Źč§Łćž?
---> 42.ĺ·˛ĺ?śç”¨
---> 43.äż®ć”ąé…Ťç˝®
---> 45.meatĎ€é˘?č§Łĺş“(ĺ·˛ĺşź)
---> 47.çśźÂ·ĺŠ ĺŻ†ĺ’Śč§ŁĺŻ†(ĺ®‰ĺ…¨ç‰?)
---> 48.ä¸‹č˝˝ć´›č°·ć–‡ä»¶
---> 52.ćŻ?ç?­ĺ?§(éˇľĺ?Ťć€ťäą‰)
---> 53.ć„źč°˘ĺ?ŤĺŤ•
---> 55.ĺ±•ç¤şlogo
---> 56.meatpi 2ĺ‘¨ĺą´ĺ€’č®ˇć—¶(ĺ·˛ç»“ćťź)
---> 58.MSTS
---> 59.ć¸…é™¤čľ“ĺ‡ş''')
        if bm == '3':
            print(r'''---> 09.č®ˇç®—ć¸¸ć?Ź
---> 10.ć‰“ĺ­—ć¸¸ć?Ź
---> 11.çŚść•°ć¸¸ć?Ź1
---> 21.ĺť‘ç˘źć¸¸ć?Źç»Źĺ…¸ç‰?
---> 23.éźłäą?ĺ¤§ĺ¸?
---> 24.ĺť‘ç˘źć¸¸ć?ŹĺŤ‡çş§ç‰?
---> 26.çŚść•°ć¸¸ć?Ź2
---> 27.äż„ç˝—ć–Żć–ąĺť—
---> 29.ćµ‹čŻ•ĺŹŤĺş”é€źĺş¦
---> 32.ć‰«é›·
---> 34.çźłĺ¤´ĺ‰Şĺ?€ĺ¸?
---> 35.2ĺ±‚čż·ĺ®«(ä˝“éŞŚç‰?,ä»Ąĺ?ŽäĽšćś‰ć›´ĺ¤šĺś°ĺ›ľ)
---> 38.ĺ¤±ć?Žčż·ĺ®«(ä˝“éŞŚç‰?,ä»Ąĺ?ŽäĽšćś‰ć›´ĺ¤šĺś°ĺ›ľ)
---> 40.FJçš„ĺŤˇç‰Ść¸¸ć?Ź
---> 41.ć­¤ĺŠźč?˝ĺ› ç‰ąć®ŠĺŽźĺ› ĺ·˛ä¸Šé”?
---> 44.2048 [ćµ‹čŻ•é?¶ć®µ]
---> 46.Pots
---> 49.çŚść•°ć¸¸ć?Ź3
---> 50.ĺ› ĺĽŹĺ?†č§Łĺ°Źç»?äą 
---> 51.č®ˇç®—ĺą¸čż?ć•°ĺ­—(ä¸Ťć?Żé‚Łç§Ťç”¨ç”źć—Ąç®—çš„ĺž?ĺśľç¨‹ĺşŹ)
---> 54.ć•°ĺ­¦éŞ—ç´«
---> 57.ĺ®šć—¶ç‚¸éŞ—''')
        if bm == '4':
            if shf == 0:
                print('---> 2293.čŻ·ĺś¨ä¸‹ć–ąĺˇ«ĺşŹĺŹ·ĺ¤„ĺˇ«â€?2293â€™')  # Colinxu2020č®°ďĽšA97çš„é”®ç›?ĺťŹćŽ‰äş†ďĽź
            else:
                playhf(tm)
                continue
        m = input('''ĺˇ«ć­Łçˇ®çš„ĺşŹĺŹ· ĺ¦‚ 02ďĽš''')
        crossplatform.clear()
        if m == '01':
            print('''ç‰ąć®Ščż?ç®—ç¬¦ĺŹ·ďĽš
%  ĺŹ–ä˝™
**  ć¬ˇć–ą  
//  ć•´é™¤
<<  ĺ·¦ç§»
>>  ĺŹłç§»
>=  ĺ¤§äşŽç­‰äşŽ
<=  ĺ°ŹäşŽç­‰äşŽ
==  ç­‰äşŽ
!=  ä¸Ťç­‰äşŽ
and  ä¸Ž
or  ć?–
not  éťž
True  ć?Ż
False  ĺ?¦
abs()  ç»ťĺŻąĺ€Ľ''')
            try:
                print('ç­”ćˇ?ć?ŻďĽš', eval(input('čŻ·čľ“ĺ…Ąç®—ĺĽŹďĽ?ä¸Ťĺ¸¦=ďĽ‰ďĽš')))
            except ZeroDivisionError:
                print('ç®—ĺĽŹä¸­ĺ?«ćś‰é™¤ä»Ą0ďĽŚć— ćł•č®ˇç®—')
            except SyntaxError:
                print('ć— ćł•č®ˇç®—')
        elif m == '02':
            while True:
                inp = input('''1.čľ“ĺ‡şä¸€ĺ?°ĺ‡ ä»Ąĺ†…çš„č´¨ć•°
2.čľ“ĺ‡şä»Žä¸€ä¸Şć•°ĺ?°ĺŹ¦ä¸€ä¸Şć•°çš„č´¨ć•°
3.ĺ?¤ć–­ä¸€ä¸Şć•°ć?Żä¸Ťć?Żč´¨ć•°
4.é€€ĺ‡şč´¨ć•°ĺ?¤ć–­ĺ™¨
ĺˇ«1,2,3ć?–4ďĽš''')
                bl = True
                if inp == '1':
                    print('čż?čˇŚć—¶é—´ĺŹŻč?˝ćŻ”čľ?é•żďĽŚčŻ·č€?ĺż?ç­‰ĺľ…')
                    inp_1 = int(input('ä˝ ć?łçźĄé?“ä»Žä¸€ĺ?°ĺ‡ çš„č´¨ć•°ďĽź '))
                    while inp_1 < 2:
                        print('ä¸Ťč?˝ĺ°ŹäşŽ2ĺ“¦ďĽ?čŻ·é‡Ťć–°čľ“ĺ…Ą')
                        inp_1 = int(input('ä˝ ć?łçźĄé?“ä»Žä¸€ĺ?°ĺ‡ çš„č´¨ć•°ďĽź '))
                    ls = []
                    for i in range(inp_1+1):
                        ls.append(1)
                    for inp_el in range(2,inp_1+1):
                        if ls[inp_el]==1:
                            for k in range(inp_el**2,inp_1+1,inp_el):
                                ls[k] = 0
                    print('ä»Ąä¸‹ć?Żé‚Łć®µć•°ĺ­—é‡Śçš„č´¨ć•°')
                    ls2=[]
                    for i in range(2,inp_1+1):
                        if ls[i] == 1:
                            ls2.append(i)
                    print(ls2)
                    print('ćś‰',len(ls2),'ä¸Şč´¨ć•°')
                elif inp == '2':
                    print('čż?čˇŚć—¶é—´ĺŹŻč?˝ćŻ”čľ?é•żďĽŚčŻ·č€?ĺż?ç­‰ĺľ…')
                    ls = []
                    inp_4_1 = int(input('ä˝ ć?łä»Žĺ‡ ĺĽ€ĺ§‹čŻ´č´¨ć•°ďĽź '))
                    while inp_4_1 < 2:
                        print('ä¸Ťč?˝ĺ°ŹäşŽ2,čŻ·é‡Ťć–°čľ“ĺ…Ą')
                        inp_4_1 = int(input('ä˝ ć?łä»Žĺ‡ ĺĽ€ĺ§‹čŻ´č´¨ć•°ďĽź '))
                    inp_4_2 = int(input('ä˝ ć?łĺ?°ĺ‡ ç»“ćťźčŻ´č´¨ć•°ďĽź '))
                    while inp_4_2 <= inp_4_1:
                        print(f'ĺż…éˇ»ĺ¤§äşŽ{inp_4_1},čŻ·é‡Ťć–°čľ“ĺ…Ą')
                        inp_4_2 = int(input('ä˝ ć?łĺ?°ĺ‡ ç»“ćťźčŻ´č´¨ć•°ďĽź '))
                    ls = []
                    for i in range(inp_4_2+1):
                        ls.append(1)
                    for inp_el in range(2,inp_4_2+1):
                        if ls[inp_el]==1:
                            for k in range(inp_el**2,inp_4_2+1,inp_el):
                                ls[k] = 0
                    print('ä»Ąä¸‹ć?Żé‚Łć®µć•°ĺ­—é‡Śçš„č´¨ć•°')
                    ls2=[]
                    for i in range(2,inp_4_2+1):
                        if ls[i] == 1 and i >= inp_4_1:
                            ls2.append(i)
                    print(ls2)
                    print('ćś‰',len(ls2),'ä¸Şč´¨ć•°')
                elif inp == '3':
                    print('čż?čˇŚć—¶é—´ĺŹŻč?˝ćŻ”čľ?é•żďĽŚčŻ·č€?ĺż?ç­‰ĺľ…')
                    inp_2 = int(input('ä˝ ć?łçźĄé?“ĺ“Şä¸Şć•°ć?Żä¸Ťć?Żč´¨ć•°ďĽź '))
                    if inp_2 <= 1:
                        print('ä¸Ťć?Ż')
                    for cpr_num in range(2,inp_2):
                        if inp_2 % cpr_num == 0:
                            print('ä¸Ťć?Ż')
                            bl = False
                            break
                    if bl :
                        print('ć?Ż')
                elif inp == '4':
                    break
                else:
                    print('čľ“ĺ…Ąć— ć•?')
        elif m == '03':
            s = int(input('ć•°ĺ?—ä»Žĺ‡ ĺĽ€ĺ§‹ďĽź '))
            e = int(input('ć•°ĺ?—ĺ?°ĺ‡ ç»“ćťźďĽź '))
            while e <= s:
                    print(f'ĺż…éˇ»ĺ¤§äşŽ{s},čŻ·é‡Ťć–°čľ“ĺ…Ą')
                    e = int(input('ĺ?°ĺ‡ ç»“ćťźďĽź '))
            while True:
                q = input('çźĄé?“ç›¸é‚»çš„ä¸¤ä¸Şć•°é—´éš”čľ“ĺ…Ą1ďĽŚçźĄé?“ä¸Şć•°čľ“ĺ…Ą2ďĽš')
                if q == '1':
                    d = int(input('é—´éš”ĺ¤šĺ°‘ďĽź '))
                    n = (e-s)/d+1
                elif q == '2':
                    n = int(input('ä¸Şć•°ć?Żĺ‡ ďĽź '))
                else:
                    print('čľ“ĺ…Ąć— ć•?')
                    continue
                print('ç­”ćˇ?ć?Ż',(s+e)*n/2)
                break
        elif m == '04':
            a = int(input('ĺ?†ĺ­?ďĽź '))
            b = int(input('ĺ?†ćŻŤďĽź '))
            i = 2
            while i < ((a+b)-abs(a-b))/2+1:
                if a % i == 0 and b % i == 0:
                    a,b = a / i,b / i
                else:
                    i += 1
            print('ĺŚ–ç®€ĺ?Žçš„ĺ?†ć•°ć?ŻďĽš',int(a),'/',int(b))
        elif m == '05':
            n = int(input('č¦?č˝¬ćŤ˘çš„ć•°ć?ŻďĽź '))
            x = int(input('č¦?č˝¬ćŤ˘ć??ĺ¤šĺ°‘čż›ĺ?¶ďĽź '))
            print(fff(n,x))
        elif m == '06':
            q = input('č¦?č˝¬ćŤ˘çš„ć•°ć?ŻďĽź ')
            nm = int(input('čż™ä¸Şć•°ć?Żĺ¤šĺ°‘čż›ĺ?¶çš„ďĽź '))
            try:
                print(int(q,nm))
            except ValueError:
                print("ć•°ćŤ®čľ“ĺ…Ąé”™čŻŻ")
        elif m == '07':
            a = int(input('ç¬¬ä¸€ä¸Şć•°ć?Żĺ‡ ďĽź '))
            b = int(input('ç¬¬äşŚä¸Şć•°ć?Żĺ‡ ďĽź '))
            print('ç­”ćˇ?ć?Ż',math.lcm(a,b))
        elif m == '08':
            ls=[]
            allres = []
            allres2 = []
            ls.append(int(input('ç¬¬1ä¸Şć•°:')))
            ls.append(int(input('ç¬¬2ä¸Şć•°:')))
            ls.append(int(input('ç¬¬3ä¸Şć•°:')))
            ls.append(int(input('ç¬¬4ä¸Şć•°:')))
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        for l in range(4):
                            if i!=j and i!=k and i!=l and j!=k and j!=l and k!=l:
                                ls2 = [ls[i],ls[j],ls[k],ls[l]]
                                for m in range(216):
                                    res = str(ls2[0])
                                    for now in range(1,4):
                                        nowele = ls2[now]
                                        if ((m%(6**(now)))//((6**(now-1)))) == 0:
                                            res += '+'+str(nowele)
                                        if ((m%(6**(now)))//((6**(now-1)))) == 1:
                                            res += '*'+str(nowele)
                                        if ((m%(6**(now)))//((6**(now-1)))) == 2:
                                            res += '-'+str(nowele)
                                        if ((m%(6**(now)))//((6**(now-1)))) == 3:
                                            res = str(nowele) + '-' + res
                                        if ((m%(6**(now)))//((6**(now-1)))) == 4:
                                            res += '/'+str(nowele)
                                        if ((m%(6**(now)))//((6**(now-1)))) == 5:
                                            res = str(nowele) + '/' + res
                                        res = '(' + res + ')'
                                    try:
                                        if abs(int(res)-24) <= 0.001:
                                            allres.append(res)
                                    except Exception:
                                        pass
                                for m in range(216):
                                    res = ''
                                    res1 = ''
                                    res2 = ''
                                    if ((m%(6**1))//((6**(0)))) == 0:
                                        res1 = '('+str(ls[0])+'+'+str(ls[1])+')'
                                    if ((m%(6**1))//((6**(0)))) == 1:
                                        res1 = '('+str(ls[0])+'*'+str(ls[1])+')'
                                    if ((m%(6**1))//((6**(0)))) == 2:
                                        res1 = '('+str(ls[0])+'-'+str(ls[1])+')'
                                    if ((m%(6**1))//((6**(0)))) == 3:
                                        res1 = '('+str(ls[1])+'-'+str(ls[0])+')'
                                    if ((m%(6**1))//((6**(0)))) == 4:
                                        res1 = '('+str(ls[0])+'/'+str(ls[1])+')'
                                    if ((m%(6**1))//((6**(0)))) == 5:
                                        res1 = '('+str(ls[1])+'/'+str(ls[0])+')'
                                    if ((m%(6**3))//((6**(2)))) == 0:
                                        res2 = '('+str(ls[2])+'+'+str(ls[3])+')'
                                    if ((m%(6**3))//((6**(2)))) == 1:
                                        res2 = '('+str(ls[2])+'*'+str(ls[3])+')'
                                    if ((m%(6**3))//((6**(2)))) == 2:
                                        res2 = '('+str(ls[2])+'-'+str(ls[3])+')'
                                    if ((m%(6**3))//((6**(2)))) == 3:
                                        res2 = '('+str(ls[3])+'-'+str(ls[2])+')'
                                    if ((m%(6**3))//((6**(2)))) == 4:
                                        res2 = '('+str(ls[2])+'/'+str(ls[3])+')'
                                    if ((m%(6**3))//((6**(2)))) == 5:
                                        res2 = '('+str(ls[3])+'/'+str(ls[2])+')'
                                    if ((m%(6**2))//((6**(1)))) == 0:
                                        res = '('+res1+'+'+res2+')'
                                    if ((m%(6**2))//((6**(1)))) == 1:
                                        res = '('+res1+'*'+res2+')'
                                    if ((m%(6**2))//((6**(1)))) == 2:
                                        res = '('+res1+'-'+res2+')'
                                    if ((m%(6**2))//((6**(1)))) == 3:
                                        res = '('+res2+'-'+res1+')'
                                    if ((m%(6**2))//((6**(1)))) == 4:
                                        res = '('+res1+'/'+res2+')'
                                    if ((m%(6**2))//((6**(1)))) == 5:
                                        res = '('+res2+'/'+res1+')'
                                    try:
                                        if abs(int(res)-24) <= 0.001:
                                            allres.append(res)
                                    except Exception:
                                        pass
            for res in allres:
                if res not in allres2:
                    allres2.append(res)
                    print(res)
            if len(allres) == 0:
                print('ć— ćł•ç®—ĺ‡ş24ďĽ?')
        elif m == '09':
            ri = 0
            ttime = 0
			
            for cd in [3,2,1]:
                print(cd)
                tm.sleep(Settings.settings['delay'])
            for n in range(1,q+1):
                a = random.randint(1,100)
                b = random.randint(1,100)
                start = tm.time()
                print('ç¬¬%ié?“é˘?ďĽš%i + %i = '%(n,a,b),end='')
                re_i = int(input(''))
                end = tm.time()
                ttime += end - start
                if re_i == a+b:
                    print('ç­”ĺŻąäş†ďĽ?')
                    ri += 1
                else:
                    print('ç­”é”™äş†ă€‚ă€‚ă€‚')
            print('ĺąłĺť‡ć—¶é—´ďĽš%.2f ç§’'%(ttime/q))
            print('ć­Łçˇ®çŽ‡ďĽš',ri/q*100,'%')
            print('ĺ?†ć•°ďĽš%.2fďĽ?č¶…čż‡100ĺ°±ç®—ĺŽ‰ĺ®łçš„ĺ•¦ďĽ‰'%(ri/q*100/(ttime/q/2.8)))
        elif m == '10':
            ttime,tlen = 0,0
            ri = 0
            q = int(input('ä¸€ĺ…±č¦?ĺ¤šĺ°‘é?“é˘?ďĽź'))
            for cd in [3,2,1]:
                print(cd)
                tm.sleep(Settings.settings['delay'])
            for n in range(1,q+1):
                kwc = random.choice(keyword.kwlist)
                print(kwc,end=' čŻ·ć‰“ĺ‡şç›¸ĺ?Śçš„ĺŤ•čŻŤ:')
                start = tm.time()
                kwcin = input()
                end = tm.time()
                ttime,tlen = ttime+(end-start),tlen+len(kwc)
                if kwcin == kwc:
                    ri += 1
            print('ć‰“ĺ‡şä¸€ä¸Şĺ­—ćŻŤç”¨çš„ĺąłĺť‡ć—¶é—´ďĽš%.2f ç§’'%(ttime/tlen))
            print('ć­Łçˇ®çŽ‡ďĽš',ri/q*100,'%')
            print('Tĺ€ĽďĽš%d (ä˝śč€…äş˛ćµ‹227)'%(int(tlen/ttime*ri/q*100)))
        elif m == '11':
            print('ĺ› ä¸şColinxu2020ĺ®žĺś¨ć?žä¸Ťć‡‚A97_QWQć?Żć€Žäą?č®©ä¸‹éť˘çš„nč˘«ĺŁ°ć?Žä¸şListç±»ĺž‹çš„ďĽŚć•…č€ŚColinxu2020ĺŹŞĺľ—ĺ?‡č®ľäĽšĺ‡şçŽ°é”™čŻŻďĽŚćŠŠćś¬ĺŠźč?˝ć”ľĺ…Ąç»´ćŠ¤ĺŠźč?˝ä¸­')
            while input('äş†č§ŁďĽź(Y/N)')=='N':
                pass
            raise RuntimeError('ç»´ćŠ¤ä¸­...')
            n2 = int(input("ä˝ č¦?é€‰ä¸€ä¸Şä»Ž0ĺ?°nçš„ć•°ďĽŚč®©ç”µč„‘çŚśä˝ é€‰çš„ć?Żĺ“Şä¸Şć•°ďĽŚčŻ·čľ“ĺ…Ąn:"))
            copyn=n
            a = ''
            while copyn != 0:
                w = copyn%2
                if w > 10:
                    print('')
                    w = l[n.index(w)]
                a += str(w)
                copyn = copyn//2
            a = a[::-1]
            l = len(a)
            input(f'čŻ·é€‰ä¸€ä¸Şä»Ž0ĺ?°{b1}çš„ć•°ďĽŚč®°ĺś¨ĺż?é‡ŚďĽŚć?łĺĄ˝äş†ćŚ‰ĺ›žč˝¦')
            inp = []
            ls = []
            for i in range(0,2**l):
                a = bin(i)[2:]
                for i in range(l-len(a)):
                    a = '0'+a
                ls.append(a)
            for i in range(l):
                tda = []
                for tn in ls:
                    if (tn[0-(i+1)] == '1'):
                        tda.append(tn)
                tda2 = []
                for tt in tda:
                    tt2 = 0
                    for j in range(len(tt)):
                        tt2 += (2**j)*int(tt[0-(j+1)])
                    if tt2 <= bl:
                        tda2.append(tt2)
                print('čż™ä¸Şć•°ĺś¨',tda2,'é‡Śĺ?—ďĽź(ĺ?¦:0,ć?Ż:1)')
                inp.append(int(input()))
            it = 0
            for i in range(l):
                it += (2**i)*inp[i]
            print('ä˝ é€‰çš„ć•°ć?Ż',it)
        elif m == '12':
            a = int(input('ç¬¬ä¸€ä¸Şć•°ć?Żĺ‡ ďĽź '))
            b = int(input('ç¬¬äşŚä¸Şć•°ć?Żĺ‡ ďĽź '))
            for i in range(1,min(a,b)+1)[::-1]:
                if a%i == 0 and b%i == 0:
                    print('ç­”ćˇ?ć?Ż',i)
                    break
        elif m == '13':
            ls = []
            print('''äşŚĺ…?ä¸€ć¬ˇć–ąç¨‹ć ‡ĺ‡†ĺ˝˘ĺĽŹďĽš
ax + by + c = 0
dx + ey + f = 0''')
            for i in ['a','b','c','d','e','f']:
                ls.append(int(input(('čŻ·čľ“ĺ…Ą'+i+':'))))
            a,b,c,d,e,f = ls[0],ls[1],ls[2],ls[3],ls[4],ls[5]
            print('x =',(c*e-b*f)/(b*d-a*e))
            print('y =',(c*d-a*f)/(a*e-b*d))
        elif m == '14':
            print('''ä¸€ĺ…?äşŚć¬ˇć–ąç¨‹ć ‡ĺ‡†ĺ˝˘ĺĽŹďĽš
axÂ˛ + bx + c = 0''')
            a = int(input('čŻ·čľ“ĺ…ĄaďĽš'))
            b = int(input('čŻ·čľ“ĺ…ĄbďĽš'))
            c = int(input('čŻ·čľ“ĺ…ĄcďĽš'))
            if (0-(c/a)) >= 0:
                if b/2/a >= 0:
                    print('x =',(b*b-4*a*c)/(4*a*a),'çš„ĺąłć–ąć ą -',b/2/a,'(',((b*b-4*a*c)/(4*a*a))**0.5-b/2/a,'ć?–',0-((b*b-4*a*c)/(4*a*a))**0.5-b/2/a,')')
                else:
                    print('x =',(b*b-4*a*c)/(4*a*a),'çš„ĺąłć–ąć ą +',0- (b/2/a),'(',(b*b-4*a*c)/(4*a*a)**0.5-b/2/a,'ć?–',0-((b*b-4*a*c)/(4*a*a))**0.5-b/2/a,')')
            else:
                print('ć— ĺ®žć•°č§Ł'+chr(10006))
        elif m == '15':
            n = int(input('čŻ·čľ“ĺ…Ąć?łĺ?†č§Łçš„ć•°ďĽš'))
            if n < 1:
                print('ć— ćł•ĺ?†č§Ł')
            else:
                ls = []
                x = 2
                while n != 1:
                    while n % x == 0:
                        n /= x
                        ls.append(x)
                    x += 1
                print('ĺ?†č§Łĺ?Žçš„ĺ?—čˇ¨',ls)
        elif m == '16':
            a = int(input('čŻ·čľ“ĺ…ĄĺŹ‚ć•°ďĽš'))
            x = a*2-1
            y = (x*x-1)/2
            z = y + 1
            print('ç»“ćžśďĽš',x,y,z)
        elif m == '17':
            x = input('čľ“ĺ…Ąč¦?ĺŠ ĺŻ†ć–‡ćś¬:')
            key = input('čľ“ĺ…ĄĺŠ ĺŻ†ĺŻ†ç ?(ĺ…­ä˝Ťć•´ć•°):')
            s = ''
            for y in range(len(x)):
                res = ord(x[y])
                s += bin(res*(int(key[:3])+1)+int(key[3:]))[2:]+'2'
            n = int(s,base=3)
            print(n,'\n')
        elif m == '18':
            res = ''
            n = input('čľ“ĺ…Ąĺ·˛ĺŠ ĺŻ†ć–‡ćś¬:')
            key = input('čľ“ĺ…ĄĺŠ ĺŻ†ĺŻ†ç ?(ĺ…­ä˝Ťć•´ć•°):')
            x = ins(n,key)
            for i in x:
                res += chr(i)
            print(res)
        elif m == '19':
            import turtle as t
            t.clear()
            cor = []
            t.speed(0)
            t.seth(0)
            t.shape('classic')
            t.color('black')
            t.up()
            t.goto(0,0)
            if do21:
                t2.clear()
                t2.shape('blank')
            l = int(input("čľ“ĺ…Ąé•żĺş¦ďĽ?ĺ?Źç´ ďĽ‰:"))
            d = 145
            print('čŻ·č€?ĺż?ç­‰ĺľ…')
            t.fillcolor('red')
            t.begin_fill()
            for i in range(145):
                i2 = i + 1
                nowl = i2*l/145
                t.home()
                t.lt(125)
                t.lt(i2)
                t.fd(nowl)
                cor.append([t.xcor(),t.ycor()])
                t.goto(0,0)
            t.down()
            for i in cor[1:]:
                t.goto(i[0],i[1])
            t.up()
            t.home()
            cor = []
            for i in range(145):
                i2 = i + 1
                nowl = i2*l/145
                t.home()
                t.lt(55)
                t.rt(i2)
                t.fd(nowl)
                cor.append([t.xcor(),t.ycor()])
                t.goto(0,0)
            t.down()
            for i in cor[1:]:
                t.goto(i[0],i[1])
            t.end_fill()
        elif m == '20':
            ls = [0,0,0,0,0,0,0,0,0,0]
            qu = int(input('č¦?č®ˇç®—ĺ?°ĺ°Źć•°ç‚ąĺ?Žç¬¬ĺ‡ ä˝ŤďĽź'))
            co,k, a, b, a1, b1 = -1,2, 4, 1, 12, 4
            while True:
                p, q, k = k*k, 2*k+1, k+1
                a, b, a1, b1 = a1, b1, p*a+q*a1, p*b+q*b1
                d, d1 = a/b, a1/b1
                while d == d1:
                    if co == -1:
                        print(int(d),end = '.')
                    else:
                        print(int(d),end = '')
                    ls[int(d)] += 1
                    co,a, a1 = co+1,10*(a%b), 10*(a1%b1)
                    d, d1 = a/b, a1/b1
                    if co == qu:
                        break
                if co == qu:
                    break
            print('\nć•°ĺ­—ä¸Şć•°ďĽŚĺŚ…ć‹¬ä¸Şä˝Ťçš„3:')
            for i in range(10):
                print(i,':',ls[i],'ä¸Ş')
        elif m == '21':
            import turtle as t
            if do21:
                t2.clear()
                t2.shape('blank')
            do21 = 1
            t.clear()
            t.color('black')
            t.up()
            t.goto(0,0)
            t.down()
            t.seth(0)
            t.speed(0)
            t.shape('square')
            t2 = t.Turtle()
            t2.up()
            t2.shape('square')
            t2.goto(110,110)
            lsa = ['I','H','G','F','E','D','C','B','A','']
            lsb = ['01','02','03','04','05','06','07','08','09','10','11','']
            keypoint = ['E03','H07','D05','F08','B09','C10','A11']
            for i in range(10):
                t.fd(220)
                t.bk(220)
                t.up()
                t.rt(180)
                t.fd(20)
                t.write(lsa[i],font=('Arial',16))
                t.bk(20)
                t.lt(180)
                t.down()
                if i != 9:
                    t.lt(90)
                    t.fd(20)
                    t.rt(90)
            t.up()
            t.goto(0,0)
            t.down()
            t.lt(90)
            for i in range(12):
                t.fd(180)
                t.bk(180)
                t.up()
                t.rt(180)
                t.fd(20)
                t.write(lsb[i],font=('Arial',9))
                t.bk(20)
                t.lt(180)
                t.down()
                if i != 11:
                    t.rt(90)
                    t.fd(20)
                    t.lt(90)
            print('''č§„ĺ?™ďĽš
ä»ŽI01ĺ‡şĺŹ‘ďĽŚç»?ç‚ąć?ŻA11ďĽŚćŻŹć¬ˇć“Ťä˝śĺŹŻä»Ąĺľ€ä¸Ščµ°ä»»ć„Źć ĽďĽŚĺľ€ĺŹłčµ°ä»»ć„Źć ĽďĽŚć?–ĺľ€ĺŹłä¸Ščµ°ä»»ć„Źć ĽďĽŚä˝ ĺ’Śç”µč„‘č˝®ćµ?čż›čˇŚć“Ťä˝śďĽŚč°?ĺ…?ĺ?°ç»?ç‚ąč°?ĺ°±čµ˘ă€‚''')
            t.up()
            t.goto(10,10)
            t.down()
            s = 'I01'
            x = input('č°?ĺ…?ćťĄďĽ?ç”µč„‘ĺ…?ćťĄčľ“ĺ…Ą1ďĽŚä˝ ĺ…?ćťĄčľ“ĺ…Ą2ďĽ‰ďĽź')
            if x == '2':
                while s != 'A11':
                    t.color('blue')
                    s2 = input('ä˝ ć?łčµ°ĺ?°ĺ“Şé‡ŚďĽź')
                    while not ok(s,s2):
                        s2 = input('čµ°ä¸Ťĺ?°ďĽŚčŻ·é‡Ťć–°čľ“ĺ…ĄďĽš')
                    s = s2
                    t.goto(lsb.index(s2[1:])*20+10,lsa.index(s2[0])*20+10)
                    tm.sleep(Settings.settings['delay'])
                    for i in keypoint:
                        if ok(s,i):
                            t.color('red')
                            print('ç”µč„‘ĺ†łĺ®ščµ°ĺ?°',i)
                            s = i
                            t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
                print('ç”µč„‘čµ˘äş†ďĽ?ďĽ?ďĽ?')
            else:
                while True:
                    t.color('red')
                    m = 1
                    for i in keypoint:
                        if ok(s,i):
                            print('ç”µč„‘ĺ†łĺ®ščµ°ĺ?°',i)
                            m = 0
                            s = i
                            t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
                    if m:
                        cc = random.randint(1,4)
                        if cc == 1 and ok(s,chr(ord(s[0])-1)+s[1:]):
                            print('ç”µč„‘ĺ†łĺ®ščµ°ĺ?°',chr(ord(s[0])-1)+s[1:])
                            s = chr(ord(s[0])-1)+s[1:]
                            t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
                        elif cc == 2 and ok(s,s[0]+((int(s[1:])+1)<10)*'0'+str(int(s[1:])+1)):
                            s = s[0]+((int(s[1:])+1)<10)*'0'+str(int(s[1:])+1)
                            print('ç”µč„‘ĺ†łĺ®ščµ°ĺ?°',s)
                            t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
                        else:
                            s = chr(ord(s[0])-1)+((int(s[1:])+1)<10)*'0'+str(int(s[1:])+1)
                            print('ç”µč„‘ĺ†łĺ®ščµ°ĺ?°',s)
                            t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
                    if s == 'A11':
                        print('ç”µč„‘čµ˘äş†ďĽ?ďĽ?ďĽ?')
                        break
                    t.color('blue')
                    s2 = input('ä˝ ć?łčµ°ĺ?°ĺ“Şé‡ŚďĽź')
                    while not ok(s,s2):
                        s2 = input('čµ°ä¸Ťĺ?°ďĽŚčŻ·é‡Ťć–°čľ“ĺ…ĄďĽš')
                    s = s2
                    t.goto(lsb.index(s2[1:])*20+10,lsa.index(s2[0])*20+10)
                    tm.sleep(Settings.settings['delay'])
                    if s == 'A11':
                        print('ä˝ čµ˘äş†ďĽ?ďĽ?ďĽ?')
                        break
            t.up()
        elif m == '22':
            import turtle as t
            t.clear()
            t.speed(0)
            t.seth(0)
            t.shape('classic')
            t.color('black')
            t.up()
            t.goto(0,0)
            if do21:
                t2.clear()
                t2.shape('blank')
            t.goto(-150,-150)
            t.down()
            for i in range(-150,151,15):
                t.goto(i,-150)
                t.lt(90)
                t.fd(300)
                t.bk(300)
                if i != 150:
                    t.up()
                    t.bk(16)
                    t.write(i//15+11,font=('Arial',8))
                    t.fd(16)
                    t.down()
                t.rt(90)
            for i in range(-150,151,15):
                t.goto(-150,i)
                t.fd(300)
                t.bk(300)
                if i != 150:
                    t.up()
                    t.bk(16)
                    t.write(i//15+11,font=('Arial',8))
                    t.fd(16)
                    t.down()
            while True:
                inp = input('''1.ćŠŠä¸€ä¸Şć Ľĺ­?ć¶‚ä¸Šé˘śč‰˛
2.ćŠŠä»Ž x1,y1(ĺ·¦ä¸‹č§’) ĺ?° x2,y2(ĺŹłä¸Šč§’) çš„ć Ľĺ­?ć¶‚ä¸Šé˘śč‰˛
3.é€€ĺ‡şç”»ćťż
4. x1,y1 ĺ?° x2,y2 çš„é‚Łćťˇçşżć¶‚ä¸Šé˘śč‰˛
ĺˇ«ĺşŹĺŹ·ďĽš''')
                if inp == '1':
                    x = int(input('čŻ·čľ“ĺ…Ąć Ľĺ­?çš„ć¨Şĺť?ć ‡ďĽš'))
                    y = int(input('čŻ·čľ“ĺ…Ąć Ľĺ­?çš„çşµĺť?ć ‡ďĽš'))
                    c = bin(int(input('čŻ·čľ“ĺ…Ąé˘śč‰˛(é»‘:0 č“ť:1 ç»ż:2 éť’:3 çş˘:4 ç´«:5 é»„:6 ç™˝:7)ďĽš')))
                    c = c[:2] + (5-len(c))*'0' + c[2:]
                    t.up()
                    t.goto((x-1)*15-150,(y-1)*15-150)
                    t.down()
                    t.fillcolor(int(c[2]),int(c[3]),int(c[4]))
                    t.begin_fill()
                    for k in range(4):
                        t.fd(15)
                        t.lt(90)
                    t.end_fill()
                elif inp == '4':
                    x1 = int(input('čŻ·čľ“ĺ…Ąç¬¬1ä¸Şç‚ąçš„ć¨Şĺť?ć ‡ďĽš'))
                    y1 = int(input('čŻ·čľ“ĺ…Ąç¬¬1ä¸Şç‚ąçš„çşµĺť?ć ‡ďĽš'))
                    x2 = int(input('čŻ·čľ“ĺ…Ąç¬¬2ä¸Şç‚ąçš„ć¨Şĺť?ć ‡ďĽš'))
                    y2 = int(input('čŻ·čľ“ĺ…Ąç¬¬2ä¸Şç‚ąçš„çşµĺť?ć ‡ďĽš'))
                    if x1 > x2:
                        x1,y1,x2,y2=x2,y2,x1,y1
                    c = bin(int(input('čŻ·čľ“ĺ…Ąé˘śč‰˛(é»‘:0 č“ť:1 ç»ż:2 éť’:3 çş˘:4 ç´«:5 é»„:6 ç™˝:7)ďĽš')))
                    c = c[:2] + (5-len(c))*'0' + c[2:]
                    t.fillcolor(int(c[2]),int(c[3]),int(c[4]))
                    for x in range(x1,x2+1):
                        try:
                            y = int(y1+((x-x1)/(x2-x1))*(y2-y1))
                        except ZeroDivisionError:
                            y = y1
                        t.up()
                        t.goto((x-1)*15-150,(y-1)*15-150)
                        t.down()
                        t.begin_fill()
                        for k in range(4):
                            t.fd(15)
                            t.lt(90)
                        t.end_fill()
                    if y1 <= y2:
                        for y in range(y1,y2+1):
                            try:
                                x = int(x1+((y-y1)/(y2-y1))*(x2-x1))
                            except ZeroDivisionError:
                                x = x1
                            t.up()
                            t.goto((x-1)*15-150,(y-1)*15-150)
                            t.down()
                            t.begin_fill()
                            for k in range(4):
                                t.fd(15)
                                t.lt(90)
                            t.end_fill()
                    else:
                        for y in range(y2,y1+1):
                            try:
                                x = int(x1+((y-y2)/(y1-y2))*(x2-x1))
                                x = x2-(x-x1)
                            except ZeroDivisionError:
                                x = x1
                            t.up()
                            t.goto((x-1)*15-150,(y-1)*15-150)
                            t.down()
                            t.begin_fill()
                            for k in range(4):
                                t.fd(15)
                                t.lt(90)
                            t.end_fill()
                elif inp == '2':
                    x1 = int(input('čŻ·čľ“ĺ…Ąĺ·¦ä¸‹č§’çš„ć¨Şĺť?ć ‡ďĽš'))
                    y1 = int(input('čŻ·čľ“ĺ…Ąĺ·¦ä¸‹č§’çš„çşµĺť?ć ‡ďĽš'))
                    x2 = int(input('čŻ·čľ“ĺ…ĄĺŹłä¸Šč§’çš„ć¨Şĺť?ć ‡ďĽš'))
                    y2 = int(input('čŻ·čľ“ĺ…ĄĺŹłä¸Šč§’çš„çşµĺť?ć ‡ďĽš'))
                    c = bin(int(input('čŻ·čľ“ĺ…Ąé˘śč‰˛(é»‘:0 č“ť:1 ç»ż:2 éť’:3 çş˘:4 ç´«:5 é»„:6 ç™˝:7)ďĽš')))
                    c = c[:2] + (5-len(c))*'0' + c[2:]
                    t.fillcolor(int(c[2]),int(c[3]),int(c[4]))
                    for x in range(x1,x2+1):
                        for y in range(y1,y2+1):
                            t.up()
                            t.goto((x-1)*15-150,(y-1)*15-150)
                            t.down()
                            t.begin_fill()
                            for k in range(4):
                                t.fd(15)
                                t.lt(90)
                            t.end_fill()
                elif inp == '3':
                    break
                else:
                    print('čľ“ĺ…Ąć— ć•?')
                for i in range(5):
                    print()
        elif m == '23':
            if crossplatform.nowin:
                print('ĺŁ°éźłĺŠźč?˝ĺś¨éťžWindowsçł»ç»źä¸Šä¸ŤĺŹŻç”¨ă€‚')
                tm.sleep(Settings.settings['delay'])
                continue
            print("é”®ç›?ä¸Šq-u,z-kĺ?†ĺ?«ĺŻąĺş”ä˝Žéźł1ĺ?°é«?éźł1,é”®ç›?ä¸Šçš„2,3,5,6,7,s,d,g,h,jĺ?†ĺ?«ĺŻąĺş”ä˝Žéźł1ĺ?°é«?éźł1é—´çš„ć‰€ćś‰ĺŤ‡é™Ťéźł,ç©şć Ľä»Łčˇ¨ç©şć‹Ť")
            a = ['q','2','w','3','e','random','5','t','6','y','7','u','z','s','x','d','c','v','g','b','h','n','j','m','k']
            s = input()
            for j in s:
                if j != ' ':
                    x = int(245*2**(a.index(j)/12))
                    print(j)
                    crossplatform.winsound.Beep(x,200)
                    for i in range(4000000):
                        pppp=1
                else:
                    for i in range(6000000):
                        pppp=1
        elif m == '24':
            import turtle as t
            if do21:
                t2.clear()
                t2.shape('blank')
            do21 = 1
            t.clear()
            t.color('black')
            t.up()
            t.goto(0,0)
            t.down()
            t.seth(0)
            t.speed(0)
            t.shape('square')
            t2 = t.Turtle()
            t2.up()
            t2.shape('square')
            t2.goto(150,150)
            t2.stamp()
            t2.goto(50,50)
            lsa = ['K','J','I','H','G','F','E','D','C','B','A','']
            lsb = ['01','02','03','04','05','06','07','08','09','10','11','12','13','']
            keypoint = ['G02','J08','E05','H09','D07','F10','B11','C12','A13']
            for i in range(12):
                t.fd(260)
                t.bk(260)
                t.up()
                t.rt(180)
                t.fd(20)
                t.write(lsa[i],font=('Arial',16))
                t.bk(20)
                t.lt(180)
                t.down()
                if i != 11:
                    t.lt(90)
                    t.fd(20)
                    t.rt(90)
            t.up()
            t.goto(0,0)
            t.down()
            t.lt(90)
            for i in range(14):
                t.fd(220)
                t.bk(220)
                t.up()
                t.rt(180)
                t.fd(20)
                t.write(lsb[i],font=('Arial',9))
                t.bk(20)
                t.lt(180)
                t.down()
                if i != 13:
                    t.rt(90)
                    t.fd(20)
                    t.lt(90)
            print('''č§„ĺ?™ďĽš
ä»ŽK01ĺ‡şĺŹ‘ďĽŚç»?ç‚ąć?ŻA13ďĽŚćŻŹć¬ˇć“Ťä˝śĺŹŻä»Ąĺľ€ä¸Ščµ°ä»»ć„Źć ĽďĽŚĺľ€ĺŹłčµ°ä»»ć„Źć ĽďĽŚć?–ĺľ€ĺŹłä¸Ščµ°ä»»ć„Źć ĽďĽŚä˝ ĺ’Śç”µč„‘č˝®ćµ?čż›čˇŚć“Ťä˝śďĽŚč°?ĺ…?ĺ?°ç»?ç‚ąč°?ĺ°±čµ˘ă€‚''')
            t.up()
            t.goto(10,10)
            t.down()
            s = 'K01'
            x = input('č°?ĺ…?ćťĄďĽ?ç”µč„‘ĺ…?ćťĄčľ“ĺ…Ą1ďĽŚä˝ ĺ…?ćťĄčľ“ĺ…Ą2ďĽ‰ďĽź')
            if x == '2':
                while s != 'A13':
                    t.color('blue')
                    s2 = input('ä˝ ć?łčµ°ĺ?°ĺ“Şé‡ŚďĽź')
                    while not ok2(s,s2):
                        s2 = input('čµ°ä¸Ťĺ?°ďĽŚčŻ·é‡Ťć–°čľ“ĺ…ĄďĽš')
                    s = s2
                    t.goto(lsb.index(s2[1:])*20+10,lsa.index(s2[0])*20+10)
                    tm.sleep(Settings.settings['delay'])
                    for i in keypoint:
                        if ok2(s,i):
                            t.color('red')
                            print('ç”µč„‘ĺ†łĺ®ščµ°ĺ?°',i)
                            s = i
                            t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
                print('ç”µč„‘čµ˘äş†ďĽ?ďĽ?ďĽ?')
            else:
                while True:
                    t.color('red')
                    m = 1
                    for i in keypoint:
                        if ok2(s,i):
                            print('ç”µč„‘ĺ†łĺ®ščµ°ĺ?°',i)
                            m = 0
                            s = i
                            t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
                    if m:
                        cc = random.randint(1,4)
                        if cc == 1 and ok2(s,chr(ord(s[0])-1)+s[1:]):
                            print('ç”µč„‘ĺ†łĺ®ščµ°ĺ?°',chr(ord(s[0])-1)+s[1:])
                            s = chr(ord(s[0])-1)+s[1:]
                            t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
                        elif cc == 2 and ok2(s,s[0]+((int(s[1:])+1)<10)*'0'+str(int(s[1:])+1)):
                            s = s[0]+((int(s[1:])+1)<10)*'0'+str(int(s[1:])+1)
                            print('ç”µč„‘ĺ†łĺ®ščµ°ĺ?°',s)
                            t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
                        else:
                            s = chr(ord(s[0])-1)+((int(s[1:])+1)<10)*'0'+str(int(s[1:])+1)
                            print('ç”µč„‘ĺ†łĺ®ščµ°ĺ?°',s)
                            t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
                    if s == 'A13':
                        print('ç”µč„‘čµ˘äş†ďĽ?ďĽ?ďĽ?')
                        break
                    t.color('blue')
                    s2 = input('ä˝ ć?łčµ°ĺ?°ĺ“Şé‡ŚďĽź')
                    while not ok2(s,s2):
                        s2 = input('čµ°ä¸Ťĺ?°ďĽŚčŻ·é‡Ťć–°čľ“ĺ…ĄďĽš')
                    s = s2
                    t.goto(lsb.index(s2[1:])*20+10,lsa.index(s2[0])*20+10)
                    tm.sleep(Settings.settings['delay'])
                    if s == 'A13':
                        print('ä˝ čµ˘äş†ďĽ?ďĽ?ďĽ?')
                        break
            t.up()
        elif m == '25':
            a = input('ć›´ć”ą(1)čż?ć?ŻćźĄçś‹(2)čż?ć?Żäżťĺ­?ä¸şć–‡ä»¶(3)ďĽź')
            if '1' in a:
                ss = input('čŻ·čľ“ĺ…Ąć•°ćŤ®:')
                print('ĺ·˛äżťĺ­?')
            elif '2' in a:
                print(ss)
            else:
                fn = input('ć–‡ä»¶ĺ?Ť?')+'.'+input('ĺ?ŽçĽ€ĺ?Ť(ĺ¦‚txt)?')
                open(fn,'a').write(ss)
        elif m == '26':
            print('ç”µč„‘ĺ°†éšŹćśşç”źć??ä¸€ä¸Şnä˝Ťć•°ďĽŚä˝ ćŻŹć¬ˇçŚśä¸€ä¸Şnä˝Ťć•°ă€‚ç”µč„‘äĽšĺ‘ŠčŻ‰ä˝ ĺŻąäş†ĺ‡ ä¸Şć•°ĺ­—ă€‚')
            n = int(input('nć?Żĺ‡ ďĽź'))
            x = str(random.randint(10**(n-1),10**n-1))
            a = input('ä˝ çŚść?Żĺ‡ ďĽź')
            while a != x:
                n1 = 0
                n2 = 0
                for i in range(n):
                    n1 += int(a[i] == x[i])
                    n2 += int(a[i] in x and a[i] != x[i])
                print('ä˝Ťç˝®ä¸”ć•°ĺ­—ć­Łçˇ®%dä¸ŞďĽŚä»…ć•°ĺ­—ć­Łçˇ®%dä¸Şă€‚'%(n1,n2))
                a = input('ä˝ çŚść?Żĺ‡ ďĽź')
            print('çŚśĺŻąäş†ďĽ?')
        elif m == '27':
            score = 0
            block = [[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[1,0,0]],[[0,0,0],[1,0,0],[1,0,0]],[[0,0,0],[0,0,0],[1,1,0]],[[1,0,0],[1,0,0],[1,0,0]],[[0,0,0],[0,0,0],[1,1,1]],[[0,0,0],[1,0,0],[1,1,0]],[[0,0,0],[0,1,0],[1,1,0]],[[0,0,0],[1,1,0],[0,1,0]],[[0,0,0],[1,1,0],[1,0,0]]]
            blockcol = [0,1,1,2,1,3,2,2,2,2]
            a = []
            for i in range(20):
                a.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            f = 15
            while f:
                for c in range(1,9):
                    print('.',end='')
                f -= 1
                print()
            while True:
                typ = random.randint(1,9)
                score += blockcol[typ]*2
                print('ć–ąĺť—:')
                for i in range(3):
                    for j in range(3):
                        if block[typ][i][j]:
                            print('#',end='')
                        else:
                            print('.',end='')
                    print()
                col = int(input('ć”ľĺś¨ç¬¬ĺ‡ ĺ?—ďĽź'))
                brk = 1
                place = 15
                while place:
                    for i in range(3):
                        for j in range(3):
                            if a[place-i+2][col+j] and block[typ][i][j]:
                                brk = 0
                                break
                        if brk == 0:
                            break
                    if brk == 0:
                        break
                    place -= 1
                place += 1
                for i in range(3):
                    for j in range(3):
                        if block[typ][i][j]:
                            a[place-i+2][col+j] = block[typ][i][j]
                f = 15
                while f:
                    bl = 1
                    for k in range(1,9):
                        if a[f][k] == 0:
                            bl = 0
                    if bl:
                        score += 12
                        for x in range(f,15):
                            for c in range(1,9):
                                a[x][c] = a[x+1][c]
                        a[15] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    f -= 1
                f = 15
                while f:
                    for c in range(1,9):
                        if a[f][c]:
                            print('#',end='')
                        else:
                            print('.',end='')
                    f -= 1
                    print()
                bl = 0
                for k in range(1,9):
                    if a[15][k] == 1:
                        bl = 1
                if bl:
                    print('ĺ?†ć•°:',score)
                    print('ć¸¸ć?Źç»“ćťź')
                    break
        elif m == '28':
            trm = input('0ä¸şć™®é€šč®ˇć—¶ďĽŚ1ä¸şĺ€’č®ˇć—¶ďĽš')
            if trm == '0':
                print('aä¸şĺĽ€ĺ§‹č®ˇć—¶ďĽŚbä¸şç»“ćťźč®ˇć—¶ďĽŚcä¸şé€€ĺ‡ş')
                tr = 0
                c = input('čŻ·čľ“ĺ…ĄćŚ‡ä»¤:')
                while c != 'c':
                    if c == 'a':
                        tr = tm.time()
                    if c == 'b':
                        print('%.2f s'%(tm.time()-tr))
                    c = input('čŻ·čľ“ĺ…ĄćŚ‡ä»¤:')
            if trm == '1':
                t = int(input('ĺ€’č®ˇć—¶ĺ¤šĺ°‘ç§’?'))
                while t > 0:
                    print(t,'s')
                    t -= 1
                    tm.sleep(Settings.settings['delay'])
        elif m == '29':
            x = input('ç”µč„‘ć?ľç¤şä¸€ä¸Ş"[ĺ›žč˝¦]"ĺ?ŽčŻ·ç«‹ĺŤłćŚ‰ĺ›žč˝¦ďĽŚćś‰5~10sçš„ĺ‡†ĺ¤‡ć—¶é—´ďĽŚçŽ°ĺś¨ćŚ‰ĺ›žč˝¦ĺĽ€ĺ§‹:')
            tm.sleep(random.randint(5,10))
            s = tm.time()
            input('[ĺ›žč˝¦]')
            e = tm.time()
            print('ĺŹŤĺş”é€źĺş¦:%.2f s'%(e-s))
        elif m == '30':
            x = int(input('éšŹćśşä¸‹é™?:'))
            y = int(input('éšŹćśşä¸Šé™?:'))
            print(random.randint(x,y-1)+random.random())
        elif m == '31':
            n = int(input("ĺ¤šĺ°‘ä¸Şć•°ćŤ®?"))
            sum = 0
            for i in range(n):
                sum += int(input('ć•°ćŤ®ďĽš'))
            print("%.2f"%(sum/n))
        elif m == '32':
            ls = []
            f = []
            lei = []
            for i in range(1,18):
                t1 = []
                t2 = []
                for j in range(1,18):
                    t1.append(random.randint(0,3) == 0)
                    t2.append(0)
                ls.append(t1)
                f.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
                lei.append(t2)
            for i in range(1,9):
                for j in range(1,10-i):
                    f[i][j] = 1
                    ls[i][j] = 0
            tot = 0
            for i in range(0,17):
                ls[i][0] = 0
                ls[i][16] = 0
                ls[0][i] = 0
                ls[16][i] = 0
            for i in range(1,16):
                for j in range(1,16):
                    tot += ls[i][j]
                    for x in range(3):
                        for y in range(3):
                            lei[i][j] += ls[i+x-1][j+y-1]
                    if ls[i][j]==1:
                        lei[i][j] = -1
            print('ä¸€ĺ…±%dä¸Şé›·'%(tot))
            while True:
                cnt = 0
                print('  123456789012345')
                for i in range(1,16):
                    print(i%10,end=' ')
                    for j in range(1,16):
                        if f[i][j]:
                            if ls[i][j] == 0:
                                print(lei[i][j],end='')
                            else:
                                print('/',end='')
                            pass
                        else:
                            cnt += 1
                            print('#',end='')
                            pass
                    print()
                if cnt == 0:
                    print('é€šĺ…ł!')
                    break
                typ = input('čŻ·čľ“ĺ…ĄćŚ‡ä»¤ç±»ĺž‹(0=ç‚ąĺĽ€,1=ć ‡č®°ä¸şé›·)')
                x = int(input('çşµĺť?ć ‡'))
                y = int(input('ć¨Şĺť?ć ‡'))
                if typ == '0':
                    if ls[x][y] == 1:
                        print('ä˝ čľ“äş†!')
                        break
                    else:
                        f[x][y] = 1
                else:
                    if ls[x][y] == 0:
                        print('ä˝ čľ“äş†!')
                        break
                    else:
                        f[x][y] = 1
        elif m == '33':
            n = int(input("ć‰“ĺŤ°ĺ¤šĺ°‘čˇŚ"))
            while n<=0:
                n = int(input("ä¸Ťč?˝ĺ°ŹäşŽ1ĺ“¦ďĽ?čŻ·ĺ†Ťć¬ˇčľ“ĺ…Ą"))
            l = []
            for i in range(1,n+1):
                l.append(1)
                if i>2:
                    for j in range(2,i):
                        j=i-j
                        l[j]=l[j]+l[j-1]
                for j in range(i):
                    if j==i-1:
                        print(l[j])
                    else:
                        print(l[j],end=" ")
        elif m == '34':
            winner = [[0,1,-1],[-1,0,1],[1,-1,0]]
            name = ['çźłĺ¤´','ĺ‰Şĺ?€','ĺ¸?']
            turn = int(input('ćťĄĺ‡ ĺ±€?'))
            tw = 0
            for i in range(turn):
                print('ç¬¬%dč˝®'%(i+1))
                p = int(input('ä˝ ĺ‡şä»€äą?(0:çźłĺ¤´ 1:ĺ‰Şĺ?€ 2:ĺ¸?)?'))
                c = random.randint(0,2)
                print('ç”µč„‘ĺ‡ş%s'%(name[c]))
                tw += winner[p][c]
            if tw > 0:
                print('ä˝ čµ˘äş†')
            elif tw == 0:
                print('ĺąłĺ±€')
            else:
                print('ä˝ čľ“äş†')
        elif m == '35':
            map1 = [[0,1,1,0,0,1,0,1],[0,0,0,0,1,0,0,0],[0,1,1,1,0,1,1,1],[0,0,1,0,0,1,0,0],[0,1,0,1,0,1,1,2]]
            map2 = [[0,1,0,0,1,0,1,0],[1,0,1,0,1,0,0,0],[1,1,1,1,1,0,1,0],[1,0,0,0,1,1,0,1],[1,1,1,1,0,0,0,1]]
            le = ['w','a','s','d']
            dx = [-1,0,1,0]
            dy = [0,-1,0,1]
            x,y = 0,0
            mp = 1
            while x != 4 or y != 7:
                for i in range(5):
                    for j in range(8):
                        if x == i and y == j and mp == 1:
                            print('i',end='')
                        elif map1[i][j] == 2:
                            print('#',end='')
                        elif map1[i][j] == 0:
                            print('.',end='')
                        elif map1[i][j] == 1:
                            print('*',end='')
                    print()
                print()
                for i in range(5):
                    for j in range(8):
                        if x == i and y == j and mp == 2:
                            print('i',end='')
                        elif map2[i][j] == 0:
                            print('.',end='')
                        else:
                            print('*',end='')
                    print()
                c = input('wasdç§»ĺŠ¨ä˝Ťç˝®,cĺ?‡ćŤ˘ĺś°ĺ›ľ')
                if c == 'c':
                    mp = 3-mp
                    if mp == 1:
                        if map1[x][y] == 1:
                            mp = 2
                            print('ĺ¤±č´Ą')
                    else:
                        if map2[x][y] == 1:
                            mp = 1
                            print('ĺ¤±č´Ą')
                else:
                    dxn = dx[le.index(c)]
                    dyn = dy[le.index(c)]
                    if mp == 1:
                        if map1[x+dxn][y+dyn] == 1:
                            print('ĺ¤±č´Ą')
                        else:
                            x += dxn
                            y += dyn
                    else:
                        if map2[x+dxn][y+dyn] == 1:
                            print('ĺ¤±č´Ą')
                        else:
                            x += dxn
                            y += dyn
            print('ćŚ‘ć??ć??ĺŠź!')
        elif m == '36':
            s = '''
-----------------------------------
ä˝śč€…:a9754610
ĺ…¶ä»–ĺŹ‚ä¸Žçš„äşş:FisherJohn,lyleli2010ç­‰
-----------------------------------
čż™ä¸Şç¨‹ĺşŹć?Żä˝śč€…ä»Ž2021ĺą´7ćś?ĺĽ€ĺ§‹ĺ†™çš„ďĽŚč·ťç¦»çŽ°ĺś¨ĺ·˛ç»Źćś‰ĺĄ˝ĺ‡ ĺą´äş†ďĽŚ
ć?‘ĺ†™čż™ć®µčŻťçš„ć—¶ĺ€™(2022/1/21 19:49:31)ć?‘ĺ·˛ç»Źĺ’Śä¸Šéť˘çš„é‚Łäş›äşşĺś¨
ć?‘ä»¬çš„ĺ·Ąä˝śĺ®¤(www.luogu.com.cn/team/41105)ĺ??ä˝ś2ĺ¤©ĺ¤šäş†ďĽŚ
ćś€čż‘ć­ŁĺĄ˝ć”ľĺ?‡ďĽŚć­¤ç¨‹ĺşŹĺ­—ć•°çŚ›ć¶¨ďĽŚ2ĺ¤©ĺ°±ä»Ž46.5Kć¶¨ĺ?°äş†53.5KďĽŚ
ĺŤ?ĺ?†çš„ĺż«äą?ĺ•Šä¸Ťć?ŻďĽŚčľ›č‹¦ďĽŚĺ¸Śćś›ä˝ çŽ©ć?‘ä»¬çš„ç¨‹ĺşŹč?˝çŽ©çš„ĺĽ€ĺż?ďĽ?
-----------------------------------'''
            for i in s:
                if i != '\n':
                    print(i,end='')
                else:
                    print()
                    tm.sleep(Settings.settings['delay'])
        elif m == '37':
            s = input('čŻ·čľ“ĺ…Ąç˝‘ĺť€:')
            webbrowser.open(s)
        elif m == '38':
            map1 = [[0,1,0,0,0,0,0,0,0,0,1,0,0,0,0],[0,1,0,1,0,1,1,1,1,0,1,0,1,1,0],[0,1,0,1,0,1,0,0,0,0,1,0,1,0,0],[0,0,0,1,0,1,0,1,1,1,1,0,1,0,1],[1,0,1,1,0,1,0,1,0,0,0,0,1,0,0],[0,0,1,0,0,1,0,0,0,1,1,1,1,1,1],[0,1,1,0,1,1,1,1,1,1,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0,0,1,1,1,0],[0,1,1,1,1,1,1,1,1,1,1,1,0,1,0],[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],[1,1,0,1,1,1,0,1,1,1,0,1,1,1,1],[0,0,0,1,0,0,0,0,0,1,0,0,1,0,0],[0,1,1,1,0,1,0,1,0,0,1,0,0,0,0],[0,0,1,1,0,1,0,1,1,0,0,1,1,1,0],[1,0,0,0,0,0,0,0,1,1,0,0,0,1,2]]
            le = ['w','a','s','d']
            dx = [-1,0,1,0]
            dy = [0,-1,0,1]
            x,y = 0,0
            while x != 14 or y != 14:
                for i in range(15):
                    for j in range(15):
                        if x == i and y == j:
                            print('i',end='')
                        elif abs(x-i)<2 and abs(y-j)<2 and map1[i][j] == 1:
                            print('*',end='')
                        elif abs(x-i)<2 and abs(y-j)<2 and map1[i][j] == 0:
                            print('.',end='')
                        elif abs(x-i)<2 and abs(y-j)<2 and map1[i][j] == 2:
                            print('#',end='')
                        else:
                            print('?',end='')
                    print()
                c = input('wasdç§»ĺŠ¨ä˝Ťç˝®')
                dxn = dx[le.index(c)]
                dyn = dy[le.index(c)]
                if map1[x+dxn][y+dyn] == 1:
                    pass
                else:
                    x += dxn
                    y += dyn
            print('ćŚ‘ć??ć??ĺŠź!')
        elif m == '39':
            x = int(input('ĺ‡ čˇŚďĽź'))
            y = int(input('ĺ‡ ĺ?—ďĽź'))
            n = int(input('ĺ‡ ä¸Şéšśç˘Ťç‰©ďĽź'))
            bc = []
            for i in range(n):
                bc.append(input('éšśç˘Ťç‰©ä˝Ťç˝®(čŻ·ĺˇ«ĺ†™çĽ–ĺŹ·)ďĽź'))
            if bc == ['D06'] and x == 9 and y == 11:
                print('\nčŻ·ä¸Ťč¦?ä˝śĺĽŠ')
                continue
            if (bc == ['D08','I03'] or bc == ['I03','D08']) and x == 11 and y == 13:
                print('\nčŻ·ä¸Ťč¦?ä˝śĺĽŠ')
                continue
            ls = []
            for i in range(x+1):
                t = []
                for j in range(y+1):
                    t.append(0)
                ls.append(t)
            for i in range(x,0,-1):
                for j in range(y,0,-1):
                    le = chr(ord('A')+x-i)
                    nu = '0'*(1-j//10)+str(j)
                    if le+nu in bc:
                        continue
                    u = 1
                    for ti in range(i+1,x+1):
                        let = chr(ord('A')+x-ti)
                        if let+nu in bc:
                            break
                        if ls[ti][j]:
                            u = 0
                    random = 1
                    for tj in range(j+1,y+1):
                        nut = '0'*(1-tj//10)+str(tj)
                        if le+nut in bc:
                            break
                        if ls[i][tj]:
                            random = 0
                    ur = 1
                    for dur in range(1,min(x-i,y-j)+1):
                        let = chr(ord('A')+x-(i+dur))
                        nut = '0'*(1-(j+dur)//10)+str(j+dur)
                        if let+nut in bc:
                            break
                        if ls[i+dur][j+dur]:
                            ur = 0
                    if u and random and ur:
                        ls[i][j] = 1
            for i in range(x,0,-1):
                for j in range(1,y+1):
                    if ls[i][j]:
                        print('# ',end='')
                    else:
                        print('* ',end='')
                print()
            print('ä¸Šéť˘ĺ›ľä¸­#ć?Żĺ…łé”®ç‚ąďĽŚä˝ éś€č¦?ĺ°˝é‡ŹĺŽ»čµ°é‚Łäş›ç‚ąă€‚')
        elif m == '40':
            q = input('ć?Żĺ?¦čŻ»ĺ‰§ć?…?(ä¸ŤčŻ»:0,čŻ»:1):')
            print('\n')
            corr = random.randint(1,16)
            ch = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
            cl = ch[:corr]+ch[corr+1:]
            num = [0]
            while len(ch)>1:
                x = random.randint(1,len(ch)-1)
                num.append(ch[x])
                ch = ch[:x]+ch[x+1:]
            vis = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            s0 = '''
čż™é‡Śä¸€ĺ…±ćś‰16ĺĽ çş¸ç‰ŚďĽŚĺąłĺť‡ĺ?†ć??4
ç»„ďĽŚćŻŹç»„4ĺĽ ďĽŚćŻŹĺĽ ä¸Šé?˝ćś‰ä¸€ä¸ŞéšŹ
ćśşçš„çĽ–ĺŹ·(1~16),čż?ćś‰ä¸€äş›ćŹ?é†’ă€‚
ä˝ ç¬¬ä¸€ć¬ˇĺŹŻä»Ąé€‰ć‹©ç¬¬ĺ‡ ç»„çš„ç¬¬ĺ‡ 
ĺĽ ďĽŚäĽšćś‰ćŹ?é†’ďĽŚč€Śä¸”ä˝ ä¸‹ä¸€ć¬ˇçš„
ç»„ĺ?«ĺ·˛ç»Źč˘«ĺ›şĺ®šä¸şçĽ–ĺŹ·ä¸şçş¸ç‰ŚçĽ–
ĺŹ·č·ź4ĺŹ–ä˝™ç„¶ĺ?Žĺ†ŤĺŠ 1çš„é‚Łä¸€ç»„ă€‚\n'''
            if q == '1':
                s = '''ĺ‰§ć?…:
ä»Šĺ¤©ä¸­ĺŤ?ĺ°Źaĺ??ĺ®ŚéĄ­ďĽŚĺ›žĺ?°ć•™ĺ®¤ďĽŚ
ĺŹ‘çŽ°ä»–çš„ćś‹ĺŹ‹FJĺś¨ä»–çš„ćˇŚĺ­?ä¸Šĺ†™
çť€ä»€äą?ďĽŚĺ°Źaĺ‡‘čż‡ĺŽ»ďĽŚFJĺŻąä»–čŻ´:
"čż™ä¸Şć¸¸ć?Źć?Żé‚Łč°?ç»™ć?‘çš„ă€‚"
"č°?ĺ•ŠďĽź"
"ä»€äą?č?˝ĺ?¸ć”¶ć°´ĺ’Ść— ćśşç›?ďĽź"
"ĺ“¦â™‚ďĽŚç„¶ĺ?Žĺ‘˘"
"ä»–čŻ´ĺ¦‚ćžść?‘ĺ?šä¸Ťĺ‡şćťĄďĽŚä¸‹ĺŤ?ä¸Šć“Ť
ĺ°±...ä˝ ć‡‚çš„"
"ĺ•ŠďĽ?ďĽź"
"ć‰€ä»Ąĺ¸®ć?‘çś‹çś‹ďĽź"
'''
                print(s)
            print(s0)
            rw = int(input('ä»Žç¬¬ĺ‡ ç»„ĺĽ€ĺ§‹(1~4)ďĽź'))
            nownum = 0
            while nownum != corr:
                print()
                print('ç¬¬%dç»„'%(rw))
                for i in range(4):
                    print('ç¬¬%dä¸Ş:'%(i+1),end='')
                    if vis[(rw-1)*4+i+1]:
                        print(num[(rw-1)*4+i+1])
                    else:
                        print('?')
                print()
                c = int(input('ç¬¬ĺ‡ ä¸ŞďĽź'))
                nownum = (rw-1)*4+c
                if nownum == corr:
                    break
                x = cl[random.randint(1,len(cl)-1)]
                print()
                print('-====================-')
                print('çĽ–ĺŹ·:',num[nownum])
                print('ćŹ?é†’: %dç»„%dä¸Şä¸Ťć?Żç­”ćˇ?'%((x-1)//4+1,(x-1)%4+1))
                print('-====================-')
                print()
                rw = num[nownum]%4+1
                vis[nownum] = 1
            print('çŚśĺŻąäş†ďĽ?ďĽ?')
            print('ĺ˝©č›‹\nčŻťčŻ´é‚Łč°?é?‡ĺ?°äş†ä¸€é?“ç”źç‰©é˘?ďĽŚĺ®?ä¸ŤçźĄé?“â?šĺżµä»€äą?ďĽŚçś‹çś‹čż™é?“é˘?ĺ?§ďĽ?')
            print('A.ć ą B.sqrt C.ĺąłć–ąć ą D.ć ąĺ„żč±Ş')
            if input('ä˝ é€‰ä»€äą?ďĽź') == 'D':
                print('ĺ?šĺŻąäş†ďĽŚé‚Łč°?ĺľ?é«?ĺ…´')
            else:
                print('ĺ?šé”™äş†ďĽŚé‚Łč°?ĺ†łĺ®šĺś¨ä¸‹ĺŤ?č·‘ć“Ťć—¶...')
        elif m == '41' and 0:
            print('ć¬˘čżŽćťĄĺ?°rĎ€ă?®ĺ†’é™©ĺ°Źć¸¸ć?ŹďĽ?ä˝ ć?ŻrĎ€ďĽŚä¸€ĺ?Ťĺľ?ć™®é€šçš„ä¸­ĺ­¦ç”źďĽŚ2021ĺą´ä˝ ć‰“ç®—ĺś¨ć ˇĺ†…ćťĄä¸€ĺśşĺ†’é™©ă€‚')
            dates = ['','6ćś?28ć—Ą','6ćś?29ć—Ą','6ćś?30ć—Ą','6ćś?31ć—Ą(ĺż?äş†ćŹ?é†’ä˝ ďĽŚrĎ€ĺŹŻä¸ŤäĽšć•°ć•°)','7ćś?0ć—Ą(çś‹ćťĄrĎ€ĺĄ˝ĺ?Źć˛ˇćś‰ç”źć´»ĺ¸¸čŻ†)','7ćś?1ć—Ą','7ćś?2ć—Ą','7ćś?3ć—Ą','7ćś?4ć—Ą','7ćś?5ć—Ą']
            names = ['č?˝é‡Ź','ĺą»ĺ?¬ă?®ĺŠ›','é‡‘é’±','ć”»ĺ‡»']
            data = [random.randint(60,80),random.randint(50,75),random.randint(100,320),random.randint(60,80)]
            day = 0
            score = 20
            while day < 10:
                day += 1;
                print()
                print('ä»Šĺ¤©ć?Ż'+dates[day]+',ĺŹ?ć?Żć ¸ĺąłçš„ä¸€ĺ¤©ĺ•Š!')
                print('ä˝ çš„ĺ±žć€§')
                for i in range(4):
                    print(names[i],data[i])
                print('ä˝ ć‰“ç®—......?')
                print('1.ĺą»ĺ?¬ 2.ć¬şč´źĺ?Śĺ­¦ 3.ĺ??éĄ­ 4.ćŚ–çźż')
                ch = input('čŻ·é€‰ć‹©: ')
                if ch == '1':
                    print('ä˝ é?‡č§?äş†ä¸€ä˝Ťĺ?Śĺ­¦ďĽŚĺ‡†ĺ¤‡ĺĽ€ĺ§‹ĺą»ĺ?¬...')
                    print('â€”â€”â€”â€” ĺ?żďĽŚä˝ ĺŹ«ć?‘"luogu"!?(ćł¨ďĽšçśźĺ®žäş‹ä»¶ćśŞç»Źć”ąçĽ–)')
                    if data[1] >= random.randint(data[1]-10,87):
                        print('â€”â€”â€”â€” ĺ•ŠďĽŚä¸Ťć?ŻďĽŚčż™ä¸Ş...')
                        print('ä˝ ć??ĺŠźäş†ďĽ?')
                        print('č?˝é‡Ź-3')
                        data[0] -= 3
                        print('ĺą»ĺ?¬ă?®ĺŠ›+5')
                        data[1] += 5
                        score += 2
                    else:
                        print('â€”â€”â€”â€” ĺ?ż!')
                        print('ä˝ č˘«ćŹŤäş†ă€‚')
                        print('č?˝é‡Ź-4')
                        data[0] -= 4
                        print('ĺą»ĺ?¬ă?®ĺŠ›+2')
                        data[1] += 2
                        score -= 2
                elif ch == '2':
                    print('ä˝ çś‹č§?äş†ä¸€ä˝Ťä˝ çš„ä»‡äşşďĽŚĺ‡†ĺ¤‡ĺĽ€ĺ§‹ć¬şč´ź...')
                    print('ä˝ ĺ‡‘äş†čż‡ĺŽ»ďĽŚä¸€ćŠŠć‹‰ä˝Źä»–ďĽŚĺ?‘ä»–č¦?é’±...')
                    if data[3] >= random.randint(data[3]-10,92):
                        print('â€”â€”â€”â€” ĺ•Šĺ•Šĺ•Šĺ•Šĺ•Šĺ•Šĺ•Šĺ•Šĺ•Š')
                        print('ä˝ ć??ĺŠźäş†ďĽ?')
                        print('č?˝é‡Ź-3')
                        data[0] -= 3
                        print('é‡‘é’±+5')
                        data[2] += 5
                        score += 2
                    else:
                        print('â€”â€”â€”â€” ä˝ ĺŹ?tâ™‚mć¬ ćŹŤäş†ć?Żĺ?§!')
                        print('ä˝ č˘«ćŹŤäş†ă€‚')
                        print('č?˝é‡Ź-4')
                        data[0] -= 4
                        print('é‡‘é’±-2')
                        data[2] -= 2
                        score -= 2
                elif ch == '3':
                    print('é‡‘é’±-12')
                    data[2] -= 12
                    print('č?˝é‡Ź+12')
                    data[0] += 12
                else:
                    print('č?˝é‡Ź-12')
                    data[0] -= 12
                    print('é‡‘é’±+12')
                    data[2] += 12
            print('ćś€ç»?ĺ?†:',score)
            print('ç„¶č€Ś...')
            tm.sleep(Settings.settings['delay'])
            print('ä˝ çš„čˇŚä¸şé?­ĺ?°äş†ĺ?Śĺ­¦ä»¬çš„ć‰ąčŻ„ă€?ĺŽŚć?¶...')
            tm.sleep(Settings.settings['delay'])
            print('2022ĺą´5ćś?13ć—Ą...')
            tm.sleep(Settings.settings['delay'])
            print('a97ĺ†™ä¸‹äş†čż™ć®µä»Łç ?...')
            tm.sleep(Settings.settings['delay'])
            print('...')
        elif m == '43':
            Settings.settings = Settings.ask_settings()
            Settings.store_settings()
        elif m == '44':
            score = 0
            ops = ['w','a','s','d']
            inbound = lambda x,y:(x>=0 and x<4 and y>=0 and y<4)
            mp = [\
[0,0,0,0],\
[0,0,0,0],\
[0,0,0,0],\
[0,0,0,0]]
            dx = [-1,0,1,0]
            dy = [0,-1,0,1]
            while True:
                crossplatform.clear()
                ok = 0
                for i in range(4):
                    for j in range(4):
                        if mp[i][j] == 0:
                            ok = 1
                if not ok:
                    print('ć¸¸ć?Źç»“ćťźďĽŚĺľ—ĺ?†:',score)
                    break
                x = random.randint(0,3)
                y = random.randint(0,3)
                while mp[x][y] != 0:
                    x = random.randint(0,3)
                    y = random.randint(0,3)
                mp[x][y] = 2-int(random.randint(0,22)!=0);
                for i in range(4):
                    for j in range(4):
                        print(chr(mp[i][j]+ord('@')),end='')
                    print()
                print()
                op = input('Operation(q 4 quit):')
                if op == 'q':
                    print('ć¸¸ć?Źç»“ćťźďĽŚĺľ—ĺ?†:',score)
                    break
                while op not in ops:
                    op = input('ERROR Please try again:')
                opn = ops.index(op)
                if opn%2:
                    for i in range(4):
                        nowls = [3,2,1,0]
                        if opn/2:
                            nowls = [0,1,2,3]
                        for j in nowls:
                            u,v = i,j;
                            if mp[u][v] == 0:
                                continue
                            while True:
                                u,v = u+dx[opn],v+dy[opn];
                                if not inbound(u,v) or (mp[u][v] != 0 and mp[u][v] != mp[u-dx[opn]][v-dy[opn]]):
                                    break
                                elif mp[u][v] == 0:
                                    mp[u][v] = mp[u-dx[opn]][v-dy[opn]]
                                    mp[u-dx[opn]][v-dy[opn]] = 0
                                else:
                                    mp[u][v] = mp[u][v] + 1
                                    mp[u-dx[opn]][v-dy[opn]] = 0
                                    break
                else:
                    for j in range(4):
                        nowls = [3,2,1,0]
                        if opn/2:
                            nowls = [0,1,2,3]
                        for i in nowls:
                            u,v = i,j;
                            if mp[u][v] == 0:
                                continue
                            while True:
                                u,v = u+dx[opn],v+dy[opn];
                                if not inbound(u,v) or (mp[u][v] != 0 and mp[u][v] != mp[u-dx[opn]][v-dy[opn]]):
                                    break
                                elif mp[u][v] == 0:
                                    mp[u][v] = mp[u-dx[opn]][v-dy[opn]]
                                    mp[u-dx[opn]][v-dy[opn]] = 0
                                else:
                                    mp[u][v] = mp[u][v] + 1
                                    mp[u-dx[opn]][v-dy[opn]] = 0
                                    break
                score += 1
        elif m == '45':
            show(tm)
        elif m == '46':
            print('P O T S')
            a = random.randint(3,12)
            b = a
            while b%a  == 0 or a%b == 0 or gcd(a,b) != 1:
                b = random.randint(3,12)
            a0,b0 = a,b
            a,b = 0,0
            c = a0
            while c == a0 or c == b0 or c == abs(a0-b0):
                c = random.randint(2,max(a0,b0)-1)
            while a != c and b != c:
                print('%d/%d %d/%d --> %d'%(a,a0,b,b0,c))
                op = input('[s]swap,[q]fill,[random]drop,[t]pour,[n]quit:')
                if op == 's':
                    a,b,a0,b0 = b,a,b0,a0;
                if op == 'q':
                    a = a0
                if op == 'random':
                    a = 0
                if op == 't':
                    t = min(a,b0-b)
                    a -= t
                    b += t
                if op == 'n':
                    break
        elif m == '47':
            ls = [\
[\
[0,7,1,2,4,1,0,3,6,5,1,7,6,2,2,0],\
[3,4,5,1,2,1,2,3,7,4,1,0,1,2,5,4],\
[4,1,4,7,6,5,6,7,3,1,5,0,7,6,2,5],\
[4,7,6,3,6,5,1,0,2,3,2,6,5,1,4,2],\
[1,0,1,2,4,3,3,3,5,0,7,2,4,5,4,7],\
[4,6,4,5,3,6,4,2,5,1,6,7,0,6,2,2],\
[6,5,4,0,1,0,2,3,7,5,7,1,1,1,1,1],\
[0,1,2,3,4,5,6,7,7,6,5,4,3,2,1,0],\
[2,3,3,3,1,0,7,7,2,7,2,7,3,4,1,2],\
[1,7,5,0,1,3,0,4,4,5,1,6,1,0,7,6],\
[4,1,4,0,5,2,6,7,3,0,2,1,5,1,6,6],\
[2,5,1,6,6,4,3,1,5,6,1,6,4,6,1,6],\
[0,7,1,1,7,1,0,4,5,1,4,6,1,4,7,1],\
[2,3,6,4,1,5,6,3,1,3,4,5,2,5,6,0],\
[4,0,3,6,6,1,4,1,2,2,6,0,3,2,0,7],\
[7,2,5,5,0,2,1,2,6,1,2,4,2,7,7,5]],\
[\
[2,0,0,0,2,2,0,1,6,4,3,0,5,1,6,1],\
[1,2,6,2,1,6,4,6,0,3,5,1,6,4,3,7],\
[0,0,5,1,4,0,6,6,1,0,5,0,5,5,5,0],\
[0,5,7,1,3,3,2,7,1,4,6,2,0,0,3,2],\
[2,7,1,2,1,7,6,5,6,3,6,3,3,3,7,4],\
[2,0,3,2,4,3,1,7,4,2,6,1,2,0,2,5],\
[0,7,2,7,5,1,6,7,1,2,7,6,2,5,4,5],\
[4,3,4,3,4,2,5,6,7,5,6,5,0,6,1,5],\
[3,5,7,3,1,5,1,3,6,2,7,5,3,3,6,5],\
[4,0,6,6,5,0,2,0,0,0,6,3,3,6,7,1],\
[2,3,7,7,0,2,4,6,7,1,6,1,0,3,6,3],\
[2,4,6,4,2,0,5,1,6,7,6,5,3,3,1,5],\
[5,5,4,3,3,0,6,7,4,7,5,2,6,3,7,3],\
[7,7,6,0,2,1,7,6,5,5,7,3,1,3,6,3],\
[4,0,1,5,7,1,3,4,1,7,3,6,6,4,7,2],\
[6,3,1,5,0,3,1,5,5,3,0,7,1,3,0,0]],\
[\
[6,0,5,6,6,7,6,2,2,2,2,5,6,7,1,6],\
[7,5,5,5,1,5,0,7,2,1,4,5,6,7,3,5],\
[1,1,3,2,4,1,5,4,3,1,0,5,4,5,4,4],\
[2,2,7,5,0,7,1,0,6,4,5,6,0,4,4,3],\
[7,6,6,5,6,4,4,5,4,6,1,1,4,4,1,4],\
[6,7,7,3,7,0,3,2,0,6,2,5,2,0,0,0],\
[2,7,0,6,0,6,4,4,0,6,6,0,5,2,5,4],\
[0,3,3,5,6,4,4,5,7,3,7,4,2,4,7,0],\
[1,5,3,0,4,0,7,5,3,6,3,7,5,6,7,2],\
[0,0,4,6,7,1,6,1,2,6,3,6,5,5,6,1],\
[5,1,5,4,5,2,6,2,2,1,1,0,0,7,2,5],\
[5,1,3,4,7,3,7,0,0,7,1,1,3,4,0,6],\
[2,0,0,7,3,6,3,5,5,2,3,3,6,0,2,1],\
[4,6,6,0,7,1,6,4,0,0,2,3,5,0,5,6],\
[2,1,0,7,0,4,5,1,0,2,3,0,0,2,4,1],\
[3,1,1,4,2,7,5,0,0,5,2,7,4,6,2,7]],\
[\
[4,6,2,3,4,4,1,2,0,1,5,1,0,7,0,6],\
[4,1,3,4,7,1,1,7,4,1,3,1,1,5,1,0],\
[2,6,3,3,5,6,4,7,0,0,2,6,5,6,6,7],\
[0,1,2,2,5,1,2,5,2,0,2,3,4,2,5,7],\
[2,5,4,4,5,4,4,5,1,2,2,1,5,1,4,7],\
[5,6,1,4,6,7,4,7,3,2,2,3,4,3,7,7],\
[7,7,4,2,4,1,5,1,7,0,0,5,5,5,7,5],\
[0,2,0,3,7,7,4,1,0,6,2,4,1,2,0,1],\
[5,6,0,6,6,1,2,3,4,5,4,2,2,4,7,4],\
[2,0,7,0,2,5,4,5,6,5,4,5,0,5,0,6],\
[3,0,5,7,7,5,0,4,5,5,5,1,3,2,3,4],\
[3,3,6,4,4,6,3,1,3,3,1,0,1,5,2,5],\
[4,2,1,7,6,1,7,0,0,6,3,0,4,0,3,1],\
[0,5,6,6,2,1,6,6,1,4,4,3,1,4,0,7],\
[3,5,7,3,1,5,1,3,0,7,6,0,6,3,1,5],\
[4,3,1,5,7,0,0,6,2,2,0,7,0,2,0,6]],\
]
            ls = ls[int(input('čŻ·čľ“ĺ…Ąä˝żç”¨çš„ĺŠ ĺŻ†čˇ¨ (0:Cl 1:R1 2:R2 3:R3) ďĽš'))]
            q = input('ĺŠ ĺŻ†ĺˇ«1ďĽŚč§ŁĺŻ†ĺˇ«2:')
            if q == '1':
                s = input('čŻ·čľ“ĺ…Ą:')
                key = ''
                for i in range(len(s)):
                    key += chr(ord('a')+random.randint(0,15))
                print('ä˝ çš„ĺŻ†ç ?ć?Ż '+key)
                outp = ''
                for i in range(len(s)):
                    outp += fff(ord(s[i])+ls[i%16][ord(key[i])-ord('a')],8)+'8'
                print(fff(int(outp,9),16))
            else:
                s = fff(int(input('čŻ·čľ“ĺ…Ą:'),16),9)
                key = input('ĺŻ†ç ?:')
                now = ''
                cnt = 0
                for i in range(len(s)):
                    if s[i] != '8':
                        now += str(s[i])
                    else:
                        print(chr(int(now,8)-ls[cnt%16][ord(key[cnt])-ord('a')]),end='')
                        cnt += 1
                        now = ''
                print()
        elif m == '48':
            s = input('čŻ·čľ“ĺ…Ąč¦?ä¸‹č˝˝çš„ć–‡ä»¶çš„ć–‡ä»¶ĺŹ·(äľ‹ďĽšuk608ajr)ďĽš')
            s = 'https://www.luogu.com.cn/api/team/downloadFile/'+s
            webbrowser.open(s)
        elif m == '49':
            n = random.randint(1,100)
            ls = [0]
            for i in range(100):
                if abs(n-i-1) <= 10:
                    ls.append(0)
                else:
                    ls.append(int(random.randint(0,2)>0))
            for i in range(100):
                if ls[i+1] == 0:
                    if isprimebad(abs(i+1-n)):
                        ls[i+1] = 2
            step = 0
            print('ćł¨ďĽšč™˝ç„¶a97ĺś¨čż™ä¸Şç¨‹ĺşŹä¸ŠčŠ±äş†ĺľ?ĺ¤§ć—¶é—´ďĽŚčż™ä¸Şç¨‹ĺşŹçš„ć•?ćžśčż?ä¸Ťĺ¤§ç?†ć?łďĽŚćś‰ä¸€äş›ä¸Ťĺ??ç?†çš„ĺś°ć–ąďĽŚć‰€ä»Ąć?‘ä»¬ĺ?Žç»­äĽšç»§ç»­čż›čˇŚć›´ć–°ă€‚')
            print('čż™ć?Żä¸€ä¸ŞçŚść•°ć¸¸ć?Ź(çŚś1~100çš„ä¸€ä¸ŞéšŹćśşć•°)ďĽŚç”µč„‘ćŻŹć¬ˇäĽšć ąćŤ®ä˝ çŚśçš„ć•°ç»™ĺ‡ş3ç§ŤćŹ?é†’â€¦â€¦')
            while True:
                step += 1
                p = int(input('ä˝ çŚśçš„ć•°ďĽš'))
                if p == n:
                    print('çŚśĺŻąäş†ďĽ?')
                    print('ä˝żç”¨ć­Ąć•°ďĽš',step)
                    break
                print('çŚśé”™äş†')
                if ls[p] == 1:
                    print('ç­”ćˇ?ćŻ”ä˝ çŚśçš„ć•°'+int(n>p)*'ĺ¤§'+int(n<p)*'ĺ°Ź')
                elif ls[p] > 1:
                    print('ç­”ćˇ?ä¸Žä˝ çŚśçš„ć•°çš„ĺ·®ć?Żč´¨ć•°')
                else:
                    print('ç­”ćˇ?ä¸Žä˝ çŚśçš„ć•°çš„ĺ·®ä¸Ťć?Żč´¨ć•°ďĽŚĺ®?çš„ćś€ĺ°Źč´¨ĺ› ć•°ć?Ż',badfunction(abs(n-p)))
        elif m == '50':
            print('ć•°ĺ­¦č€?ĺ¸?ç‹‚ĺ–ś')
            for i in range(5):
                a,b = random.randint(1,6),random.randint(1,6)*(int(random.randint(0,1)>1)*2-1)
                c,d = random.randint(1,6),random.randint(1,6)*(int(random.randint(0,1)>1)*2-1)
                q,w,e = a*c,a*d+b*c,b*d
                print('(ax+b)(cx+d) = %dx2 + %dx + %d'%(q,w,e))
                aa,bb,cc,dd = int(input('a?')),int(input('b?')),int(input('c?')),int(input('d?'))
                if aa*cc == q and aa*dd+bb*cc == w and bb*dd == e:
                    print('AC')
                else:
                    print('WA')
                    print('Correct Answer:',a,b,c,d)
        elif m == '51':
            s = Settings.settings[2]
            k = 0
            for i in s:
                k += ord(i)
            k %= 100
            print('ä˝ çš„ĺą¸čż?ć•°ĺ­—ć?ŻďĽš'+'0'*(k<10)+str(k))
        elif m == '52':
            if input('çˇ®č®¤č¦?ćŻ?ç?­(ĺ¦‚ćžśĺťšćŚ?ćŻ?ç?­čŻ·ĺˇ«1)ďĽź') == '1':
                os.remove(__file__)
                break
        elif m == '53':
            s = '''ć„źč°˘ĺ?ŤĺŤ•ďĽš
ä»Łç ?ć”ŻćŚ?: a97 FJ liyi zyc baidu
ĺ›˘é?źć”ŻćŚ?: FJ ybk DL01
ĺążĺ‘Šć”ŻćŚ?: a97 FJ ybk
ç?µć„źć”ŻćŚ?: FJ DL01 wrp
čµ„ćş?ć”ŻćŚ?: baidu MMS* bilibili
*Microsoft Math solver
'''
            print(s)
        elif m == '54':
            print('éŞ—ĺ­?ćťĄĺ–˝~ĺ•Šĺ“?ĺ“?ĺ“?ĺ“?ĺ“?ďĽ?é›ľ')
            webbrowser.open('https://mathsolver.microsoft.com/zh/quiz/15xukb54z?ref=s')
        elif m == '55':
            webbrowser.open('https://cdn.luogu.com.cn/upload/image_hosting/0vdhm9qn.png?x-oss-process=image/resize,m_lfit,h_5100,w_6750')
        elif m == '56':
            last = 0.0
            while True:
                k = 1658814180-tm.time()
                if last != k:
                    last = k
                    print('meatĎ€2ĺ‘¨ĺą´ĺ€’č®ˇć—¶:',1658814180-tm.time(),'ç§’')
        elif m == '57':
            k = int(input('ĺ®šć—¶ĺ¤šĺ°‘ç§’ĺ?ŽĺĽ€ĺ§‹ç‚¸éŞ—ďĽź'))
            print('ĺ€’č®ˇć—¶ä¸­...')
            tm.sleep(k)
            webbrowser.open('https://www.bilibili.com/video/BV1VB4y197c1/')
        elif m == '58':
            while True:
                input('Press enter to get the current meatpi standard time ')
                print()
                now = tm.time()
                cmp = 1595692800.0
                add = now-cmp
                tim = str(int(add/86400*20000))
                ln = len(tim)
                tim = tim[0:ln-5]+':'+tim[ln-5]+':'+tim[ln-4:]
                print()
                print(tim)
        elif m == '59':
            crossplatform.clear()
        elif m == '2293':
            shf = 1
            print('ĺĄ˝ĺ?ŹĺŹ‘ç”źäş†ä¸€äş›äş‹ć?…â€¦â€¦')
        elif m == '114514':
            print('ç¨‹ĺşŹĺŹ‘ç”źäş†ć„Źĺ¤–çš„é”™čŻŻďĽ?')
            tm.sleep(Settings.settings['delay'])
            while True:
                print('ĺ¤Şč‡­äş†ćŠŠç¨‹ĺşŹč‡­ć­»äş†',end='')
        else:
            print('čľ“ĺ…Ąć— ć•?')
        """
        print()
        tm.sleep(Settings.settings['delay'])
        input('čŻ·ćŚ‰ĺ›žč˝¦ç»§ç»­')
        crossplatform.clear()

if __name__=='__main__':
    print(COPYRIGHT)
    print('meatĎ€ 3ĺ‘¨ĺą´ĺ€’č®ˇć—¶:',datetime.datetime.fromtimestamp(1690350180)-datetime.datetime.now())
    
    tm.sleep(Settings.settings['delay'])
    while True:
        try:
           main()
        except Exception:
            traceback.print_exc()
            if not Settings.settings['auto_restart']:
                break
            else:
                tm.sleep(Settings.settings['delay'])
        except BaseException:
            traceback.print_exc()
            break
        crossplatform.clear()
    