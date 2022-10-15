import random
import time
import webbrowser

import categorybase as base
import crossplatform

    
class Games(base.BaseCategory):
    """小游戏"""
    def calc():
        """计算练习"""
        n=int(input("你想练习几轮？"))
        tottime=0
        right_count=0
        for i in range(n):
            a=random.randint(1,100)
            b=random.randint(1,100)
            start_time=time.time()
            user_answer=int(input('答案：'))
            answer=a+b
            tottime+=time.time()-start_time
            if user_answer==answer:
                print("答对了！")
                right_count+=1
            else:
                print("答错了...")
        print("平均时间：",tottime/n)
        print("正确率：",right_count/n*100)
        print("分数：",right_count*280/tottime)
        
    def type_game():
        """打字游戏（维护中）"""
        
    def kengdie_game_classic():
        """坑碟游戏经典版（未重写）"""
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
        
    def sound():
        """音乐大师"""
        if crossplatform.nowin:
            print('声音功能在非Windows系统上不可用。')
            tm.sleep(Settings.settings['delay'])
            return
        print("键盘上q-u,z-k分别对应低音1到高音1,键盘上的2,3,5,6,7,s,d,g,h,j分别对应低音1到高音1间的所有升降音,空格代表空拍")
        a = ['q','2','w','3','e','random','5','t','6','y','7','u','z','s','x','d','c','v','g','b','h','n','j','m','k']
        s = input()
        for j in s:
            if j != ' ':
                x = int(245*2**(a.index(j)/12))
                print(j)
                crossplatform.winsound.Beep(x,200)
            time.sleep(0.1)
    
    def guess_number1():
        """猜数游戏2"""
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
        
    def guess_number2():
        """猜数游戏3"""
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
                x=abs(n-p)
                res=-1
                for i in range(2,x):
                    if x%i == 0:
                        res=i
                        break
                print('答案与你猜的数的差不是质数，它的最小质因数是',result)
    
    def 俄罗斯方块():
        """俄罗斯方块（维护中）"""
    
    def enter_game():
        """测试反应速度"""
        
        input('电脑显示一个"[回车]"后请立即按回车，有5~10s的准备时间，现在按回车开始:')
        time.sleep(random.randint(5,10))
        s = tm.time()
        input('[回车]')
        print('反应速度:',time.time()-s)
                        
    def 扫雷():
        """扫雷（未重写）"""
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
                    
    def stonecutterfabric():
        """石头剪刀布"""
        winner = [[0,1,-1],[-1,0,1],[1,-1,0]]
        name = ['石头','剪刀','布']
        turn = int(input('来几局?'))
        tw = 0
        for i in range(turn):
            print(f'第{i+1}轮')
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
            
    def 双层迷宫():
        """双层迷宫（维护中）"""
    def 失明迷宫():
        """失明迷宫（维护中）"""
    
    def fj_game():
        """FJ的卡牌游戏"""
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
        if q == '1':
                print('''剧情:
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
''')
        print('''
这里一共有16张纸牌，平均分成4
组，每组4张，每张上都有一个随
机的编号(1~16),还有一些提醒。
你第一次可以选择第几组的第几
张，会有提醒，而且你下一次的
组别已经被固定为编号为纸牌编
号跟4取余然后再加1的那一组。\n''')
        rw = int(input('从第几组开始(1~4)？'))
        nownum = 0
        while nownum != corr:
            print()
            print(f'第{rw}组')
            for i in range(4):
                print(f'第{i+1}个:',end='')
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
            print(f'提醒: {(x-1)//4+1}组{(x-1)%4+1}个不是答案')
            print('-====================-')
            print()
            rw = num[nownum]%4+1
            vis[nownum] = 1
        print('猜对了！！')
    
    def game2048():
        """2048小游戏（未重写）"""
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
    
    def pots():
        """P O T S（未重写）"""
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
            op = input('[s]swap,[q]fill,[d]drop,[t]pour,[n]quit:')
            if op == 's':
                a,b,a0,b0 = b,a,b0,a0;
            if op == 'q':
                a = a0
            if op == 'd':
                a = 0
            if op == 't':
                t = min(a,b0-b)
                a -= t
                b += t
            if op == 'n':
                break
                
    def 因式分解():
        """因式分解（未重写）"""
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
                
    def 数学骗子():
        """数学骗子（彩蛋）"""
        webbrowser.open('https://mathsolver.microsoft.com/zh/quiz/15xukb54z?ref=s')
        
    def fj_phone():
        """FJ的手表"""
        modes = []
            
        for i in range(14):
            modes.append(random.randint(0, 3))
        
        def op66(x, y, dopr):
            cor = []
            nums66=[1,1,1,0,1,1,1]
            for i in range(7):
                cor.append(nums66[x][i])
            for i in range(7):
                cor.append(nums66[y][i])
            for i in range(14):
                if modes[i] == 1:
                    cor[i] = 1
                if modes[i] == 2:
                    cor[i] = 0
                if modes[i] == 3:
                    cor[i] = 1 - cor[i]
            ch1 = lambda x: int(cor[x]) * '_' + (1 - int(cor[x])) * ' '
            ch2 = lambda x: int(cor[x]) * '|' + (1 - int(cor[x])) * ' '
            if dopr:
                print(' ' + ch1(0) + '   ' + ch1(7))
                print(ch2(1) + ch1(3) + ch2(2) + ' ' + ch2(8) + ch1(10) + ch2(9))
                print(ch2(4) + ch1(6) + ch2(5) + ' ' + ch2(11) + ch1(13) + ch2(12))
            return cor
            
        for i in [5, 4, 3, 2, 1, 0]:
            for j in [5, 4, 3, 2, 1, 0]:
                crossplatform.clear()
                print(i,j,sep=='')
                time.sleep(1)
        x, y = random.randint(6, 9), random.randint(6, 9)
        clear()
        res = op66(x, y, 1)
        print()
        resi = int(input('What is this number?'))
        xi = resi // 10
        yi = resi % 10
        if res == op66(xi, yi, 0):
            print('correct!')
        else:
            print('wrong... the answer is', x * 10 + y)
    
    