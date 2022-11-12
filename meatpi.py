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
	

COPYRIGHT= 'Copyright© 2020-2022 dgncx Org.\nCopyright© 2020-2022 a9754610_team.\nAll Rights Reserved.\n\n'
        
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
    print('此功能正在施工中')
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
    ss = '未设置数据'
    cgmgr.search()
    while True:
        cur=cgbase.root
        while isinstance(cur,cgbase.Node):
            print('本级别功能列表：')
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
            inp=int(input('请选择：'))-1
            if inp==-1:
                print('已启动Meatpi调试控制台')
                print('请使用repllib关闭调试控制台')
                print('请在任何REPL中导入repllib库发送调试信息')
                repl=repllib.ReplServer(globals(),'127.0.0.1',9987)
                try:
                    repl.wait_forever()
                finally:
                    repl.close()
            elif inp<subclasscount:
                cur=cur.childrens[inp]
            elif inp>=subclasscount+len(rawidxmap):	
                print('输入无效')
                tm.sleep(Settings.settings['delay'])
                return
            else:
                cur=getattr(cur.cur,dir(cur.cur)[rawidxmap[inp-subclasscount]])
        
        cur()
            
        
        """        run52 = 0
        print('*^'*36+'*')
        print('<',tm.asctime(tm.localtime(tm.time())),'>')
        print('欢迎使用PSCCO的meatπ ————a97')
        print('meatπ2周年已到！')
        print('''
-> 1.计算类功能
-> 2.工具类功能
-> 3.游戏类功能''')
        if shf == 0:
            print('-> 4.?????????')
        else:
            print('-> 4.豪van的小游戏“推箱子”！！！')
        bm = input('''填正确的序号 如 3：''')
        crossplatform.clear()
        if bm == '1':
            print(r'''---> 01.普通计算器
---> 02.质数判断器,包括以下功能：
---> -> 1.输出一到几以内的质数
---> -> 2.输出从一个数到另一个数的质数
---> -> 3.判断一个数是不是质数
---> 03.等差数列求和
---> 04.化简分数
---> 07.最小公倍数
---> 08.算24
---> 12.最大公因数
---> 13.解二元一次方程
---> 14.解一元二次方程
---> 15.质因数分解
---> 20.计算π
---> 31.计算平均数
---> 33.帕斯卡三角形''')
        if bm == '2':
            print(r'''---> 05.十进制变几进制
---> 06.几进制变十进制
---> 16.生成勾股数
---> 17.加密文本(不安全)
---> 18.解密文本(不安全)
---> 19.画心
---> 22.画板
---> 25.更改或查看数据(可保存为文件)
---> 28.计时器
---> 30.生成随机数
---> 36.作者的话
---> 37.上网
---> 39.坑碟游戏解析
---> 42.已停用
---> 43.修改配置
---> 45.meatπ题解库(已废)
---> 47.真·加密和解密(安全版)
---> 48.下载洛谷文件
---> 52.毁灭吧(顾名思义)
---> 53.感谢名单
---> 55.展示logo
---> 56.meatpi 2周年倒计时(已结束)
---> 58.MSTS
---> 59.清除输出''')
        if bm == '3':
            print(r'''---> 09.计算游戏
---> 10.打字游戏
---> 11.猜数游戏1
---> 21.坑碟游戏经典版
---> 23.音乐大师
---> 24.坑碟游戏升级版
---> 26.猜数游戏2
---> 27.俄罗斯方块
---> 29.测试反应速度
---> 32.扫雷
---> 34.石头剪刀布
---> 35.2层迷宫(体验版,以后会有更多地图)
---> 38.失明迷宫(体验版,以后会有更多地图)
---> 40.FJ的卡牌游戏
---> 41.此功能因特殊原因已上锁
---> 44.2048 [测试阶段]
---> 46.Pots
---> 49.猜数游戏3
---> 50.因式分解小练习
---> 51.计算幸运数字(不是那种用生日算的垃圾程序)
---> 54.数学骗紫
---> 57.定时炸骗''')
        if bm == '4':
            if shf == 0:
                print('---> 2293.请在下方填序号处填‘2293’')  # Colinxu2020记：A97的键盘坏掉了？
            else:
                playhf(tm)
                continue
        m = input('''填正确的序号 如 02：''')
        crossplatform.clear()
        if m == '01':
            print('''特殊运算符号：
%  取余
**  次方  
//  整除
<<  左移
>>  右移
>=  大于等于
<=  小于等于
==  等于
!=  不等于
and  与
or  或
not  非
True  是
False  否
abs()  绝对值''')
            try:
                print('答案是：', eval(input('请输入算式（不带=）：')))
            except ZeroDivisionError:
                print('算式中含有除以0，无法计算')
            except SyntaxError:
                print('无法计算')
        elif m == '02':
            while True:
                inp = input('''1.输出一到几以内的质数
2.输出从一个数到另一个数的质数
3.判断一个数是不是质数
4.退出质数判断器
填1,2,3或4：''')
                bl = True
                if inp == '1':
                    print('运行时间可能比较长，请耐心等待')
                    inp_1 = int(input('你想知道从一到几的质数？ '))
                    while inp_1 < 2:
                        print('不能小于2哦！请重新输入')
                        inp_1 = int(input('你想知道从一到几的质数？ '))
                    ls = []
                    for i in range(inp_1+1):
                        ls.append(1)
                    for inp_el in range(2,inp_1+1):
                        if ls[inp_el]==1:
                            for k in range(inp_el**2,inp_1+1,inp_el):
                                ls[k] = 0
                    print('以下是那段数字里的质数')
                    ls2=[]
                    for i in range(2,inp_1+1):
                        if ls[i] == 1:
                            ls2.append(i)
                    print(ls2)
                    print('有',len(ls2),'个质数')
                elif inp == '2':
                    print('运行时间可能比较长，请耐心等待')
                    ls = []
                    inp_4_1 = int(input('你想从几开始说质数？ '))
                    while inp_4_1 < 2:
                        print('不能小于2,请重新输入')
                        inp_4_1 = int(input('你想从几开始说质数？ '))
                    inp_4_2 = int(input('你想到几结束说质数？ '))
                    while inp_4_2 <= inp_4_1:
                        print(f'必须大于{inp_4_1},请重新输入')
                        inp_4_2 = int(input('你想到几结束说质数？ '))
                    ls = []
                    for i in range(inp_4_2+1):
                        ls.append(1)
                    for inp_el in range(2,inp_4_2+1):
                        if ls[inp_el]==1:
                            for k in range(inp_el**2,inp_4_2+1,inp_el):
                                ls[k] = 0
                    print('以下是那段数字里的质数')
                    ls2=[]
                    for i in range(2,inp_4_2+1):
                        if ls[i] == 1 and i >= inp_4_1:
                            ls2.append(i)
                    print(ls2)
                    print('有',len(ls2),'个质数')
                elif inp == '3':
                    print('运行时间可能比较长，请耐心等待')
                    inp_2 = int(input('你想知道哪个数是不是质数？ '))
                    if inp_2 <= 1:
                        print('不是')
                    for cpr_num in range(2,inp_2):
                        if inp_2 % cpr_num == 0:
                            print('不是')
                            bl = False
                            break
                    if bl :
                        print('是')
                elif inp == '4':
                    break
                else:
                    print('输入无效')
        elif m == '03':
            s = int(input('数列从几开始？ '))
            e = int(input('数列到几结束？ '))
            while e <= s:
                    print(f'必须大于{s},请重新输入')
                    e = int(input('到几结束？ '))
            while True:
                q = input('知道相邻的两个数间隔输入1，知道个数输入2：')
                if q == '1':
                    d = int(input('间隔多少？ '))
                    n = (e-s)/d+1
                elif q == '2':
                    n = int(input('个数是几？ '))
                else:
                    print('输入无效')
                    continue
                print('答案是',(s+e)*n/2)
                break
        elif m == '04':
            a = int(input('分子？ '))
            b = int(input('分母？ '))
            i = 2
            while i < ((a+b)-abs(a-b))/2+1:
                if a % i == 0 and b % i == 0:
                    a,b = a / i,b / i
                else:
                    i += 1
            print('化简后的分数是：',int(a),'/',int(b))
        elif m == '05':
            n = int(input('要转换的数是？ '))
            x = int(input('要转换成多少进制？ '))
            print(fff(n,x))
        elif m == '06':
            q = input('要转换的数是？ ')
            nm = int(input('这个数是多少进制的？ '))
            try:
                print(int(q,nm))
            except ValueError:
                print("数据输入错误")
        elif m == '07':
            a = int(input('第一个数是几？ '))
            b = int(input('第二个数是几？ '))
            print('答案是',math.lcm(a,b))
        elif m == '08':
            ls=[]
            allres = []
            allres2 = []
            ls.append(int(input('第1个数:')))
            ls.append(int(input('第2个数:')))
            ls.append(int(input('第3个数:')))
            ls.append(int(input('第4个数:')))
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
                print('无法算出24！')
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
                print('第%i道题：%i + %i = '%(n,a,b),end='')
                re_i = int(input(''))
                end = tm.time()
                ttime += end - start
                if re_i == a+b:
                    print('答对了！')
                    ri += 1
                else:
                    print('答错了。。。')
            print('平均时间：%.2f 秒'%(ttime/q))
            print('正确率：',ri/q*100,'%')
            print('分数：%.2f（超过100就算厉害的啦）'%(ri/q*100/(ttime/q/2.8)))
        elif m == '10':
            ttime,tlen = 0,0
            ri = 0
            q = int(input('一共要多少道题？'))
            for cd in [3,2,1]:
                print(cd)
                tm.sleep(Settings.settings['delay'])
            for n in range(1,q+1):
                kwc = random.choice(keyword.kwlist)
                print(kwc,end=' 请打出相同的单词:')
                start = tm.time()
                kwcin = input()
                end = tm.time()
                ttime,tlen = ttime+(end-start),tlen+len(kwc)
                if kwcin == kwc:
                    ri += 1
            print('打出一个字母用的平均时间：%.2f 秒'%(ttime/tlen))
            print('正确率：',ri/q*100,'%')
            print('T值：%d (作者亲测227)'%(int(tlen/ttime*ri/q*100)))
        elif m == '11':
            print('因为Colinxu2020实在搞不懂A97_QWQ是怎么让下面的n被声明为List类型的，故而Colinxu2020只得假设会出现错误，把本功能放入维护功能中')
            while input('了解？(Y/N)')=='N':
                pass
            raise RuntimeError('维护中...')
            n2 = int(input("你要选一个从0到n的数，让电脑猜你选的是哪个数，请输入n:"))
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
            input(f'请选一个从0到{b1}的数，记在心里，想好了按回车')
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
                print('这个数在',tda2,'里吗？(否:0,是:1)')
                inp.append(int(input()))
            it = 0
            for i in range(l):
                it += (2**i)*inp[i]
            print('你选的数是',it)
        elif m == '12':
            a = int(input('第一个数是几？ '))
            b = int(input('第二个数是几？ '))
            for i in range(1,min(a,b)+1)[::-1]:
                if a%i == 0 and b%i == 0:
                    print('答案是',i)
                    break
        elif m == '13':
            ls = []
            print('''二元一次方程标准形式：
ax + by + c = 0
dx + ey + f = 0''')
            for i in ['a','b','c','d','e','f']:
                ls.append(int(input(('请输入'+i+':'))))
            a,b,c,d,e,f = ls[0],ls[1],ls[2],ls[3],ls[4],ls[5]
            print('x =',(c*e-b*f)/(b*d-a*e))
            print('y =',(c*d-a*f)/(a*e-b*d))
        elif m == '14':
            print('''一元二次方程标准形式：
ax² + bx + c = 0''')
            a = int(input('请输入a：'))
            b = int(input('请输入b：'))
            c = int(input('请输入c：'))
            if (0-(c/a)) >= 0:
                if b/2/a >= 0:
                    print('x =',(b*b-4*a*c)/(4*a*a),'的平方根 -',b/2/a,'(',((b*b-4*a*c)/(4*a*a))**0.5-b/2/a,'或',0-((b*b-4*a*c)/(4*a*a))**0.5-b/2/a,')')
                else:
                    print('x =',(b*b-4*a*c)/(4*a*a),'的平方根 +',0- (b/2/a),'(',(b*b-4*a*c)/(4*a*a)**0.5-b/2/a,'或',0-((b*b-4*a*c)/(4*a*a))**0.5-b/2/a,')')
            else:
                print('无实数解'+chr(10006))
        elif m == '15':
            n = int(input('请输入想分解的数：'))
            if n < 1:
                print('无法分解')
            else:
                ls = []
                x = 2
                while n != 1:
                    while n % x == 0:
                        n /= x
                        ls.append(x)
                    x += 1
                print('分解后的列表',ls)
        elif m == '16':
            a = int(input('请输入参数：'))
            x = a*2-1
            y = (x*x-1)/2
            z = y + 1
            print('结果：',x,y,z)
        elif m == '17':
            x = input('输入要加密文本:')
            key = input('输入加密密码(六位整数):')
            s = ''
            for y in range(len(x)):
                res = ord(x[y])
                s += bin(res*(int(key[:3])+1)+int(key[3:]))[2:]+'2'
            n = int(s,base=3)
            print(n,'\n')
        elif m == '18':
            res = ''
            n = input('输入已加密文本:')
            key = input('输入加密密码(六位整数):')
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
            l = int(input("输入长度（像素）:"))
            d = 145
            print('请耐心等待')
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
            qu = int(input('要计算到小数点后第几位？'))
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
            print('\n数字个数，包括个位的3:')
            for i in range(10):
                print(i,':',ls[i],'个')
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
            print('''规则：
从I01出发，终点是A11，每次操作可以往上走任意格，往右走任意格，或往右上走任意格，你和电脑轮流进行操作，谁先到终点谁就赢。''')
            t.up()
            t.goto(10,10)
            t.down()
            s = 'I01'
            x = input('谁先来（电脑先来输入1，你先来输入2）？')
            if x == '2':
                while s != 'A11':
                    t.color('blue')
                    s2 = input('你想走到哪里？')
                    while not ok(s,s2):
                        s2 = input('走不到，请重新输入：')
                    s = s2
                    t.goto(lsb.index(s2[1:])*20+10,lsa.index(s2[0])*20+10)
                    tm.sleep(Settings.settings['delay'])
                    for i in keypoint:
                        if ok(s,i):
                            t.color('red')
                            print('电脑决定走到',i)
                            s = i
                            t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
                print('电脑赢了！！！')
            else:
                while True:
                    t.color('red')
                    m = 1
                    for i in keypoint:
                        if ok(s,i):
                            print('电脑决定走到',i)
                            m = 0
                            s = i
                            t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
                    if m:
                        cc = random.randint(1,4)
                        if cc == 1 and ok(s,chr(ord(s[0])-1)+s[1:]):
                            print('电脑决定走到',chr(ord(s[0])-1)+s[1:])
                            s = chr(ord(s[0])-1)+s[1:]
                            t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
                        elif cc == 2 and ok(s,s[0]+((int(s[1:])+1)<10)*'0'+str(int(s[1:])+1)):
                            s = s[0]+((int(s[1:])+1)<10)*'0'+str(int(s[1:])+1)
                            print('电脑决定走到',s)
                            t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
                        else:
                            s = chr(ord(s[0])-1)+((int(s[1:])+1)<10)*'0'+str(int(s[1:])+1)
                            print('电脑决定走到',s)
                            t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
                    if s == 'A11':
                        print('电脑赢了！！！')
                        break
                    t.color('blue')
                    s2 = input('你想走到哪里？')
                    while not ok(s,s2):
                        s2 = input('走不到，请重新输入：')
                    s = s2
                    t.goto(lsb.index(s2[1:])*20+10,lsa.index(s2[0])*20+10)
                    tm.sleep(Settings.settings['delay'])
                    if s == 'A11':
                        print('你赢了！！！')
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
                inp = input('''1.把一个格子涂上颜色
2.把从 x1,y1(左下角) 到 x2,y2(右上角) 的格子涂上颜色
3.退出画板
4. x1,y1 到 x2,y2 的那条线涂上颜色
填序号：''')
                if inp == '1':
                    x = int(input('请输入格子的横坐标：'))
                    y = int(input('请输入格子的纵坐标：'))
                    c = bin(int(input('请输入颜色(黑:0 蓝:1 绿:2 青:3 红:4 紫:5 黄:6 白:7)：')))
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
                    x1 = int(input('请输入第1个点的横坐标：'))
                    y1 = int(input('请输入第1个点的纵坐标：'))
                    x2 = int(input('请输入第2个点的横坐标：'))
                    y2 = int(input('请输入第2个点的纵坐标：'))
                    if x1 > x2:
                        x1,y1,x2,y2=x2,y2,x1,y1
                    c = bin(int(input('请输入颜色(黑:0 蓝:1 绿:2 青:3 红:4 紫:5 黄:6 白:7)：')))
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
                    x1 = int(input('请输入左下角的横坐标：'))
                    y1 = int(input('请输入左下角的纵坐标：'))
                    x2 = int(input('请输入右上角的横坐标：'))
                    y2 = int(input('请输入右上角的纵坐标：'))
                    c = bin(int(input('请输入颜色(黑:0 蓝:1 绿:2 青:3 红:4 紫:5 黄:6 白:7)：')))
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
                    print('输入无效')
                for i in range(5):
                    print()
        elif m == '23':
            if crossplatform.nowin:
                print('声音功能在非Windows系统上不可用。')
                tm.sleep(Settings.settings['delay'])
                continue
            print("键盘上q-u,z-k分别对应低音1到高音1,键盘上的2,3,5,6,7,s,d,g,h,j分别对应低音1到高音1间的所有升降音,空格代表空拍")
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
            print('''规则：
从K01出发，终点是A13，每次操作可以往上走任意格，往右走任意格，或往右上走任意格，你和电脑轮流进行操作，谁先到终点谁就赢。''')
            t.up()
            t.goto(10,10)
            t.down()
            s = 'K01'
            x = input('谁先来（电脑先来输入1，你先来输入2）？')
            if x == '2':
                while s != 'A13':
                    t.color('blue')
                    s2 = input('你想走到哪里？')
                    while not ok2(s,s2):
                        s2 = input('走不到，请重新输入：')
                    s = s2
                    t.goto(lsb.index(s2[1:])*20+10,lsa.index(s2[0])*20+10)
                    tm.sleep(Settings.settings['delay'])
                    for i in keypoint:
                        if ok2(s,i):
                            t.color('red')
                            print('电脑决定走到',i)
                            s = i
                            t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
                print('电脑赢了！！！')
            else:
                while True:
                    t.color('red')
                    m = 1
                    for i in keypoint:
                        if ok2(s,i):
                            print('电脑决定走到',i)
                            m = 0
                            s = i
                            t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
                    if m:
                        cc = random.randint(1,4)
                        if cc == 1 and ok2(s,chr(ord(s[0])-1)+s[1:]):
                            print('电脑决定走到',chr(ord(s[0])-1)+s[1:])
                            s = chr(ord(s[0])-1)+s[1:]
                            t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
                        elif cc == 2 and ok2(s,s[0]+((int(s[1:])+1)<10)*'0'+str(int(s[1:])+1)):
                            s = s[0]+((int(s[1:])+1)<10)*'0'+str(int(s[1:])+1)
                            print('电脑决定走到',s)
                            t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
                        else:
                            s = chr(ord(s[0])-1)+((int(s[1:])+1)<10)*'0'+str(int(s[1:])+1)
                            print('电脑决定走到',s)
                            t.goto(lsb.index(s[1:])*20+10,lsa.index(s[0])*20+10)
                    if s == 'A13':
                        print('电脑赢了！！！')
                        break
                    t.color('blue')
                    s2 = input('你想走到哪里？')
                    while not ok2(s,s2):
                        s2 = input('走不到，请重新输入：')
                    s = s2
                    t.goto(lsb.index(s2[1:])*20+10,lsa.index(s2[0])*20+10)
                    tm.sleep(Settings.settings['delay'])
                    if s == 'A13':
                        print('你赢了！！！')
                        break
            t.up()
        elif m == '25':
            a = input('更改(1)还是查看(2)还是保存为文件(3)？')
            if '1' in a:
                ss = input('请输入数据:')
                print('已保存')
            elif '2' in a:
                print(ss)
            else:
                fn = input('文件名?')+'.'+input('后缀名(如txt)?')
                open(fn,'a').write(ss)
        elif m == '26':
            print('电脑将随机生成一个n位数，你每次猜一个n位数。电脑会告诉你对了几个数字。')
            n = int(input('n是几？'))
            x = str(random.randint(10**(n-1),10**n-1))
            a = input('你猜是几？')
            while a != x:
                n1 = 0
                n2 = 0
                for i in range(n):
                    n1 += int(a[i] == x[i])
                    n2 += int(a[i] in x and a[i] != x[i])
                print('位置且数字正确%d个，仅数字正确%d个。'%(n1,n2))
                a = input('你猜是几？')
            print('猜对了！')
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
                print('方块:')
                for i in range(3):
                    for j in range(3):
                        if block[typ][i][j]:
                            print('#',end='')
                        else:
                            print('.',end='')
                    print()
                col = int(input('放在第几列？'))
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
                    print('分数:',score)
                    print('游戏结束')
                    break
        elif m == '28':
            trm = input('0为普通计时，1为倒计时：')
            if trm == '0':
                print('a为开始计时，b为结束计时，c为退出')
                tr = 0
                c = input('请输入指令:')
                while c != 'c':
                    if c == 'a':
                        tr = tm.time()
                    if c == 'b':
                        print('%.2f s'%(tm.time()-tr))
                    c = input('请输入指令:')
            if trm == '1':
                t = int(input('倒计时多少秒?'))
                while t > 0:
                    print(t,'s')
                    t -= 1
                    tm.sleep(Settings.settings['delay'])
        elif m == '29':
            x = input('电脑显示一个"[回车]"后请立即按回车，有5~10s的准备时间，现在按回车开始:')
            tm.sleep(random.randint(5,10))
            s = tm.time()
            input('[回车]')
            e = tm.time()
            print('反应速度:%.2f s'%(e-s))
        elif m == '30':
            x = int(input('随机下限:'))
            y = int(input('随机上限:'))
            print(random.randint(x,y-1)+random.random())
        elif m == '31':
            n = int(input("多少个数据?"))
            sum = 0
            for i in range(n):
                sum += int(input('数据：'))
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
            print('一共%d个雷'%(tot))
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
                    print('通关!')
                    break
                typ = input('请输入指令类型(0=点开,1=标记为雷)')
                x = int(input('纵坐标'))
                y = int(input('横坐标'))
                if typ == '0':
                    if ls[x][y] == 1:
                        print('你输了!')
                        break
                    else:
                        f[x][y] = 1
                else:
                    if ls[x][y] == 0:
                        print('你输了!')
                        break
                    else:
                        f[x][y] = 1
        elif m == '33':
            n = int(input("打印多少行"))
            while n<=0:
                n = int(input("不能小于1哦！请再次输入"))
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
            name = ['石头','剪刀','布']
            turn = int(input('来几局?'))
            tw = 0
            for i in range(turn):
                print('第%d轮'%(i+1))
                p = int(input('你出什么(0:石头 1:剪刀 2:布)?'))
                c = random.randint(0,2)
                print('电脑出%s'%(name[c]))
                tw += winner[p][c]
            if tw > 0:
                print('你赢了')
            elif tw == 0:
                print('平局')
            else:
                print('你输了')
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
                c = input('wasd移动位置,c切换地图')
                if c == 'c':
                    mp = 3-mp
                    if mp == 1:
                        if map1[x][y] == 1:
                            mp = 2
                            print('失败')
                    else:
                        if map2[x][y] == 1:
                            mp = 1
                            print('失败')
                else:
                    dxn = dx[le.index(c)]
                    dyn = dy[le.index(c)]
                    if mp == 1:
                        if map1[x+dxn][y+dyn] == 1:
                            print('失败')
                        else:
                            x += dxn
                            y += dyn
                    else:
                        if map2[x+dxn][y+dyn] == 1:
                            print('失败')
                        else:
                            x += dxn
                            y += dyn
            print('挑战成功!')
        elif m == '36':
            s = '''
-----------------------------------
作者:a9754610
其他参与的人:FisherJohn,lyleli2010等
-----------------------------------
这个程序是作者从2021年7月开始写的，距离现在已经有好几年了，
我写这段话的时候(2022/1/21 19:49:31)我已经和上面的那些人在
我们的工作室(www.luogu.com.cn/team/41105)合作2天多了，
最近正好放假，此程序字数猛涨，2天就从46.5K涨到了53.5K，
十分的快乐啊不是，辛苦，希望你玩我们的程序能玩的开心！
-----------------------------------'''
            for i in s:
                if i != '\n':
                    print(i,end='')
                else:
                    print()
                    tm.sleep(Settings.settings['delay'])
        elif m == '37':
            s = input('请输入网址:')
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
                c = input('wasd移动位置')
                dxn = dx[le.index(c)]
                dyn = dy[le.index(c)]
                if map1[x+dxn][y+dyn] == 1:
                    pass
                else:
                    x += dxn
                    y += dyn
            print('挑战成功!')
        elif m == '39':
            x = int(input('几行？'))
            y = int(input('几列？'))
            n = int(input('几个障碍物？'))
            bc = []
            for i in range(n):
                bc.append(input('障碍物位置(请填写编号)？'))
            if bc == ['D06'] and x == 9 and y == 11:
                print('\n请不要作弊')
                continue
            if (bc == ['D08','I03'] or bc == ['I03','D08']) and x == 11 and y == 13:
                print('\n请不要作弊')
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
            print('上面图中#是关键点，你需要尽量去走那些点。')
        elif m == '40':
            q = input('是否读剧情?(不读:0,读:1):')
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
这里一共有16张纸牌，平均分成4
组，每组4张，每张上都有一个随
机的编号(1~16),还有一些提醒。
你第一次可以选择第几组的第几
张，会有提醒，而且你下一次的
组别已经被固定为编号为纸牌编
号跟4取余然后再加1的那一组。\n'''
            if q == '1':
                s = '''剧情:
今天中午小a吃完饭，回到教室，
发现他的朋友FJ在他的桌子上写
着什么，小a凑过去，FJ对他说:
"这个游戏是那谁给我的。"
"谁啊？"
"什么能吸收水和无机盐？"
"哦♂，然后呢"
"他说如果我做不出来，下午上操
就...你懂的"
"啊！？"
"所以帮我看看？"
'''
                print(s)
            print(s0)
            rw = int(input('从第几组开始(1~4)？'))
            nownum = 0
            while nownum != corr:
                print()
                print('第%d组'%(rw))
                for i in range(4):
                    print('第%d个:'%(i+1),end='')
                    if vis[(rw-1)*4+i+1]:
                        print(num[(rw-1)*4+i+1])
                    else:
                        print('?')
                print()
                c = int(input('第几个？'))
                nownum = (rw-1)*4+c
                if nownum == corr:
                    break
                x = cl[random.randint(1,len(cl)-1)]
                print()
                print('-====================-')
                print('编号:',num[nownum])
                print('提醒: %d组%d个不是答案'%((x-1)//4+1,(x-1)%4+1))
                print('-====================-')
                print()
                rw = num[nownum]%4+1
                vis[nownum] = 1
            print('猜对了！！')
            print('彩蛋\n话说那谁遇到了一道生物题，它不知道√念什么，看看这道题吧！')
            print('A.根 B.sqrt C.平方根 D.根儿豪')
            if input('你选什么？') == 'D':
                print('做对了，那谁很高兴')
            else:
                print('做错了，那谁决定在下午跑操时...')
        elif m == '41' and 0:
            print('欢迎来到rπの冒险小游戏！你是rπ，一名很普通的中学生，2021年你打算在校内来一场冒险。')
            dates = ['','6月28日','6月29日','6月30日','6月31日(忘了提醒你，rπ可不会数数)','7月0日(看来rπ好像没有生活常识)','7月1日','7月2日','7月3日','7月4日','7月5日']
            names = ['能量','幻听の力','金钱','攻击']
            data = [random.randint(60,80),random.randint(50,75),random.randint(100,320),random.randint(60,80)]
            day = 0
            score = 20
            while day < 10:
                day += 1;
                print()
                print('今天是'+dates[day]+',又是核平的一天啊!')
                print('你的属性')
                for i in range(4):
                    print(names[i],data[i])
                print('你打算......?')
                print('1.幻听 2.欺负同学 3.吃饭 4.挖矿')
                ch = input('请选择: ')
                if ch == '1':
                    print('你遇见了一位同学，准备开始幻听...')
                    print('———— 嘿，你叫我"luogu"!?(注：真实事件未经改编)')
                    if data[1] >= random.randint(data[1]-10,87):
                        print('———— 啊，不是，这个...')
                        print('你成功了！')
                        print('能量-3')
                        data[0] -= 3
                        print('幻听の力+5')
                        data[1] += 5
                        score += 2
                    else:
                        print('———— 嘿!')
                        print('你被揍了。')
                        print('能量-4')
                        data[0] -= 4
                        print('幻听の力+2')
                        data[1] += 2
                        score -= 2
                elif ch == '2':
                    print('你看见了一位你的仇人，准备开始欺负...')
                    print('你凑了过去，一把拉住他，向他要钱...')
                    if data[3] >= random.randint(data[3]-10,92):
                        print('———— 啊啊啊啊啊啊啊啊啊')
                        print('你成功了！')
                        print('能量-3')
                        data[0] -= 3
                        print('金钱+5')
                        data[2] += 5
                        score += 2
                    else:
                        print('———— 你又t♂m欠揍了是吧!')
                        print('你被揍了。')
                        print('能量-4')
                        data[0] -= 4
                        print('金钱-2')
                        data[2] -= 2
                        score -= 2
                elif ch == '3':
                    print('金钱-12')
                    data[2] -= 12
                    print('能量+12')
                    data[0] += 12
                else:
                    print('能量-12')
                    data[0] -= 12
                    print('金钱+12')
                    data[2] += 12
            print('最终分:',score)
            print('然而...')
            tm.sleep(Settings.settings['delay'])
            print('你的行为遭到了同学们的批评、厌恶...')
            tm.sleep(Settings.settings['delay'])
            print('2022年5月13日...')
            tm.sleep(Settings.settings['delay'])
            print('a97写下了这段代码...')
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
                    print('游戏结束，得分:',score)
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
                    print('游戏结束，得分:',score)
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
            ls = ls[int(input('请输入使用的加密表 (0:Cl 1:R1 2:R2 3:R3) ：'))]
            q = input('加密填1，解密填2:')
            if q == '1':
                s = input('请输入:')
                key = ''
                for i in range(len(s)):
                    key += chr(ord('a')+random.randint(0,15))
                print('你的密码是 '+key)
                outp = ''
                for i in range(len(s)):
                    outp += fff(ord(s[i])+ls[i%16][ord(key[i])-ord('a')],8)+'8'
                print(fff(int(outp,9),16))
            else:
                s = fff(int(input('请输入:'),16),9)
                key = input('密码:')
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
            s = input('请输入要下载的文件的文件号(例：uk608ajr)：')
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
            print('注：虽然a97在这个程序上花了很大时间，这个程序的效果还不大理想，有一些不合理的地方，所以我们后续会继续进行更新。')
            print('这是一个猜数游戏(猜1~100的一个随机数)，电脑每次会根据你猜的数给出3种提醒……')
            while True:
                step += 1
                p = int(input('你猜的数：'))
                if p == n:
                    print('猜对了！')
                    print('使用步数：',step)
                    break
                print('猜错了')
                if ls[p] == 1:
                    print('答案比你猜的数'+int(n>p)*'大'+int(n<p)*'小')
                elif ls[p] > 1:
                    print('答案与你猜的数的差是质数')
                else:
                    print('答案与你猜的数的差不是质数，它的最小质因数是',badfunction(abs(n-p)))
        elif m == '50':
            print('数学老师狂喜')
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
            print('你的幸运数字是：'+'0'*(k<10)+str(k))
        elif m == '52':
            if input('确认要毁灭(如果坚持毁灭请填1)？') == '1':
                os.remove(__file__)
                break
        elif m == '53':
            s = '''感谢名单：
代码支持: a97 FJ liyi zyc baidu
团队支持: FJ ybk DL01
广告支持: a97 FJ ybk
灵感支持: FJ DL01 wrp
资源支持: baidu MMS* bilibili
*Microsoft Math solver
'''
            print(s)
        elif m == '54':
            print('骗子来喽~啊哈哈哈哈哈（雾')
            webbrowser.open('https://mathsolver.microsoft.com/zh/quiz/15xukb54z?ref=s')
        elif m == '55':
            webbrowser.open('https://cdn.luogu.com.cn/upload/image_hosting/0vdhm9qn.png?x-oss-process=image/resize,m_lfit,h_5100,w_6750')
        elif m == '56':
            last = 0.0
            while True:
                k = 1658814180-tm.time()
                if last != k:
                    last = k
                    print('meatπ2周年倒计时:',1658814180-tm.time(),'秒')
        elif m == '57':
            k = int(input('定时多少秒后开始炸骗？'))
            print('倒计时中...')
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
            print('好像发生了一些事情……')
        elif m == '114514':
            print('程序发生了意外的错误！')
            tm.sleep(Settings.settings['delay'])
            while True:
                print('太臭了把程序臭死了',end='')
        else:
            print('输入无效')
        """
        print()
        tm.sleep(Settings.settings['delay'])
        input('请按回车继续')
        crossplatform.clear()

if __name__=='__main__':
    print(COPYRIGHT)
    print('meatπ 3周年倒计时:',datetime.datetime.fromtimestamp(1690350180)-datetime.datetime.now())
    
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
    