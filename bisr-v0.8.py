import webbrowser
import time as tm
import random as r
import turtle as t
import os
import keyword as kw
import math

A = abs
B = bin
C = chr
E = eval
I = input
K = t.bk
L = len
M = min
N = open
O = ord
P = print
Q = int
R = r.randint
S = str
T = t.fd
U = tm.sleep
W = range
X = max


def clear():
    if Sz.ls[2] == 0:
        return 0
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


s = 'Copyright (c) 2022 Python Source Code Collecting Org.\nAll Rights Reserved.\nCopyright (c) 2022 dgncx(c) Org.\nAll Rights Reserved.\nCopyright (c) 2022 Python Game Designing Org.\nAll Rights Reserved.\n'
P(s)
P('Initializing your data...')


class Dt:
    try:
        nums66, et47, wheel62, hfms, block27, blockcol27, map135, map235, map138 = E(
            open('Meatpi_Data.dat', 'r').read())
    except:
        Dts = '''[[1,1,1,0,1,1,1],[0,0,1,0,0,1,0],[1,0,1,1,1,0,1],[1,0,1,1,0,1,1],[0,1,1,1,0,1,0],[1,1,0,1,0,1,1],[1,1,0,1,1,1,1],[1,0,1,0,0,1,0],[1,1,1,1,1,1,1],[1,1,1,1,0,1,1]],[[[0,7,1,2,4,1,0,3,6,5,1,7,6,2,2,0],[3,4,5,1,2,1,2,3,7,4,1,0,1,2,5,4],[4,1,4,7,6,5,6,7,3,1,5,0,7,6,2,5],[4,7,6,3,6,5,1,0,2,3,2,6,5,1,4,2],[1,0,1,2,4,3,3,3,5,0,7,2,4,5,4,7],[4,6,4,5,3,6,4,2,5,1,6,7,0,6,2,2],[6,5,4,0,1,0,2,3,7,5,7,1,1,1,1,1],[0,1,2,3,4,5,6,7,7,6,5,4,3,2,1,0],[2,3,3,3,1,0,7,7,2,7,2,7,3,4,1,2],[1,7,5,0,1,3,0,4,4,5,1,6,1,0,7,6],[4,1,4,0,5,2,6,7,3,0,2,1,5,1,6,6],[2,5,1,6,6,4,3,1,5,6,1,6,4,6,1,6],[0,7,1,1,7,1,0,4,5,1,4,6,1,4,7,1],[2,3,6,4,1,5,6,3,1,3,4,5,2,5,6,0],[4,0,3,6,6,1,4,1,2,2,6,0,3,2,0,7],[7,2,5,5,0,2,1,2,6,1,2,4,2,7,7,5]]],[[4,9,21,2,8,10,7,26,25,20,11,16,3,17,0,23,22,6,13,18,1,24,12,5,14,19,15],[13,10,3,17,5,1,4,24,0,12,11,6,19,23,22,20,7,26,2,18,25,8,16,9,14,15,21],[20,8,7,21,19,18,3,15,2,24,22,25,23,0,11,6,13,10,12,4,1,5,14,26,16,9,17],[26,3,1,2,10,16,15,19,14,13,6,21,8,4,17,18,25,12,11,9,7,5,0,23,20,24,22],[22,13,18,23,2,8,17,12,1,14,3,20,0,7,5,6,10,24,4,26,16,15,25,21,9,11,19]],[[[1,1,1,1,1,1,1,1,1,1,1],[1,0,1,1,1,0,0,0,0,0,1],[1,0,0,0,1,0,0,1,1,1,1],[1,0,1,0,0,0,0,0,0,0,1],[1,0,1,0,1,0,1,1,0,0,1],[1,0,0,0,0,0,0,0,0,0,1],[1,0,1,1,1,1,1,1,1,0,1],[1,0,0,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1,1,1]],[[1,1,1,1,1,1,1,1,1,1,1],[1,0,1,0,0,0,0,0,0,0,1],[1,0,0,0,1,0,0,0,0,0,1],[1,0,1,0,1,0,1,0,1,0,1],[1,0,1,0,0,0,1,0,1,0,1],[1,0,0,0,0,0,0,0,1,0,1],[1,0,0,0,0,1,0,0,1,0,1],[1,0,1,1,1,1,0,0,0,0,1],[1,1,1,1,1,1,1,1,1,1,1]]],[[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[1,0,0]],[[0,0,0],[1,0,0],[1,0,0]],[[0,0,0],[0,0,0],[1,1,0]],[[1,0,0],[1,0,0],[1,0,0]],[[0,0,0],[0,0,0],[1,1,1]],[[0,0,0],[1,0,0],[1,1,0]],[[0,0,0],[0,1,0],[1,1,0]],[[0,0,0],[1,1,0],[0,1,0]],[[0,0,0],[1,1,0],[1,0,0]]],[0,1,1,2,1,3,2,2,2,2],[[0,1,1,0,0,1,0,1],[0,0,0,0,1,0,0,0],[0,1,1,1,0,1,1,1],[0,0,1,0,0,1,0,0],[0,1,0,1,0,1,1,2]],[[0,1,0,0,1,0,1,0],[1,0,1,0,1,0,0,0],[1,1,1,1,1,0,1,0],[1,0,0,0,1,1,0,1],[1,1,1,1,0,0,0,1]],[[0,1,0,0,0,0,0,0,0,0,1,0,0,0,0],[0,1,0,1,0,1,1,1,1,0,1,0,1,1,0],[0,1,0,1,0,1,0,0,0,0,1,0,1,0,0],[0,0,0,1,0,1,0,1,1,1,1,0,1,0,1],[1,0,1,1,0,1,0,1,0,0,0,0,1,0,0],[0,0,1,0,0,1,0,0,0,1,1,1,1,1,1],[0,1,1,0,1,1,1,1,1,1,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0,0,1,1,1,0],[0,1,1,1,1,1,1,1,1,1,1,1,0,1,0],[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],[1,1,0,1,1,1,0,1,1,1,0,1,1,1,1],[0,0,0,1,0,0,0,0,0,1,0,0,1,0,0],[0,1,1,1,0,1,0,1,0,0,1,0,0,0,0],[0,0,1,1,0,1,0,1,1,0,0,1,1,1,0],[1,0,0,0,0,0,0,0,1,1,0,0,0,1,2]]'''
        nums66, et47, wheel62, hfms, block27, blockcol27, map135, map235, map138 = E(
            Dts)
        open('Meatpi_Data.dat', 'w').write(Dts)


P('Initializing your personal settings...')


class Sz:
    try:
        ls = E(N('Meatpi_Settings.dat', 'r').read())
        P('Reading your personal settings...')
        if L(ls) != 5:
            P('WARNING\nYour settings file is too old to read.\nYour settings will reset automatically.'
              )
            I('Press Enter to continue')
            excepter
    except:
        P('Resetting or creating your settings...')
        ls = [1, 1, 1, 0.6, I('Please input your username (will be saved):')]
        N('Meatpi_Settings.dat', 'w').write(S(ls))
    name = [
        'sound', 're-opening after error', 'clearing output',
        'time gap between runs', 'username'
    ]


nowin = 0
try:
    import winsound
except:
    nowin = 1
    Sz.ls[0] = 0
    N('Meatpi_Settings.dat', 'w').write(S(Sz.ls))
    P('WARNING\nThe "winsound" module is not found in your computer.\nSound has been disabled automatically.'
      )
    I('Press Enter to continue')
P('Defining functions...')


def ok1(now, s):
    if L(s) != 3 or s[0] < 'A' or s[0] > 'I' or Q(s[1:]) < 1 or Q(
            s[1:]) > 11 or s == 'D06':
        return 0
    elif now[0] == s[0] and Q(s[1:]) > Q(
            now[1:]) and not (now[0] == 'D' and Q(s[1:]) > 6 > Q(now[1:])):
        return 1
    elif now[1:] == s[1:] and O(now[0]) > O(
            s[0]) and not (now[1:] == '06' and O(now[0]) > O('D') > O(s[0])):
        return 1
    elif O(now[0]) + Q(now[1:]) == O(s[0]) + Q(s[1:]) and O(now[0]) > O(
            s[0]) and not (O(s[0]) + Q(s[1:]) == O('D') + 6
                           and Q(s[1:]) > 6 > Q(now[1:])):
        return 1
    else:
        return 0


def ok2(now, s):
    if L(s) != 3 or s[0] < 'A' or s[0] > 'K' or Q(s[1:]) < 1 or Q(
            s[1:]) > 13 or s == 'D08' or s == 'I03':
        return 0
    elif now[0] == s[0] and Q(s[1:]) > Q(now[1:]) and not (now[0] == 'D' and Q(
            s[1:]) > 8 > Q(now[1:])) and not (now[0] == 'I'
                                              and Q(s[1:]) > 3 > Q(now[1:])):
        return 1
    elif now[1:] == s[1:] and O(now[0]) > O(s[0]) and not (
            now[1:] == '08' and O(now[0]) > O('D') > O(s[0])) and not (
                now[1:] == '03' and O(now[0]) > O('I') > O(s[0])):
        return 1
    elif O(now[0]) + Q(now[1:]) == O(s[0]) + Q(s[1:]) and O(now[0]) > O(
            s[0]) and not (O(s[0]) + Q(s[1:]) == O('D') + 8
                           and Q(s[1:]) > 8 > Q(now[1:])) and not (
                               O(s[0]) + Q(s[1:]) == O('I') + 3
                               and Q(s[1:]) > 3 > Q(now[1:])):
        return 1
    else:
        return 0


