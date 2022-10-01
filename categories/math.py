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
    
class Prime(Math):
    """质数相关功能"""
    
class Encrypt(Math):
    """加解密功能"""