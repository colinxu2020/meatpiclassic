import random
import webbrowser
import time as tm

import categorybase as base
from settings import Settings


class Tools(base.BaseCategory):
    """工具功能"""
    def decimal_to_N_decimal():
        """10进制转换N进制"""
        n = int(input('要转换的数是？ '))
        x = int(input('要转换成多少进制？ '))
        a=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        b=[]
        while n:
            y=n%x
            n//=x;
            b.append(y)
        b.reverse()
        res = ''
        for i in b:
            res += a[i]
        return res
        
    def N_decimal_to_decimal():
        """N进制转换10进制"""
        n = int(input('要转换的数是？ '))
        x = int(input('一开始是什么进制？ '))
        print(int(n,x))
        
    def generate_pythagoras():
        """计算勾股数"""
        a = int(input('请输入参数：'))
        x = a*2-1
        y = (x*x-1)/2
        z = y + 1
        print('结果：',x,y,z)
        
    def draw_heart():
        """画心（未重写）"""
        import turtle as t
        t.clear()
        cor = []
        t.speed(0)
        t.seth(0)
        t.shape('classic')
        t.color('black')
        t.up()
        t.goto(0,0)
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
        
    def draw_board():
        """画板（未重写）"""
        import turtle as t
        t.clear()
        t.speed(0)
        t.seth(0)
        t.shape('classic')
        t.color('black')
        t.up()
        t.goto(0,0)
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
    
    def clock():
        """计时器"""
        typ = input('0为普通计时，1为倒计时：')
        if typ == '0':
            print('start为开始计时，end为结束计时，exit为退出')
            tr = 0
            command = input('请输入指令:')
            while command != 'exit':
                if c == 'start':
                    tr = tm.time()
                if c == 'end':
                    print(tm.time()-tr)
                command = input('请输入指令:')
        else:
            t = int(input('倒计时多少秒?'))
            while t > 0:
                print(t,'s')
                t -= 1
                tm.sleep(1)
                
    def random():
        """生成随机数"""
        x = int(input('随机下限:'))
        y = int(input('随机上限:'))
        print(random.randint(x,y-1))
       
    def author_voise():
       """作者的话（维护中）"""
       
    def 坑碟游戏解析():
       """坑碟游戏解析（维护中）"""
       
    def change_settings():
       """修改配置"""
       Settings.settings = Settings.ask_settings()
       Settings.store_settings()
       
    def 加密与解密():
       """加密与解密（维护中）"""
       
    def download_luogu_file():
        """下载洛谷文件"""
        id = input('请输入要下载的文件的文件号(例：uk608ajr)：')
        webbrowser.open('https://www.luogu.com.cn/api/team/downloadFile/'+id)
        
    def thanks_list():
       """感谢名单"""
       print('''感谢名单：
代码支持: a97 FJ liyi zyc baidu Colinxu2020(厚颜无耻的自己加上的)
团队支持: FJ ybk DL01
广告支持: a97 FJ ybk
灵感支持: FJ DL01 wrp
资源支持: baidu MMS* bilibili
*Microsoft Math solver
''')

    def show_logo():
        """展示LOGO"""
        webbrowser.open('https://cdn.luogu.com.cn/upload/image_hosting/0vdhm9qn.png?x-oss-process=image/resize,m_lfit,h_5100,w_6750')
        
    def MSTS():
        """显示Meatpi标准时间"""
        
        now = tm.time()
        cmp = 1595692800.0
        add = now-cmp
        tim = str(int(add/86400*20000))
        ln = len(tim)
        tim = tim[0:ln-5]+':'+tim[ln-5]+':'+tim[ln-4:]
        print('Meatpi标准时间：',tim)