# 通过自己方法，完成向上取整.
# 用户输入1.1，变成2
# 用户输入1.5，变成2
# 用户输入1.9，变成2

def rounding(num):
    if num % 1 == 0:
        return int(num)
    else:
        data = int(num) + 1
        return data


num = float(input('请输入数字：'))
num1 = rounding(num)
print(num1)


# 出租车车费计算方式如下：
# 1、打车距离在3公里以内，只收起步价15元。
# 2、距离在3公里~15公里，每1公里加3元。
# 3、距离超过15公里后，每1公里加5元。请完成计价函数。
# 题目讲解
# 今天需要和BOSS朋友去吃饭，我们一起打车去市中心，我们想写一个程序，输入坐车公里数，就能自动计算车费。 出租车车费计算方式如下：

def money(distance):
    money = 0
    if distance < 3:
        money = 15
    elif 3 <= distance <= 15:
        money = 15 + (distance-3)*3
    else:
        money = 15 + 12*3 + (distance-15)*5
    return money

def dis():
    dis = float(input("输入坐车公里数:"))
    return dis

def charge():
    a = dis()
    print("车费为%f" %(money(a)))

charge()


# 参考答案
import math
km = math.ceil(float(input('请输入坐车的公里数:可以输入小数')))
def calculate(km):
    if km<=3:
        money = 15
    elif 3<km<=15:
        money = 15+(km-3)*3
    elif km>15:
        money = 15+12*3+(km-15)*5
    print('本次打车费用为:%d元'%money)
calculate(km)