def badfunction(k):
    for i in W(2, k):
        if k % i == 0:
            return i
            break


def isprimebad(k):
    if k == 1:
        return 0
    else:
        res = 1
        for i in W(2, k):
            if k % i == 0:
                res = 0
        return res


def dfs64(vis, mp64, x, y, col, m):
    vis[x][y] = 1
    res = 1
    if m == '64':
        inbound = lambda x, y: (x >= 0 and x < 5 and y >= 0 and y < 5)
    else:
        inbound = lambda x, y: (x >= 0 and x < 8 and y >= 0 and y < 8)
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    for i in range(4):
        vx, vy = x + dx[i], y + dy[i]
        if inbound(vx, vy):
            if mp64[vx][vy] == col and not vis[vx][vy]:
                vis[vx][vy] = 1
                res += dfs64(vis, mp64, vx, vy, col, m)
    return res


def op66(modes, x, y, ds, dopr):
    if ds:
        P(str(x) + str(y) + '\n')
    cor = []
    for i in range(7):
        cor.append(Dt.nums66[x][i])
    for i in range(7):
        cor.append(Dt.nums66[y][i])
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
        P(' ' + ch1(0) + '   ' + ch1(7))
        P(ch2(1) + ch1(3) + ch2(2) + ' ' + ch2(8) + ch1(10) + ch2(9))
        P(ch2(4) + ch1(6) + ch2(5) + ' ' + ch2(11) + ch1(13) + ch2(12))
    return cor


def read(k):
    P()
    P(Sz.name[k])
    if k != 4:
        P('目前状态:', Sz.ls[k])
    else:
        P("目前状态: '" + Sz.ls[k] + "'")
    Sz.ls[k] = E(I('输入新值: '))


def gcd(a, b):
    if a == 1 or b == 1:
        return 1
    elif a == 0 or b == 0:
        return X(a, b)
    else:
        return gcd(b, a % b)


def fff(n, x):
    a = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D',
        'E', 'F'
    ]
    b = []
    while True:
        s = n // x
        y = n % x
        b = b + [y]
        if s == 0:
            break
        n = s
    b.reverse()
    res = ''
    for i in b:
        res += a[i]
    return res


def getord62(c):
    if O('a') <= O(c) and O('z') >= O(c):
        return O(c) - O('a')
    else:
        return 26


def getchr62(x):
    if 0 <= x and 25 >= x:
        return C(O('a') + x)
    else:
        return ' '


def show(tm):
    P('\n此功能正在施工中\n')
    U(0.8)


hfms = Dt.hfms
players = [[5, 6], [1, 1]]
boxes = [[2, 6], [6, 7]]
targs = [[1, 1], [6, 3]]


def playhf(tm):
    ops = ['w', 'a', 's', 'd']
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    P('stages:%d' % (L(hfms)))
    for mp in hfms:
        stage = hfms.index(mp)
        U(1)
        clear()
        U(1)
        player = players[stage]
        box = boxes[stage]
        targ = targs[stage]
        boxfn = 0
        while (not (boxfn) or player != targ):
            clear()
            P("STAGE <%d>" % (stage + 1))
            for i in W(9):
                for j in W(11):
                    s = ''
                    if [i, j] == player:
                        s = 'i'
                    elif not (boxfn) and [i, j] == box:
                        s = '@'
                    elif [i, j] == targ:
                        s = 'O'
                    elif mp[i][j]:
                        s = '#'
                    else:
                        s = '.'
                    P(s, end='')
                P()
            op = I('Operation:')
            while (not (op in ops)):
                op = I('ERROR Please try again:')
            dirx = dx[ops.index(op)]
            diry = dy[ops.index(op)]
            onx = player[0] + dirx
            ony = player[1] + diry
            if boxfn and targ == [onx, ony]:
                player = [onx, ony]
                continue
            if mp[onx][ony]:
                continue
            elif box != [onx, ony]:
                player = [onx, ony]
            elif mp[onx + dirx][ony + diry]:
                continue
            else:
                player = [onx, ony]
                box = [onx + dirx, ony + diry]
            if box == targ:
                boxfn = 1


class Gl:
    shf, do21, ss, run52 = 0, 0, '', 0
    ads=[\
   '''wtlocker.eu.org PSCCO官方推荐的一款实用的聊天网站,登录即可开聊,功能齐全,快来试试吧!''',\
   '''g9mee.csb.app PSCCO官方指定的小程序下载处,有c也有py,快来玩吧!''',\
   '']


P('Initialization finished!')
U(1)
clear()


