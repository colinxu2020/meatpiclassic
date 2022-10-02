import math

import categorybase as base


class Math(base.BaseCategory):
    """数学功能"""
    def calc():
        """计算器"""
        print('''特殊运算符号：
**  次方  
//  整除
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
            
    def equidistant_series_sum():
        """等差数列求和"""
        st=int(input("数列从几开始？"))
        ed=int(input("数列到几结束？"))
        typ=int(input('知道公差输入1，知道项数输入2'))
        if typ==1:
            d=int(input('公差？'))
            n = (e-s)/d+1
        else:
            n=int(input('项数？'))
        print("答案是：",(st+ed)*n/2)
        
    def simplify_fractions():
        """化简分数"""
        a=int(input("分子？"))
        b=int(input("分母？"))
        x=gcd(a,b)
        print(a/x,'/',b/x,sep='')
        
    def lcm():
        """最小公倍数"""
        print(math.lcm(int(input('第一个数：')), int(input('第二个数？'))))
        
    def calc24():
        """算24（维护中）"""
        
    def gcd():
        """最大公倍数"""
        print(math.gcd(int(input('第一个数：')), int(input('第二个数？'))))
        
    def solve_quadratic_equation():
        """解二元一次方程"""
        info={}
        print('''二元一次方程标准形式：
ax + by + c = 0
dx + ey + f = 0''')
        for i in ['a','b','c','d','e','f']:
            info[i]=int(input(f'{i}: '))
        for i,j in info.items():
            exec(f'{i}={j}')
        print('x =',(c*e-b*f)/(b*d-a*e))
        print('y =',(c*d-a*f)/(a*e-b*d))
            
    def solve_quadratic_equation():
        """解一元二次方程"""
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
            print('无实数解')
            
    def decompose_prime_factors():
        """分解质因数"""
        n = int(input('请输入想分解的数：'))
        if n <= 1:
                print('无法分解')
                return;
        x = 2
        while n != 1:
            while n % x == 0:
                n /= x
                print(x,end=' ')
            x += 1
            
    def calc_pi():
        """算π"""
        n=int(input('精度：'))
        t=n+10
        b=10**t
        x1=b*4//5
        x2=b//-239
        s=x1+x2
        n*=2
        for i in range(3,n,2):
            x1//=-25
            x2//=-57121
            x=(x1+x2)//i
            s+=x
        pai=s*4
        pai//=10**10
        print('3.'+str(pai)[1:])
        
    def calc_avaerage():
        """算平均数"""
        n = int(input("多少个数据?"))
        sum = 0
        for i in range(n):
            sum += int(input('数据：'))
        print(sum/n)
        
    def pascal_triangle():
        """帕斯卡三角形"""
       
        n = int(input("打印多少行"))
        l = []
        for i in range(1,n+1):
            l.append(1)
            if i>2:
                for j in range(2,i):
                    j=i-j
                    l[j]=l[j]+l[j-1]
            for j in range(i):
                print(l[j],end=" ")
            print()
    
    
class Prime(Math):
    """质数相关功能"""
    def sub():
        """输出从一个数到另一个数的质数"""
        isprime={}
        print('运行时间可能较长，请耐心等待')
        
        st=int(input("请输入第一个数："))
        ed=int(input("请输入第二个数："))
        for i in range(st,ed+1):
            isprime[i]=1
        
        for i in range(max(2,st),ed+1):
            if not isprime[i]:
                continue
            for j in range(i*2, ed+1, i):
                isprime[j]=0
        for i in range(st,ed+1):
            if isprime[i]:
                print(i,end=' ')
        print()
        
    def check():
        """判断一个数是不是质数"""
        n=int(input("请输入这个数："))
        if n<2:
            return print('不是质数')
        for i in range(2, n):
            if n%i==0:
                print('不是质数')
                break
        else:
            print('是质数')
        
    
class Encrypt(Math):
    """加解密功能"""