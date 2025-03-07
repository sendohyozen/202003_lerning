# 第一步:明确目标
# 在Bike基础上，创建子类Motorbike，子类Motorbike继承父类Bike。
#
# 在子类Motorbike中，改造父类init初始化方法；初始化方法中，增加默认参数Motorbike=92，表示摩托车类使用的汽油号。
#
# 第二步:分析过程
# 使用本节课案例中的Bike类，在Bike类基础上，创建子类Motorbike，改造初始方法，增加默认参数Motorbike=92。
class Bike:
    # 初始化方法 no代表车辆编号、age代表车辆年限、
    # state代表车辆状态，0代表待租借，1代表租借中
    def __init__(self, NO, age, state=0):
        self.NO = NO
        self.age = age
        self.state = state

    def __str__(self):
        if self.state == 0:
            status = '待租借'
        else:
            status = '租借中'
        return '车辆编号%d 已经运行%d年，车辆状态：%s' % (self.NO, self.age, status)

class Motorbike(Bike):
    def __init__(self, NO, age, state=0, Motorbike=92):
        self.NO = NO
        self.age = age
        self.state = state
        self.Motorbike = Motorbike

    def __str__(self):
        if self.state == 0:
            status = '待租借'
        else:
            status = '租借中'
        return '车辆编号%d 已经运行%d年，车辆状态：%s, 马力为%d' % (self.NO, self.age, status, self.Motorbike)


Motor1 = Motorbike(1005,4)
print(Motor1)
Motor2 = Motorbike(1006,4,0,58)
print(Motor2)
Motor3 = Motorbike(1006,4,58)
print(Motor3)



# 题目要求
# 在Bike基础上，创建子类Car，子类Car继承父类Bike。
# 在子类Car中，改造父类init初始化方法；初始化方法中，增加参数name，用来接收汽车的牌子，增加参数gasoline，表示汽车类使用的汽油号。
# 题目讲解
# 使用本节课案例中的Bike类，在Bike类基础上，创建子类Car，改造初始方法，增加参数，车的牌子，车需要加多少号的汽油。
class Bike:
    # 初始化方法 no代表车辆编号、age代表车辆年限、
    # state代表车辆状态，0代表待租借，1代表租借中
    def __init__(self, NO, age, state=0):
        self.NO = NO
        self.age = age
        self.state = state

    def __str__(self):
        if self.state == 0:
            status = '待租借'
        else:
            status = '租借中'
        return '车辆编号%d 已经运行%d年，车辆状态：%s' % (self.NO, self.age, status)

class Car(Bike):
    def __init__(self, NO, age, brand, gasolin, state=0):
        self.NO = NO
        self.age = age
        self.state = state
        self.brand = brand
        self.gasolin = gasolin

    def __str__(self):
        if self.state == 0:
            status = '待租借'
        else:
            status = '租借中'
        return '车辆编号%d 已经运行%d年，车辆状态：%s, 品牌为%s，需要加%s号汽油' % (self.NO, self.age, status, self.brand, self.gasolin)

print('#'*30)
car1 = Car(1007,4, 'BMW', '95')
print(car1)