def runfunc(m):
    clear()
    if m == '01':
        P('''特殊运算符号：
%  取余
**  乘方
//  整除
<<  左移
>>  右移''')
        try:
            q = I('请输入算式（不带=）：')
            q_ev = E(q)
            P('答案是：', q_ev)
        except ZeroDivisionError:
            P('算式中含有除以0，无法计算')
        except:
            P('无法计算')
    elif m == '02':
        while 1:
            inp = I('''1.输出1到x以内的质数
2.输出x到y的质数
3.判断x是不是质数
4.退出
填1,2,3或4：''')
            bl = 1
            if inp == '1':
                inp_1 = E(I('x? '))
                while inp_1 < 2:
                    P('不能小于2哦!请重新输入')
                    inp_1 = E(I('x? '))
                ls = []
                for i in W(inp_1 + 1):
                    ls.append(1)
                for inp_el in W(2, inp_1 + 1):
                    if ls[inp_el] == 1:
                        for k in W(inp_el**2, inp_1 + 1, inp_el):
                            ls[k] = 0
                ls2 = []
                for i in W(2, inp_1 + 1):
                    if ls[i] == 1:
                        ls2.append(i)
                P(ls2)
                P('计数:', L(ls2))
            elif inp == '2':
                ls = []
                inp_4_1 = E(I('x? '))
                while inp_4_1 < 2:
                    P('不能小于2,请重新输入')
                    inp_4_1 = E(I('x? '))
                inp_4_2 = E(I('y? '))
                while inp_4_2 <= inp_4_1:
                    P('必须大于%i,请重新输入' % inp_4_1)
                    inp_4_2 = E(I('y? '))
                ls = []
                for i in W(inp_4_2 + 1):
                    ls.append(1)
                for inp_el in W(2, inp_4_2 + 1):
                    if ls[inp_el] == 1:
                        for k in W(inp_el**2, inp_4_2 + 1, inp_el):
                            ls[k] = 0
                ls2 = []
                for i in W(2, inp_4_2 + 1):
                    if ls[i] == 1 and i >= inp_4_1:
                        ls2.append(i)
                P(ls2)
                P('计数:', L(ls2))
            elif inp == '3':
                inp_2 = E(I('x? '))
                if inp_2 <= 1:
                    P('不是')
                    for i in W(5):
                        P()
                    continue
                for cpr_num in W(2, inp_2):
                    if inp_2 % cpr_num == 0:
                        P('不是')
                        bl = 0
                        break
                if bl:
                    P('是')
            elif inp == '4':
                break
            else:
                P('输入无效')
            for i in W(5):
                P()
    elif m == '03':
        s = E(I('数列首项? '))
        e = E(I('数列末项? '))
        while e <= s:
            P('必须大于%i,请重新输入' % s)
            e = E(I('数列末项? '))
        while 1:
            q = I('输入公差回答1,输入个数回答2：')
            if q == '1':
                d = E(I('公差? '))
                n = (e - s) / d + 1
            elif q == '2':
                n = E(I('个数? '))
            else:
                P('输入无效')
                continue
            P('答案是', (s + e) * n / 2)
            break
    elif m == '04':
        a = E(I('分子? '))
        b = E(I('分母? '))
        i = 2
        while i < ((a + b) - A(a - b)) / 2 + 1:
            if a % i == 0 and b % i == 0:
                a, b = a / i, b / i
            else:
                i += 1
        P('化简后的分数是：', Q(a), '/', Q(b))
    elif m == '05':
        n = Q(I('要转换的数是? '))
        x = Q(I('要转换成多少进制? '))
        P(fff(n, x))
    elif m == '06':
        q = I('要转换的数是? ')
        nm = Q(I('这个数是多少进制的? '))
        try:
            P(Q(q, nm))
        except:
            P("数据输入错误")
    elif m == '07':
        a = E(I('第一个数是几? '))
        b = E(I('第二个数是几? '))
        P('答案是', math.lcm(a, b))
    elif m == '08':
        ls = []
        allres = []
        allres2 = []
        ls.append(Q(I('第1个数:')))
        ls.append(Q(I('第2个数:')))
        ls.append(Q(I('第3个数:')))
        ls.append(Q(I('第4个数:')))
        for i in W(4):
            for j in W(4):
                for k in W(4):
                    for l in W(4):
                        if i != j and i != k and i != l and j != k and j != l and k != l:
                            ls2 = [ls[i], ls[j], ls[k], ls[l]]
                            for m in W(216):
                                res = S(ls2[0])
                                for now in W(1, 4):
                                    nowele = ls2[now]
                                    pol = (m % (6**(now))) // ((6**(now - 1)))
                                    if (pol) == 0:
                                        res += '+' + S(nowele)
                                    if (pol) == 1:
                                        res += '*' + S(nowele)
                                    if (pol) == 2:
                                        res += '-' + S(nowele)
                                    if (pol) == 3:
                                        res = S(nowele) + '-' + res
                                    if (pol) == 4:
                                        res += '/' + S(nowele)
                                    if (pol) == 5:
                                        res = S(nowele) + '/' + res
                                    res = '(' + res + ')'
                                try:
                                    if A(E(res) - 24) <= 0.001:
                                        allres.append(res)
                                except:
                                    pass
                            for m in W(216):
                                res = ''
                                res1 = ''
                                res2 = ''
                                pol1 = (m % (6**1)) // ((6**(0)))
                                pol2 = (m % (6**3)) // ((6**(2)))
                                pol3 = (m % (6**2)) // ((6**(1)))
                                if (pol1) == 0:
                                    res1 = '(' + S(ls[0]) + '+' + S(
                                        ls[1]) + ')'
                                if (pol1) == 1:
                                    res1 = '(' + S(ls[0]) + '*' + S(
                                        ls[1]) + ')'
                                if (pol1) == 2:
                                    res1 = '(' + S(ls[0]) + '-' + S(
                                        ls[1]) + ')'
                                if (pol1) == 3:
                                    res1 = '(' + S(ls[1]) + '-' + S(
                                        ls[0]) + ')'
                                if (pol1) == 4:
                                    res1 = '(' + S(ls[0]) + '/' + S(
                                        ls[1]) + ')'
                                if (pol1) == 5:
                                    res1 = '(' + S(ls[1]) + '/' + S(
                                        ls[0]) + ')'
                                if (pol2) == 0:
                                    res2 = '(' + S(ls[2]) + '+' + S(
                                        ls[3]) + ')'
                                if (pol2) == 1:
                                    res2 = '(' + S(ls[2]) + '*' + S(
                                        ls[3]) + ')'
                                if (pol2) == 2:
                                    res2 = '(' + S(ls[2]) + '-' + S(
                                        ls[3]) + ')'
                                if (pol2) == 3:
                                    res2 = '(' + S(ls[3]) + '-' + S(
                                        ls[2]) + ')'
                                if (pol2) == 4:
                                    res2 = '(' + S(ls[2]) + '/' + S(
                                        ls[3]) + ')'
                                if (pol2) == 5:
                                    res2 = '(' + S(ls[3]) + '/' + S(
                                        ls[2]) + ')'
                                if (pol3) == 0:
                                    res = '(' + res1 + '+' + res2 + ')'
                                if (pol3) == 1:
                                    res = '(' + res1 + '*' + res2 + ')'
                                if (pol3) == 2:
                                    res = '(' + res1 + '-' + res2 + ')'
                                if (pol3) == 3:
                                    res = '(' + res2 + '-' + res1 + ')'
                                if (pol3) == 4:
                                    res = '(' + res1 + '/' + res2 + ')'
                                if (pol3) == 5:
                                    res = '(' + res2 + '/' + res1 + ')'
                                try:
                                    if A(E(res) - 24) <= 0.0001:
                                        allres.append(res)
                                except:
                                    pass
        for res in allres:
            if not (res in allres2):
                allres2.append(res)
                P(res)
        if L(allres) == 0:
            P('无法算出24!')
    elif m == '09':
        ri = 0
        ttime = 0
        q = Q(I('一共要多少道题?'))
        for cd in [3, 2, 1]:
            P(cd)
            U(1)
        for n in W(1, q + 1):
            a = R(1, 100)
            b = R(1, 100)
            start = tm.time()
            P('第%i道题：%i+%i=' % (n, a, b), end='')
            re_i = Q(I(''))
            end = tm.time()
            ttime += end - start
            if re_i == a + b:
                P('答对了!')
                ri += 1
            else:
                P('答错了...')
        P('平均时间：%.2f 秒' % (ttime / q))
        P('正确率：', ri / q * 100, '%')
        P('分数：%.2f（超过100就算厉害的啦）' % (ri / q * 100 / (ttime / q / 2.8)))
    elif m == '10':
        ttime, tlen = 0, 0
        ri = 0
        q = Q(I('一共要多少道题?'))
        for cd in [3, 2, 1]:
            P(cd)
            U(1)
        for n in W(1, q + 1):
            kwc = r.choice(kw.kwlist)
            P(kwc, end=' 请打出相同的单词:')
            start = tm.time()
            kwcin = I()
            end = tm.time()
            ttime, tlen = ttime + (end - start), tlen + L(kwc)
            if kwcin == kwc:
                ri += 1
        P('打出一个字母用的平均时间：%.2f 秒' % (ttime / tlen))
        P('正确率：', ri / q * 100, '%')
        P('T值：%d (作者亲测227)' % (Q(tlen / ttime * ri / q * 100)))
    elif m == '11':
        bl = Q(I("你要选一个从0到n的数，让电脑猜你选的是哪个数，请输入n:"))
        q = S(bl)
        nm = 2
        ql = L(q)
        q = E(q)
        a = ''
        while q != 0:
            w = q % nm
            if w > 10:
                w = l[n.index(w)]
            a += S(w)
            q = Q(q / nm)
        a = a[::-1]
        l = L(a)
        P('请选一个从0到%d的数，记在心里，想好了按回车' % (bl), end='')
        I()
        inp = []
        ls = []
        for i in W(0, 2**l):
            a = B(i)[2:]
            for i in W(l - L(a)):
                a = '0' + a
            ls.append(a)
        for i in W(l):
            tda = []
            for tn in ls:
                if (tn[0 - (i + 1)] == '1'):
                    tda.append(tn)
            tda2 = []
            for tt in tda:
                tt2 = 0
                for j in W(L(tt)):
                    tt2 += (2**j) * Q(tt[0 - (j + 1)])
                if tt2 <= bl:
                    tda2.append(tt2)
            P('这个数在', tda2, '里吗?(否:0,是:1)')
            inp.append(Q(I()))
        it = 0
        for i in W(l):
            it += (2**i) * inp[i]
        P('你选的数是', it)
    elif m == '12':
        a = E(I('第一个数是几? '))
        b = E(I('第二个数是几? '))
        for i in W(1, M(a, b) + 1)[::-1]:
            if a % i == 0 and b % i == 0:
                P('答案是', i)
                break
    elif m == '13':
        ls = []
        P('''二元一次方程标准形式：
ax+by+c=0
dx+ey+f=0''')
        for i in ['a', 'b', 'c', 'd', 'e', 'f']:
            ls.append(E(I(('请输入' + i + ':'))))
        a, b, c, d, e, f = ls[0], ls[1], ls[2], ls[3], ls[4], ls[5]
        P('x =', (c * e - b * f) / (b * d - a * e))
        P('y =', (c * d - a * f) / (a * e - b * d))
    elif m == '14':
        P('''一元二次方程标准形式：
ax²+bx+c=0''')
        a = E(I('请输入a：'))
        b = E(I('请输入b：'))
        c = E(I('请输入c：'))
        if (0 - (c / a)) >= 0:
            if b / 2 / a >= 0:
                P('x =', (b * b - 4 * a * c) / (4 * a * a), '的平方根 -',
                  b / 2 / a, '(',
                  ((b * b - 4 * a * c) / (4 * a * a))**0.5 - b / 2 / a, '或',
                  0 - ((b * b - 4 * a * c) / (4 * a * a))**0.5 - b / 2 / a,
                  ')')
            else:
                P('x =', (b * b - 4 * a * c) / (4 * a * a), '的平方根 +',
                  0 - (b / 2 / a), '(',
                  (b * b - 4 * a * c) / (4 * a * a)**0.5 - b / 2 / a, '或',
                  0 - ((b * b - 4 * a * c) / (4 * a * a))**0.5 - b / 2 / a,
                  ')')
        else:
            P('无实数解' + C(10006))
    elif m == '15':
        n = Q(I('请输入想分解的数：'))
        if n < 1:
            P('无法分解')
        else:
            ls = []
            x = 2
            while n != 1:
                while n % x == 0:
                    n /= x
                    ls.append(x)
                x += 1
            P('分解后的列表', ls)
    elif m == '16':
        a = Q(I('请输入参数：'))
        x = a * 2 - 1
        y = (x * x - 1) / 2
        z = y + 1
        P('结果：', x, y, z)
    elif m == '19':
        import turtle as t
        t.clear()
        cor = []
        t.speed(0)
        t.seth(0)
        t.shape('classic')
        t.color('black')
        t.up()
        t.goto(0, 0)
        if Gl.do21:
            t2.clear()
            t2.shape('blank')
        l = Q(I("输入长度（像素）:"))
        d = 145
        P('请耐心等待')
        t.fillcolor('red')
        t.begin_fill()
        for i in W(145):
            i2 = i + 1
            nowl = i2 * l / 145
            t.home()
            t.lt(125)
            t.lt(i2)
            T(nowl)
            cor.append([t.xcor(), t.ycor()])
            t.goto(0, 0)
        t.down()
        for i in cor[1:]:
            t.goto(i[0], i[1])
        t.up()
        t.home()
        cor = []
        for i in W(145):
            i2 = i + 1
            nowl = i2 * l / 145
            t.home()
            t.lt(55)
            t.rt(i2)
            T(nowl)
            cor.append([t.xcor(), t.ycor()])
            t.goto(0, 0)
        t.down()
        for i in cor[1:]:
            t.goto(i[0], i[1])
        t.end_fill()
    elif m == '20':
        ls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        qu = Q(I('要计算到小数点后第几位?'))
        co, k, a, b, a1, b1 = -1, 2, 4, 1, 12, 4
        while 1:
            p, q, k = k * k, 2 * k + 1, k + 1
            a, b, a1, b1 = a1, b1, p * a + q * a1, p * b + q * b1
            d, d1 = a / b, a1 / b1
            while d == d1:
                if co == -1:
                    P(Q(d), end='.')
                else:
                    P(Q(d), end='')
                ls[Q(d)] += 1
                co, a, a1 = co + 1, 10 * (a % b), 10 * (a1 % b1)
                d, d1 = a / b, a1 / b1
                if co == qu:
                    break
            if co == qu:
                break
        P('\n数字个数，包括个位的3:')
        for i in W(10):
            P(i, ':', ls[i], '个')
    elif m == '21':
        import turtle as t
        if Gl.do21:
            t2.clear()
            t2.shape('blank')
        Gl.do21 = 1
        t.clear()
        t.color('black')
        t.up()
        t.goto(0, 0)
        t.down()
        t.seth(0)
        t.speed(0)
        t.shape('square')
        t2 = t.Turtle()
        t2.up()
        t2.shape('square')
        t2.goto(110, 110)
        lsa = ['I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A', '']
        lsb = [
            '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11',
            ''
        ]
        keypoint = ['E03', 'H07', 'D05', 'F08', 'B09', 'C10', 'A11']
        for i in W(10):
            T(220)
            K(220)
            t.up()
            t.rt(180)
            T(20)
            t.write(lsa[i], font=('Arial', 16))
            K(20)
            t.lt(180)
            t.down()
            if i != 9:
                t.lt(90)
                T(20)
                t.rt(90)
        t.up()
        t.goto(0, 0)
        t.down()
        t.lt(90)
        for i in W(12):
            T(180)
            K(180)
            t.up()
            t.rt(180)
            T(20)
            t.write(lsb[i], font=('Arial', 9))
            K(20)
            t.lt(180)
            t.down()
            if i != 11:
                t.rt(90)
                T(20)
                t.lt(90)
        P('''规则：
从I01出发，终点是A11，每次操作可以往上走任意格，往右走任意格，或往右上走任意格，你和电脑轮流进行操作，谁先到终点谁就赢。''')
        t.up()
        t.goto(10, 10)
        t.down()
        s = 'I01'
        x = I('谁先来（电脑先来输入1，你先来输入2）?')
        if x == '2':
            while s != 'A11':
                t.color('blue')
                s2 = I('你想走到哪里?')
                while (not ok1(s, s2)):
                    s2 = I('走不到，请重新输入：')
                s = s2
                t.goto(lsb.index(s2[1:]) * 20 + 10, lsa.index(s2[0]) * 20 + 10)
                U(0.3)
                for i in keypoint:
                    if ok1(s, i):
                        t.color('red')
                        P('电脑决定走到', i)
                        s = i
                        t.goto(
                            lsb.index(s[1:]) * 20 + 10,
                            lsa.index(s[0]) * 20 + 10)
            P('电脑赢了!!!')
        else:
            while 1:
                t.color('red')
                m = 1
                for i in keypoint:
                    if ok1(s, i):
                        P('电脑决定走到', i)
                        m = 0
                        s = i
                        t.goto(
                            lsb.index(s[1:]) * 20 + 10,
                            lsa.index(s[0]) * 20 + 10)
                if m:
                    cc = R(1, 4)
                    if cc == 1 and ok1(s, C(O(s[0]) - 1) + s[1:]):
                        P('电脑决定走到', C(O(s[0]) - 1) + s[1:])
                        s = C(O(s[0]) - 1) + s[1:]
                        t.goto(
                            lsb.index(s[1:]) * 20 + 10,
                            lsa.index(s[0]) * 20 + 10)
                    elif cc == 2 and ok1(
                            s, s[0] +
                        ((Q(s[1:]) + 1) < 10) * '0' + S(Q(s[1:]) + 1)):
                        s = s[0] + (
                            (Q(s[1:]) + 1) < 10) * '0' + S(Q(s[1:]) + 1)
                        P('电脑决定走到', s)
                        t.goto(
                            lsb.index(s[1:]) * 20 + 10,
                            lsa.index(s[0]) * 20 + 10)
                    else:
                        s = C(O(s[0]) - 1) + (
                            (Q(s[1:]) + 1) < 10) * '0' + S(Q(s[1:]) + 1)
                        P('电脑决定走到', s)
                        t.goto(
                            lsb.index(s[1:]) * 20 + 10,
                            lsa.index(s[0]) * 20 + 10)
                if s == 'A11':
                    P('电脑赢了!!!')
                    break
                t.color('blue')
                s2 = I('你想走到哪里?')
                while (not ok1(s, s2)):
                    s2 = I('走不到，请重新输入：')
                s = s2
                t.goto(lsb.index(s2[1:]) * 20 + 10, lsa.index(s2[0]) * 20 + 10)
                U(0.3)
                if s == 'A11':
                    P('你赢了!!!')
                    break
        t.up()
    elif m == '22':
        t.clear()
        t.speed(0)
        t.seth(0)
        t.shape('classic')
        t.color('black')
        t.up()
        t.goto(0, 0)
        if Gl.do21:
            t2.clear()
            t2.shape('blank')
        t.goto(-150, -150)
        t.down()
        for i in W(-150, 151, 15):
            t.goto(i, -150)
            t.lt(90)
            T(300)
            K(300)
            if i != 150:
                t.up()
                K(16)
                t.write(i // 15 + 11, font=('Arial', 8))
                T(16)
                t.down()
            t.rt(90)
        for i in W(-150, 151, 15):
            t.goto(-150, i)
            T(300)
            K(300)
            if i != 150:
                t.up()
                K(16)
                t.write(i // 15 + 11, font=('Arial', 8))
                T(16)
                t.down()
        while 1:
            inp = I('''1.把一个格子涂上颜色
2.把从 x1,y1(左下角) 到 x2,y2(右上角) 的格子涂上颜色
3.退出
4.x1,y1 到 x2,y2 的那条线涂上颜色
填序号：''')
            if inp == '1':
                x = Q(I('请输入格子的横坐标：'))
                y = Q(I('请输入格子的纵坐标：'))
                c = B(Q(I('请输入颜色(黑:0 蓝:1 绿:2 青:3 红:4 紫:5 黄:6 白:7)：')))
                c = c[:2] + (5 - L(c)) * '0' + c[2:]
                t.up()
                t.goto((x - 1) * 15 - 150, (y - 1) * 15 - 150)
                t.down()
                t.fillcolor(Q(c[2]), Q(c[3]), Q(c[4]))
                t.begin_fill()
                for k in W(4):
                    T(15)
                    t.lt(90)
                t.end_fill()
            elif inp == '4':
                x1 = Q(I('请输入第1个点的横坐标：'))
                y1 = Q(I('请输入第1个点的纵坐标：'))
                x2 = Q(I('请输入第2个点的横坐标：'))
                y2 = Q(I('请输入第2个点的纵坐标：'))
                if x1 > x2:
                    x1, y1, x2, y2 = x2, y2, x1, y1
                c = B(Q(I('请输入颜色(黑:0 蓝:1 绿:2 青:3 红:4 紫:5 黄:6 白:7)：')))
                c = c[:2] + (5 - L(c)) * '0' + c[2:]
                t.fillcolor(Q(c[2]), Q(c[3]), Q(c[4]))
                for x in W(x1, x2 + 1):
                    try:
                        y = Q(y1 + ((x - x1) / (x2 - x1)) * (y2 - y1))
                    except:
                        y = y1
                    t.up()
                    t.goto((x - 1) * 15 - 150, (y - 1) * 15 - 150)
                    t.down()
                    t.begin_fill()
                    for k in W(4):
                        T(15)
                        t.lt(90)
                    t.end_fill()
                if y1 <= y2:
                    for y in W(y1, y2 + 1):
                        try:
                            x = Q(x1 + ((y - y1) / (y2 - y1)) * (x2 - x1))
                        except:
                            x = x1
                        t.up()
                        t.goto((x - 1) * 15 - 150, (y - 1) * 15 - 150)
                        t.down()
                        t.begin_fill()
                        for k in W(4):
                            T(15)
                            t.lt(90)
                        t.end_fill()
                else:
                    for y in W(y2, y1 + 1):
                        try:
                            x = Q(x1 + ((y - y2) / (y1 - y2)) * (x2 - x1))
                            x = x2 - (x - x1)
                        except:
                            x = x1
                        t.up()
                        t.goto((x - 1) * 15 - 150, (y - 1) * 15 - 150)
                        t.down()
                        t.begin_fill()
                        for k in W(4):
                            T(15)
                            t.lt(90)
                        t.end_fill()
            elif inp == '2':
                x1 = Q(I('请输入左下角的横坐标：'))
                y1 = Q(I('请输入左下角的纵坐标：'))
                x2 = Q(I('请输入右上角的横坐标：'))
                y2 = Q(I('请输入右上角的纵坐标：'))
                c = B(Q(I('请输入颜色(黑:0 蓝:1 绿:2 青:3 红:4 紫:5 黄:6 白:7)：')))
                c = c[:2] + (5 - L(c)) * '0' + c[2:]
                t.fillcolor(Q(c[2]), Q(c[3]), Q(c[4]))
                for x in W(x1, x2 + 1):
                    for y in W(y1, y2 + 1):
                        t.up()
                        t.goto((x - 1) * 15 - 150, (y - 1) * 15 - 150)
                        t.down()
                        t.begin_fill()
                        for k in W(4):
                            T(15)
                            t.lt(90)
                        t.end_fill()
            elif inp == '3':
                break
            else:
                P('输入无效')
            for i in W(5):
                P()
    elif m == '23':
        if not (Sz.ls[0]):
            P('你似乎可能也许大概没开声音...?')
            U(0.8)
            return
        P("键盘上q-u,z-k分别对应低音1到高音1,键盘上的2,3,5,6,7,s,d,g,h,j分别对应低音1到高音1间的所有升降音,空格代表空拍"
          )
        a = [
            'q', '2', 'w', '3', 'e', 'r', '5', 't', '6', 'y', '7', 'u', 'z',
            's', 'x', 'd', 'c', 'v', 'g', 'b', 'h', 'n', 'j', 'm', 'k'
        ]
        s = I()
        for j in s:
            if j != ' ':
                x = Q(245 * 2**(a.index(j) / 12))
                P(j)
                winsound.Beep(x, 200)
                for i in W(4000000):
                    ppp = 1
            else:
                for i in W(6000000):
                    ppp = 1
    elif m == '24':
        import turtle as t
        if Gl.do21:
            t2.clear()
            t2.shape('blank')
        Gl.do21 = 1
        t.clear()
        t.color('black')
        t.up()
        t.goto(0, 0)
        t.down()
        t.seth(0)
        t.speed(0)
        t.shape('square')
        t2 = t.Turtle()
        t2.up()
        t2.shape('square')
        t2.goto(150, 150)
        t2.stamp()
        t2.goto(50, 50)
        lsa = ['K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A', '']
        lsb = [
            '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11',
            '12', '13', ''
        ]
        keypoint = [
            'G02', 'J08', 'E05', 'H09', 'D07', 'F10', 'B11', 'C12', 'A13'
        ]
        for i in W(12):
            T(260)
            K(260)
            t.up()
            t.rt(180)
            T(20)
            t.write(lsa[i], font=('Arial', 16))
            K(20)
            t.lt(180)
            t.down()
            if i != 11:
                t.lt(90)
                T(20)
                t.rt(90)
        t.up()
        t.goto(0, 0)
        t.down()
        t.lt(90)
        for i in W(14):
            T(220)
            K(220)
            t.up()
            t.rt(180)
            T(20)
            t.write(lsb[i], font=('Arial', 9))
            K(20)
            t.lt(180)
            t.down()
            if i != 13:
                t.rt(90)
                T(20)
                t.lt(90)
        P('''规则：
从K01出发，终点是A13，每次操作可以往上走任意格，往右走任意格，或往右上走任意格，你和电脑轮流进行操作，谁先到终点谁就赢。''')
        t.up()
        t.goto(10, 10)
        t.down()
        s = 'K01'
        x = I('谁先来（电脑先来输入1，你先来输入2）?')
        if x == '2':
            while s != 'A13':
                t.color('blue')
                s2 = I('你想走到哪里?')
                while (not ok2(s, s2)):
                    s2 = I('走不到，请重新输入：')
                s = s2
                t.goto(lsb.index(s2[1:]) * 20 + 10, lsa.index(s2[0]) * 20 + 10)
                U(0.3)
                for i in keypoint:
                    if ok2(s, i):
                        t.color('red')
                        P('电脑决定走到', i)
                        s = i
                        t.goto(
                            lsb.index(s[1:]) * 20 + 10,
                            lsa.index(s[0]) * 20 + 10)
            P('电脑赢了!!!')
        else:
            while 1:
                t.color('red')
                m = 1
                for i in keypoint:
                    if ok2(s, i):
                        P('电脑决定走到', i)
                        m = 0
                        s = i
                        t.goto(
                            lsb.index(s[1:]) * 20 + 10,
                            lsa.index(s[0]) * 20 + 10)
                if m:
                    cc = R(1, 4)
                    if cc == 1 and ok2(s, C(O(s[0]) - 1) + s[1:]):
                        P('电脑决定走到', C(O(s[0]) - 1) + s[1:])
                        s = C(O(s[0]) - 1) + s[1:]
                        t.goto(
                            lsb.index(s[1:]) * 20 + 10,
                            lsa.index(s[0]) * 20 + 10)
                    elif cc == 2 and ok2(
                            s, s[0] +
                        ((Q(s[1:]) + 1) < 10) * '0' + S(Q(s[1:]) + 1)):
                        s = s[0] + (
                            (Q(s[1:]) + 1) < 10) * '0' + S(Q(s[1:]) + 1)
                        P('电脑决定走到', s)
                        t.goto(
                            lsb.index(s[1:]) * 20 + 10,
                            lsa.index(s[0]) * 20 + 10)
                    else:
                        s = C(O(s[0]) - 1) + (
                            (Q(s[1:]) + 1) < 10) * '0' + S(Q(s[1:]) + 1)
                        P('电脑决定走到', s)
                        t.goto(
                            lsb.index(s[1:]) * 20 + 10,
                            lsa.index(s[0]) * 20 + 10)
                if s == 'A13':
                    P('电脑赢了!!!')
                    break
                t.color('blue')
                s2 = I('你想走到哪里?')
                while (not ok2(s, s2)):
                    s2 = I('走不到，请重新输入：')
                s = s2
                t.goto(lsb.index(s2[1:]) * 20 + 10, lsa.index(s2[0]) * 20 + 10)
                U(0.3)
                if s == 'A13':
                    P('你赢了!!!')
                    break
        t.up()
    elif m == '25':
        a = I('更改(1)还是查看(2)还是保存为文件(3)?')
        if '1' in a:
            Gl.ss = I('请输入数据:')
            P('已保存')
        elif '2' in a:
            P(Gl.ss)
        else:
            fn = I('文件名?') + '.' + I('后缀名(如txt)?')
            N(fn, 'a').write(Gl.ss)
    elif m == '26':
        P('电脑将随机生成一个n位数，你每次猜一个n位数。电脑会告诉你对了几个数字。')
        n = Q(I('n是几?'))
        x = S(R(10**(n - 1), 10**n - 1))
        a = I('你猜是几?')
        while a != x:
            n1 = 0
            n2 = 0
            for i in W(n):
                n1 += Q(a[i] == x[i])
                n2 += Q(a[i] in x and a[i] != x[i])
            P('位置且数字正确%d个，仅数字正确%d个。' % (n1, n2))
            a = I('你猜是几?')
        P('猜对了!')
    elif m == '27':
        score = 0
        block = Dt.block27
        blockcol = Dt.blockcol27
        a = []
        for i in W(20):
            a.append(
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        f = 15
        while f:
            for c in W(1, 9):
                P('.', end='')
            f -= 1
            P()
        while 1:
            typ = R(1, 9)
            score += blockcol[typ] * 2
            P('方块:')
            for i in W(3):
                for j in W(3):
                    if block[typ][i][j]:
                        P('#', end='')
                    else:
                        P('.', end='')
                P()
            col = Q(I('放在第几列?'))
            while (col + blockcol[typ] > 9):
                col = Q(I('无效列数,请重新输入:'))
            brk = 1
            place = 15
            while (place):
                for i in W(3):
                    for j in W(3):
                        if a[place - i + 2][col + j] and block[typ][i][j]:
                            brk = 0
                            break
                    if brk == 0:
                        break
                if brk == 0:
                    break
                place -= 1
            place += 1
            for i in W(3):
                for j in W(3):
                    if block[typ][i][j]:
                        a[place - i + 2][col + j] = block[typ][i][j]
            f = 15
            while f:
                bl = 1
                for k in W(1, 9):
                    if a[f][k] == 0:
                        bl = 0
                if bl:
                    score += 12
                    for x in W(f, 15):
                        for c in W(1, 9):
                            a[x][c] = a[x + 1][c]
                    a[15] = [
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0
                    ]
                f -= 1
            f = 15
            while f:
                for c in W(1, 9):
                    if a[f][c]:
                        P('#', end='')
                    else:
                        P('.', end='')
                f -= 1
                P()
            bl = 0
            for k in W(1, 9):
                if a[15][k] == 1:
                    bl = 1
            if bl:
                P('分数:', score)
                P('游戏结束')
                break
    elif m == '28':
        trm = I('0为普通计时，1为倒计时：')
        if trm == '0':
            P('a为开始计时，b为结束计时，c为退出')
            tr = 0
            c = I('请输入指令:')
            while c != 'c':
                if c == 'a':
                    tr = tm.time()
                if c == 'b':
                    P('%.2f s' % (tm.time() - tr))
                c = I('请输入指令:')
        if trm == '1':
            t = Q(I('倒计时多少秒?'))
            while t > 0:
                P(t, 's')
                t -= 1
                U(1)
    elif m == '29':
        x = I('电脑显示一个"[回车]"后请立即按回车，有5~10s的准备时间，现在按回车开始:')
        U(R(5, 10))
        s = tm.time()
        I('[回车]')
        e = tm.time()
        P('反应速度:%.2f s' % (e - s))
    elif m == '30':
        x = Q(I('随机下限:'))
        y = Q(I('随机上限:'))
        P(R(x, y - 1) + r.random())
    elif m == '31':
        n = Q(I("多少个数据?"))
        sm = 0
        for i in W(n):
            sm += E(I('数据：'))
        P("%.2f" % (sm / n))
    elif m == '32':
        ls = []
        f = []
        lei = []
        for i in W(1, 18):
            t1 = []
            t2 = []
            for j in W(1, 18):
                t1.append(R(0, 3) == 0)
                t2.append(0)
            ls.append(t1)
            f.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            lei.append(t2)
        for i in W(1, 9):
            for j in W(1, 10 - i):
                f[i][j] = 1
                ls[i][j] = 0
        tot = 0
        for i in W(0, 17):
            ls[i][0] = 0
            ls[i][16] = 0
            ls[0][i] = 0
            ls[16][i] = 0
        for i in W(1, 16):
            for j in W(1, 16):
                tot += ls[i][j]
                for x in W(3):
                    for y in W(3):
                        lei[i][j] += ls[i + x - 1][j + y - 1]
                if ls[i][j] == 1:
                    lei[i][j] = -1
        P('一共%d个雷' % (tot))
        while 1:
            cnt = 0
            P('  123456789012345')
            for i in W(1, 16):
                P(i % 10, end=' ')
                for j in W(1, 16):
                    if f[i][j]:
                        if ls[i][j] == 0:
                            P(lei[i][j], end='')
                        else:
                            P('/', end='')
                        pass
                    else:
                        cnt += 1
                        P('#', end='')
                        pass
                P()
            if cnt == 0:
                P('通关!')
                break
            typ = I('请输入指令类型(0=点开,1=标记为雷)')
            x = Q(I('纵坐标'))
            y = Q(I('横坐标'))
            if typ == '0':
                if ls[x][y] == 1:
                    P('你输了!')
                    break
                else:
                    f[x][y] = 1
            else:
                if ls[x][y] == 0:
                    P('你输了!')
                    break
                else:
                    f[x][y] = 1
    elif m == '33':
        n = Q(I("打印多少行"))
        while n <= 0:
            n = Q(I("不能小于1哦!请再次输入"))
        l = []
        for i in W(1, n + 1):
            l.append(1)
            if i > 2:
                for j in W(2, i):
                    j = i - j
                    l[j] = l[j] + l[j - 1]
            for j in W(i):
                if j == i - 1:
                    P(l[j])
                else:
                    P(l[j], end=" ")
    elif m == '34':
        winner = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
        name = ['石头', '剪刀', '布']
        turn = Q(I('来几局?'))
        tw = 0
        for i in W(turn):
            P('第%d轮' % (i + 1))
            p = Q(I('你出什么(0:石头 1:剪刀 2:布)?'))
            c = R(0, 2)
            P('电脑出%s' % (name[c]))
            tw += winner[p][c]
        if tw > 0:
            P('你赢了')
        elif tw == 0:
            P('平局')
        else:
            P('你输了')
    elif m == '35':
        map1, map2 = Dt.map135, Dt.map235
        le = ['w', 'a', 's', 'd']
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        x, y = 0, 0
        mp = 1
        while (x != 4 or y != 7):
            for i in W(5):
                for j in W(8):
                    if x == i and y == j and mp == 1:
                        P('i', end='')
                    elif map1[i][j] == 2:
                        P('#', end='')
                    elif map1[i][j] == 0:
                        P('.', end='')
                    elif map1[i][j] == 1:
                        P('*', end='')
                P()
            P()
            for i in W(5):
                for j in W(8):
                    if x == i and y == j and mp == 2:
                        P('i', end='')
                    elif map2[i][j] == 0:
                        P('.', end='')
                    else:
                        P('*', end='')
                P()
            c = I('wasd移动位置,c切换地图')
            clear()
            if c == 'c':
                mp = 3 - mp
                if mp == 1:
                    if map1[x][y] == 1:
                        mp = 2
                        P('失败')
                else:
                    if map2[x][y] == 1:
                        mp = 1
                        P('失败')
            else:
                dxn = dx[le.index(c)]
                dyn = dy[le.index(c)]
                if mp == 1:
                    if map1[x + dxn][y + dyn] == 1:
                        P('失败')
                    else:
                        x += dxn
                        y += dyn
                else:
                    if map2[x + dxn][y + dyn] == 1:
                        P('失败')
                    else:
                        x += dxn
                        y += dyn
        P('挑战成功!')
    elif m == '36':
        s = '''
----------------------------------
作者:a9754610
其他参与的人:FisherJohn,lyleli2010等
----------------------------------
这个程序是作者从2020年7月开始写的，距离现在已经有好几年了,
我写这段话的时候这个程序已经是一个十分著名的程序了,
我们的工作室发展得十分出色,希望你能玩的愉快!
----------------------------------'''
        for i in s:
            if i != '\n':
                P(i, end='')
            else:
                P()
                U(1)
    elif m == '37':
        s = I('请输入网址:')
        webbrowser.open(s)
    elif m == '38':
        map1 = Dt.map138
        le = ['w', 'a', 's', 'd']
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        x, y = 0, 0
        while (x != 14 or y != 14):
            for i in W(15):
                for j in W(15):
                    if x == i and y == j:
                        P('i', end='')
                    elif A(x - i) < 2 and A(y - j) < 2 and map1[i][j] == 1:
                        P('*', end='')
                    elif A(x - i) < 2 and A(y - j) < 2 and map1[i][j] == 0:
                        P('.', end='')
                    elif A(x - i) < 2 and A(y - j) < 2 and map1[i][j] == 2:
                        P('#', end='')
                    else:
                        P('?', end='')
                P()
            c = I('wasd移动位置')
            clear()
            dxn = dx[le.index(c)]
            dyn = dy[le.index(c)]
            if map1[x + dxn][y + dyn] == 1:
                pass
            else:
                x += dxn
                y += dyn
        P('挑战成功!')
    elif m == '39':
        x = Q(I('几行?'))
        y = Q(I('几列?'))
        n = Q(I('几个障碍物?'))
        bc = []
        for i in W(n):
            bc.append(I('障碍物位置(请填写编号)?'))
        if bc == ['D06'] and x == 9 and y == 11:
            P('\n我是人工智能，不是人工智障!别想作弊')
            return
        if (bc == ['D08', 'I03']
                or bc == ['I03', 'D08']) and x == 11 and y == 13:
            P('\n我是人工智能，不是人工智障!别想作弊')
            return
        ls = []
        for i in W(x + 1):
            t = []
            for j in W(y + 1):
                t.append(0)
            ls.append(t)
        for i in W(x, 0, -1):
            for j in W(y, 0, -1):
                le = C(O('A') + x - i)
                nu = '0' * (1 - j // 10) + S(j)
                if le + nu in bc:
                    continue
                u = 1
                for ti in W(i + 1, x + 1):
                    let = C(O('A') + x - ti)
                    if let + nu in bc:
                        break
                    if ls[ti][j]:
                        u = 0
                r = 1
                for tj in W(j + 1, y + 1):
                    nut = '0' * (1 - tj // 10) + S(tj)
                    if le + nut in bc:
                        break
                    if ls[i][tj]:
                        r = 0
                ur = 1
                for dur in W(1, M(x - i, y - j) + 1):
                    let = C(O('A') + x - (i + dur))
                    nut = '0' * (1 - (j + dur) // 10) + S(j + dur)
                    if let + nut in bc:
                        break
                    if ls[i + dur][j + dur]:
                        ur = 0
                if u and r and ur:
                    ls[i][j] = 1
        for i in W(x, 0, -1):
            for j in W(1, y + 1):
                if ls[i][j]:
                    P('# ', end='')
                else:
                    P('* ', end='')
            P()
        P('上面图中#是关键点，你需要尽量去走那些点。')
    elif m == '40':
        P('\n')
        corr = R(1, 16)
        ch = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        cl = ch[:corr] + ch[corr + 1:]
        num = [0]
        while (L(ch) > 1):
            x = R(1, L(ch) - 1)
            num.append(ch[x])
            ch = ch[:x] + ch[x + 1:]
        vis = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        s0 = '''
这里一共有16张纸牌，平均分成4
组，每组4张，每张上都有一个随
机的编号(1~16),还有一些提醒。
你第一次可以选择第几组的第几
张，会有提醒，而且你下一次的
组别已经被固定为编号为纸牌编
号跟4取余然后再加1的那一组。\n'''
        P(s0)
        rw = Q(I('从第几组开始(1~4)?'))
        nownum = 0
        while nownum != corr:
            P()
            P('第%d组' % (rw))
            for i in W(4):
                P('第%d个:' % (i + 1), end='')
                if vis[(rw - 1) * 4 + i + 1]:
                    P(num[(rw - 1) * 4 + i + 1])
                else:
                    P('?')
            P()
            c = Q(I('第几个?'))
            nownum = (rw - 1) * 4 + c
            if nownum == corr:
                break
            x = cl[R(1, L(cl) - 1)]
            P()
            P('-====================-')
            P('编号:', num[nownum])
            P('提醒: %d组%d个不是答案' % ((x - 1) // 4 + 1, (x - 1) % 4 + 1))
            P('-====================-')
            P()
            rw = num[nownum] % 4 + 1
            vis[nownum] = 1
        P('猜对了!!')
        P('彩蛋\n话说那谁遇到了一道生物题，它不知道√念什么，看看这道题吧!')
        P('A.根 B.sqrt C.平方根 D.根儿豪')
        if I('你选什么?') == 'D':
            P('做对了，那谁很高兴')
        else:
            P('做错了，那谁决定在下午跑操时...')
    elif m == '41' and 0:
        pass
    elif m == '42':
        n = L(Sz.ls)
        for i in W(n):
            read(i)
        N('Meatpi_Settings.dat', 'w').write(S(Sz.ls))
    elif m == '43':
        Sz.ls = [nowin, 1, -1, 0.6, 'anonymous']
        N('Meatpi_Settings.dat', 'w').write(S(Sz.ls))
        excepter
    elif m == '44':
        score = 0
        ops = ['w', 'a', 's', 'd']
        inbound = lambda x, y: (x >= 0 and x < 4 and y >= 0 and y < 4)
        mp = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        while (1):
            clear()
            ok = 0
            for i in W(4):
                for j in W(4):
                    if mp[i][j] == 0:
                        ok = 1
            if not ok:
                P('游戏结束，得分:', score)
                break
            x = R(0, 3)
            y = R(0, 3)
            while mp[x][y] != 0:
                x = R(0, 3)
                y = R(0, 3)
            mp[x][y] = 2 - Q(R(0, 22) != 0)
            for i in W(4):
                for j in W(4):
                    P(C(mp[i][j] + O('@')), end='')
                P()
            P()
            op = I('Operation(q 4 quit):')
            if op == 'q':
                P('游戏结束，得分:', score)
                break
            while (not (op in ops)):
                op = I('ERROR Please try again:')
            opn = ops.index(op)
            if opn % 2:
                for i in W(4):
                    nowls = [3, 2, 1, 0]
                    if opn / 2:
                        nowls = [0, 1, 2, 3]
                    for j in nowls:
                        u, v = i, j
                        if mp[u][v] == 0:
                            continue
                        while (1):
                            u, v = u + dx[opn], v + dy[opn]
                            if (not inbound(u, v)) or (
                                    mp[u][v] != 0 and
                                    mp[u][v] != mp[u - dx[opn]][v - dy[opn]]):
                                break
                            elif mp[u][v] == 0:
                                mp[u][v] = mp[u - dx[opn]][v - dy[opn]]
                                mp[u - dx[opn]][v - dy[opn]] = 0
                            else:
                                mp[u][v] = mp[u][v] + 1
                                mp[u - dx[opn]][v - dy[opn]] = 0
                                break
            else:
                for j in W(4):
                    nowls = [3, 2, 1, 0]
                    if opn / 2:
                        nowls = [0, 1, 2, 3]
                    for i in nowls:
                        u, v = i, j
                        if mp[u][v] == 0:
                            continue
                        while (1):
                            u, v = u + dx[opn], v + dy[opn]
                            if (not inbound(u, v)) or (
                                    mp[u][v] != 0 and
                                    mp[u][v] != mp[u - dx[opn]][v - dy[opn]]):
                                break
                            elif mp[u][v] == 0:
                                mp[u][v] = mp[u - dx[opn]][v - dy[opn]]
                                mp[u - dx[opn]][v - dy[opn]] = 0
                            else:
                                mp[u][v] = mp[u][v] + 1
                                mp[u - dx[opn]][v - dy[opn]] = 0
                                break
            score += 1
    elif m == '45':
        show(tm)
    elif m == '46':
        P('P O T S')
        a = R(3, 12)
        b = a
        while b % a == 0 or a % b == 0 or gcd(a, b) != 1:
            b = R(3, 12)
        a0, b0 = a, b
        a, b = 0, 0
        c = a0
        while c == a0 or c == b0 or c == A(a0 - b0):
            c = R(2, X(a0, b0) - 1)
        while a != c and b != c:
            P('%d/%d %d/%d --> %d' % (a, a0, b, b0, c))
            op = I('[s]swap,[q]fill,[r]drop,[t]pour,[n]quit:')
            if op == 's':
                a, b, a0, b0 = b, a, b0, a0
            if op == 'q':
                a = a0
            if op == 'r':
                a = 0
            if op == 't':
                t = M(a, b0 - b)
                a -= t
                b += t
            if op == 'n':
                break
    elif m == '47':
        ls = Dt.et47
        I('仅存加密表C1,是否确认?')
        ls = ls[0]
        q = I('加密(1)/解密(2)?')
        if q == '1':
            s = I('请输入:')
            key = ''
            for i in W(L(s)):
                key += C(O('a') + R(0, 15))
            P('你的密码是 ' + key)
            outp = ''
            for i in W(L(s)):
                outp += fff(O(s[i]) + ls[i % 16][O(key[i]) - O('a')], 8) + '8'
            P(fff(Q(outp, 9), 16))
        else:
            s = fff(Q(I('请输入:'), 16), 9)
            key = I('密码:')
            now = ''
            cnt = 0
            for i in W(L(s)):
                if s[i] != '8':
                    now += S(s[i])
                else:
                    P(C(Q(now, 8) - ls[cnt % 16][O(key[cnt]) - O('a')]),
                      end='')
                    cnt += 1
                    now = ''
            P()
    elif m == '48':
        s = I('请输入要下载的文件的文件号(例：uk608ajr)：')
        s = 'https://www.luogu.com.cn/api/team/downloadFile/' + s
        webbrowser.open(s)
    elif m == '49':
        n = R(1, 100)
        ls = [0]
        for i in W(100):
            if A(n - i - 1) <= 10:
                ls.append(0)
            else:
                ls.append(Q(R(0, 2) > 0))
        for i in W(100):
            if ls[i + 1] == 0:
                if isprimebad(A(i + 1 - n)):
                    ls[i + 1] = 2
        step = 0
        P('注：虽然a97在这个程序上花了很大时间，这个程序的效果还不大理想，有一些不合理的地方，所以我们后续会继续进行更新。')
        P('这是一个猜数游戏(猜1~100的一个随机数)，电脑每次会根据你猜的数给出3种提醒……')
        while (1):
            step += 1
            p = Q(I('你猜的数：'))
            if p == n:
                P('猜对了!')
                P('使用步数：', step)
                break
            P('猜错了')
            if ls[p] == 1:
                P('答案比你猜的数' + Q(n > p) * '大' + Q(n < p) * '小')
            elif ls[p] > 1:
                P('答案与你猜的数的差是质数')
            else:
                P('答案与你猜的数的差不是质数，它的最小质因数是', badfunction(A(n - p)))
    elif m == '50':
        P('数学老师狂喜')
        for i in W(5):
            a, b = R(1, 6), R(1, 6) * (Q(R(0, 1) > 1) * 2 - 1)
            c, d = R(1, 6), R(1, 6) * (Q(R(0, 1) > 1) * 2 - 1)
            q, w, e = a * c, a * d + b * c, b * d
            P('(ax+b)(cx+d)=%dx2+%dx+%d' % (q, w, e))
            aa, bb, cc, dd = E(I('a?')), E(I('b?')), E(I('c?')), E(I('d?'))
            if aa * cc == q and aa * dd + bb * cc == w and bb * dd == e:
                P('AC')
            else:
                P('WA')
                P('Correct Answer:', a, b, c, d)
    elif m == '51':
        s = Sz.ls[4]
        k = 0
        for i in s:
            k += O(i)
        k %= 100
        P('你的幸运数字是：' + '0' * (k < 10) + S(k))
    elif m == '52':
        if I('确认要毁灭(如果坚持毁灭请填1)?') == '1':
            os.remove(__file__)
            return
    elif m == '53':
        s = '''感谢名单: (*表示重要)
a97_QwQ* FisherJohn* liyi_____
Donnyliu01 shao28Azyc139 ybk231847 wrp_04
OwenLMZ2022* liwant williamwei*
'''
        P(s)
    elif m == '54':
        P('骗子来喽~啊哈哈哈哈哈（雾')
        webbrowser.open(
            'https://mathsolver.microsoft.com/zh/quiz/15xukb54z?ref=s')
    elif m == '55':
        webbrowser.open('https://g9mee.csb.app/luog.jpg')
    elif m == '57':
        k = Q(I('定时多少秒后开始炸骗?'))
        P('倒计时中...')
        U(k)
        webbrowser.open('https://www.bilibili.com/video/BV1VB4y197c1/')
    elif m == '58':
        while 1:
            I('Press enter to get the current meatpi standard time ')
            P()
            now = tm.time()
            cmp = 1595692800.0
            add = now - cmp
            tim = S(Q(add / 86400 * 20000))
            ln = L(tim)
            tim = tim[0:ln - 5] + ':' + tim[ln - 5] + ':' + tim[ln - 4:]
            P()
            P(tim)
    elif m == '60':
        play60()
    elif m == '61':
        s = r'''\
while 1:
    print("''' + Sz.ls[4] + '''\
 is polite :)")'''
        N('creeper.py', 'w').write(s)
        P('哦，你的文件夹/桌面里貌似多了什么东西 :)')
    elif m == '62':
        I('此算法仅能加密小写字母和空格，是否确认>')
        wheel = Dt.wheel62
        q = I('加密(0)还是解密(1)?')
        s = I('加密或解密内容? ')
        c = I('密码(0~4的排列加上5个小写字母或空格,比如13420kkksc)?')
        new_wheel = []
        for i in W(5):
            new_wheel.append(wheel[O(c[i]) - O('0')])
            ls1 = new_wheel[i][getord62(c[i + 5]):]
            ls2 = new_wheel[i][0:getord62(c[i + 5])]
            ls1.extend(ls2)
            new_wheel.append(ls1)
        if q == '0':
            for ch in s:
                if c[-1] != ' ':
                    c = c[0:9] + getchr62(getord62(c[-1]) + 1) + c[10:]
                else:
                    c = c[0:9] + 'a' + c[10:]
                    if c[-2] != ' ':
                        c = c[0:8] + getchr62(getord62(c[-1]) + 1) + c[9:]
                    else:
                        c = c[0:8] + 'a' + c[9:]
                        if c[-3] != ' ':
                            c = c[0:7] + getchr62(getord62(c[-1]) + 1) + c[8:]
                        else:
                            c = c[0:7] + 'a' + c[8:]
                            if c[-4] != ' ':
                                c = c[0:6] + getchr62(getord62(c[-1]) +
                                                      1) + c[7:]
                            else:
                                c = c[0:6] + 'a' + c[7:]
                                if c[-5] != ' ':
                                    c = c[0:5] + getchr62(getord62(c[-1]) +
                                                          1) + c[6:]
                                else:
                                    c = c[0:5] + 'a' + c[6:]
                new_wheel = []
                for i in W(5):
                    new_wheel.append(wheel[O(c[i]) - O('0')])
                    ls1 = new_wheel[i][getord62(c[i + 5]):]
                    ls2 = new_wheel[i][0:getord62(c[i + 5])]
                    ls1.extend(ls2)
                    new_wheel.append(ls1)
                res = ch
                for i in new_wheel:
                    res = getchr62(i[getord62(res)])
                P(res, end='')
        else:
            for ch in s:
                if c[-1] != ' ':
                    c = c[0:9] + getchr62(getord62(c[-1]) + 1) + c[10:]
                else:
                    c = c[0:9] + 'a' + c[10:]
                    if c[-2] != ' ':
                        c = c[0:8] + getchr62(getord62(c[-1]) + 1) + c[9:]
                    else:
                        c = c[0:8] + 'a' + c[9:]
                        if c[-3] != ' ':
                            c = c[0:7] + getchr62(getord62(c[-1]) + 1) + c[8:]
                        else:
                            c = c[0:7] + 'a' + c[8:]
                            if c[-4] != ' ':
                                c = c[0:6] + getchr62(getord62(c[-1]) +
                                                      1) + c[7:]
                            else:
                                c = c[0:6] + 'a' + c[7:]
                                if c[-5] != ' ':
                                    c = c[0:5] + getchr62(getord62(c[-1]) +
                                                          1) + c[6:]
                                else:
                                    c = c[0:5] + 'a' + c[6:]
                new_wheel = []
                for i in W(5):
                    new_wheel.append(wheel[O(c[i]) - O('0')])
                    ls1 = new_wheel[i][getord62(c[i + 5]):]
                    ls2 = new_wheel[i][0:getord62(c[i + 5])]
                    ls1.extend(ls2)
                    new_wheel.append(ls1)
                res = ch
                for i in new_wheel[::-1]:
                    res = getchr62(i.index(getord62(res)))
                P(res, end='')
        P()
    elif m == '63':
        s = Q(I('请输入该无理数的平方(例:阿姆斯特朗常数为242): '))
        e = Q(I('计算到小数点后的位数: '))
        ei = 0
        x = Q(s**0.5)
        P(S(x) + '.', end='')
        while (ei < e):
            ei, s, x = ei + 1, s * 100, x * 10
            while (x**2 <= s):
                x += 1
            x -= 1
            P(S(x % 10), end='')
        P()
    elif m == '64' or m == '65':
        if m == '64':
            mp64 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
            temp = 5
            cols = 3
        else:
            mp64 = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
            temp = 8
            cols = 7
        for i in range(1, cols + 1):
            for k in range(int((temp * temp - 1) / cols)):
                u, v = R(0, temp - 1), R(0, temp - 1)
                while mp64[u][v] != 0:
                    u, v = R(0, temp - 1), R(0, temp - 1)
                mp64[u][v] = i
        while 1:
            ok = 1
            clear()
            col = [' ', 'A', 'B', 'C']
            if m == '65':
                col = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
            for u in range(temp):
                for v in range(temp):
                    print(col[mp64[u][v]], end='')
                print()
            ops = ['w', 'a', 's', 'd']
            dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
            op = I('Operation:')
            while (not (op in ops)):
                op = I('ERROR Please try again:')
            done = 0
            for u in range(temp):
                for v in range(temp):
                    if mp64[u][v] == 0:
                        done = 1
                        try:
                            mp64[u][v], mp64[u - dx[ops.index(op)]][v - dy[
                                ops.index(op)]] = mp64[u - dx[ops.index(op)]][
                                    v - dy[ops.index(op)]], mp64[u][v]
                        except:
                            pass
                        break
                if done:
                    break
            for i in range(1, cols + 1):
                done = 0
                for u in range(temp):
                    for v in range(temp):
                        if mp64[u][v] == i:
                            if m == '64':
                                vis = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0]]
                            else:
                                vis = [[0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 0]]
                            ok = ok and (dfs64(vis, mp64, u, v, i, m) == int(
                                (temp * temp - 1) / cols))
                            done = 1
                        break
                    if done:
                        break
            if ok:
                print('You win!')
                break
    elif m == '66':
        modes = []
        for i in range(14):
            modes.append(R(0, 3))
        for i in [5, 4, 3, 2, 1, 0]:
            for j in [5, 4, 3, 2, 1, 0]:
                clear()
                op66(modes, i, j, 1, 1)
                U(1)
        x, y = R(6, 9), R(6, 9)
        clear()
        res = op66(modes, x, y, 0, 1)
        P()
        resi = Q(I('What is this number?'))
        xi = resi // 10
        yi = resi % 10
        if res == op66(modes, xi, yi, 0, 0):
            P('correct!')
        else:
            P('wrong... the answer is', x * 10 + y)
    elif m == '67':
        open('Meatpi_Exceptions.txt', 'w').write('')
    elif m == '68':
        open('Meatpi_Data.dat', 'w').write('')
    elif m == '2293':
        Gl.shf = 1
        P('好像发生了一些事情……')
    elif m == '114514':
        P('!程#序%发&生*了）意@外￥的……错）误!')
        U(2)
        while 1:
            P('1太14臭51了41把14程序51臭死4了', end='')
    else:
        P('输入无效')


def main():
    if Sz.ls[0]:
        winsound.Beep(400, 600)
    try:
        Gl.shf = 0
        Gl.do21 = 0
        Gl.ss = ''
        while True:
            Gl.run52 = 0
            if nowin:
                Sz.ls[0] = 0
            try:
                if type(Sz.ls[0]) != int:
                    excepter
            except:
                open(__file__, 'r+').write('=')
                excepter
            P('*^' * 14)
            P('<', tm.asctime(tm.localtime(tm.time())), '>')
            P('欢迎使用meatπ  按Ctrl+c退出')
            P('meatπ 3周年倒计时:', int(1690350180 - tm.time()))
            P('''
-> 1.计算类功能
-> 2.工具类功能
-> 3.游戏类功能''')
            if Gl.shf == 0:
                P('-> 4.?????????')
            else:
                P('-> 4.好van的小游戏“推箱子”!!!')
            bm = I('''请填序号 如 3：''')
            clear()
            if bm == '1':
                P(r'''-> 01.普通计算器
-> 02.质数判断器:
-> > 1.输出1到x以内的质数
-> > 2.输出x到y的质数
-> > 3.判断x是不是质数
-> 03.等差数列求和
-> 04.化简分数
-> 07.最小公倍数
-> 08.算24
-> 12.最大公因数
-> 13.解二元一次方程
-> 14.解一元二次方程
-> 15.质因数分解
-> 20.计算π
-> 31.计算平均数 (作者:FisherJohn)
-> 33.帕斯卡三角形 (作者:liyi_____)
-> 63.平方根式无理数计算器''')
            if bm == '2':
                P(r'''-> 05.十进制变几进制
-> 06.几进制变十进制
-> 16.生成勾股数
-> 19.画心
-> 22.画板
-> 25.更改/查看/保存数据
-> 28.计时器
-> 30.生成随机数
-> 36.作者的话
-> 37.上网
-> 39.坑碟游戏解析
-> 42.设置
-> 43.恢复出厂设置
-> 47.第二代加密和解密
-> 48.下载洛谷文件
-> 52.自毁
-> 53.感谢名单
-> 55.展示logo
-> 58.MSTS
-> 62.最新版加密解密
-> 67.清理日志
-> 68.重置数据''')
            if bm == '3':
                P(r'''-> 09.计算游戏
-> 10.打字游戏
-> 11.猜数游戏1
-> 21.坑碟游戏经典版
-> 23.音乐大师
-> 24.坑碟游戏升级版
-> 26.猜数游戏2
-> 27.俄罗斯方块简化版
-> 29.测试反应速度
-> 32.扫雷
-> 34.石头剪刀布
-> 35.2层迷宫(体验版)
-> 38.失明迷宫(体验版)
-> 40.FJ的卡牌游戏
-> 44.2048
-> 46.Pots
-> 49.猜数游戏3
-> 50.因式分解小练习
-> 51.计算幸运数字
-> 54.数学骗紫
-> 57.定时炸骗
-> 61.creeper.py
-> 64.颜色华容道(3*8)
-> 65.颜色华容道(7*9)
-> 66.FJ的手表''')
            if bm == '4':
                if Gl.shf == 0:
                    P(r'-> 2293.请!%在%下方@!@填#序号&#!处填"2293"@#&')
                else:
                    playhf(tm)
                    continue
            m = I('''请填序号 如 02：''')
            runfunc(m)
            P()
            U(Sz.ls[3])
            P(Gl.ads[R(0, len(Gl.ads) - 2)])
            I('请按回车继续')
            clear()
    except KeyboardInterrupt:
        pass
    except Exception as exc:
        open('Meatpi_Exceptions.txt', 'a').write(
            tm.asctime(tm.localtime(tm.time())) + ' ' + str(type(exc)) + ' ' +
            str(exc) + '\n')
        if Sz.ls[1]:
            clear()
            main()


if __name__ == '__main__':
    main()
