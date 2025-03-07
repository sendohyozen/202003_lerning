# 次数和人向上取整
# 按次数和人分开计算

import math
# 配送调配计算
# 设置默认参数
def calculate_job(size=1,person=None,num=None):
    if(person !=None)and(num==None):
         #配送次数计算过程
        num = math.ceil(size * 100 / 20/person)
        print('%.1f个标准集装箱大的快递项目，使用%d位快递员配送，则需要配送次数%d次' %(size,person,num))
    elif(person==None)and(num!=None):
        #快递员数计算过程
        person = math.ceil(size *100 /20/ num)
        print('%.1f个标准集装箱大的快递项目，%d次配送完毕，则需要快递员数：%d位' %(size,num,person))
calculate_job(size=1.5,person=2)
calculate_job(size=0.5,num=1)


# 更改为选择类型
# 交互式输入

import math
types = int(input('请选择需要计算的工作：1-配送次数计算，2-快递员数计算，请选择：'))
sizes = float(input('请输入项目大小：1代表标准，还可以输入其他倍数或小数'))
if types ==1:
    others = int(input('请输入投入的快递员数，请输入整数'))
else:
    others = int(input('请输入快递次数，请输入整数'))

# 配送调配计算
# 设置默认参数
def calculate_job(types,sizes,others):
    print('计算结果如下')
    if types ==1:
         #配送次数计算过程
        num = math.ceil(sizes * 100 / 20/others)
        print('%.1f个标准集装箱大的快递项目，使用%d位快递员配送，则需要配送次数%d次' %(sizes,others,num))
    elif types==2:
        #快递员数计算过程
        person = math.ceil(sizes *100 /20/ others)
        print('%.1f个标准集装箱大的快递项目，%d次配送完毕，则需要快递员数：%d位' %(sizes,others,person))

calculate_job(types,sizes,others)

# bug
# 当我们选择计算配送次数， 项目大小为2.2倍，快递员数为1时。 计算工时：需要配送次数 = 2.2*100/20/1 ，得到的结果应该是11次，可是打印出来却是12次。
# 这是为什么呢？ 还是老问题， python江湖中的除法，会将数字都转换二进制再进行计算，得到的结果是一个二进制，造成数字增加。不信，你运行一下下面程序。
2.2*100/20  # ------------->11.000000000000002
math.ceil(2.2*100/20) #------------->12

# round()函数是python中提供解决小数的保留问题。此函数格式round(x ，n) x表示小数，n表示需要保留的小数位。
import math
types = int(input('请选择需要计算的工作：1-配送次数计算，2-快递员数计算，请选择'))
sizes = float(input('请输入项目大小：1代表标准，还可以输入其他倍数或小数'))
if types ==1:
    others = int(input('请输入投入的快递员数，请输入整数'))
else:
    others = int(input('请输入快递次数，请输入整数'))

# 配送调配计算
# 设置默认参数
def calculate_job(types,sizes,others):
    print('计算结果如下')
    if types ==1:
         #配送次数计算过程
        num = math.ceil(round((sizes * 100 / 20/others),2))
        print('%.1f个标准集装箱大的快递项目，使用%d位快递员配送，则需要配送次数%d次' %(sizes,others,num))
    elif types==2:
        #快递员数计算过程
        person = math.ceil(round((sizes *100 /20/ others),2))
        print('%.1f个标准集装箱大的快递项目，%d次配送完毕，则需要快递员数：%d位' %(sizes,others,person))

calculate_job(types,sizes,others)

# 但是，按照函数封装代码的思想，我们现在代码写的很杂。
# 那我们把它优化一下？
# 怎么优化呢？
# 江湖箴言：创建一个主函数，用来调用其他子函数。
import math


def BOSS_input():
    # 输入内容
    types = int(input('请选择需要计算的工作：1-配送次数计算，2-快递员数计算，请选择'))
    sizes = float(input('请输入项目大小：1代表标准，还可以输入其他倍数或小数'))
    if types == 1:
        others = int(input('请输入投入的快递员数，请输入整数'))
    else:
        others = int(input('请输入快递次数，请输入整数'))

    return types, sizes, others  # 这里返回一个数组


# 计算工作量
def calculate_job(data_input):
    # 获取参数数值
    types = data_input[0]
    sizes = data_input[1]
    others = data_input[2]

    print('计算结果如下')
    if types == 1:
        # 配送次数计算过程
        num = math.ceil(round((sizes * 100 / 20 / others), 2))
        print('%.1f个标准集装箱大的快递项目，使用%d位快递员配送，则需要配送次数%d次' % (sizes, others, num))
    elif types == 2:
        # 快递员数计算过程
        person = math.ceil(round((sizes * 100 / 20 / others), 2))
        print('%.1f个标准集装箱大的快递项目，%d次配送完毕，则需要快递员数：%d位' % (sizes, others, person))


# 主函数
def res():
    data_input = BOSS_input()
    calculate_job(data_input)


# 调用主函数
res()