# 今天我们要完成的任务是帮共享单车公司完成一个共享单车的租借平台。
# 在这个共享平台中，大家可以查看到所有的单车，能够进行租借、还车功能，也可以把自己的单车共享出来，放在平台上，让其他人使用。

# 分析流程，拆解项目
# 这节课这个项目，我们要使用面向对象编程思维来完成。既然是面向对象编程，也就是类、对象、实例化；
# 最主要的就是类。那么，我们需要写多少个类呢？需要定义多少个属性呢？需要定义多少个方法呢？

# 既然是共享单车租借系统，手段是租借，对象是单车。
# 那么，我们就先创建两个类。
# 一个单车类Bike，用来实例化单车对象，绑定单车的属性。
# 一个平台管理类Manage，将查询车辆，共享车辆，租借车辆，归还车辆功能封装到该类中。
# 并且，当平台管理类Manage实例化对象时，可以给用户弹出一个菜单，让用户选择不同的功能。

# 逐步解决，逐渐完善
# Bike类
# 我们依据由简入难的思路，先来完成第一个简单的类，Bike类。
# 每辆车都有基本的属性：车辆编号，使用年限，租借状态。我们利用初始化__init__ ，让实例被创建时自动获取这些属性。
class Bike(object):
    def __init__(self, number, year, status):
        self.number = number
        self.year = year
        self.status = status

    def attri(self):
        print("The number of this bike is %d, can be used for %d years, Now it is %s" % (
        self.number, self.year, self.status))


a1 = Bike(111, 3, 'used')
a1.attri()


# 参考答案
class Bike:
    # 初始化方法 NO代表车辆编号、age代表车辆年限、
    # state代表车辆状态，0代表待租借，1代表租借中
    def __init__(self, NO, age, state=0):
        self.NO = NO
        self.age = age
        self.state = state


bike = Bike(1001, 2)
print(bike.NO)


# 在初始化init方法中，我们将车辆状态state参数的默认值设置为0，用来表示待租借，用1来表示租借中。

# 代码还没完，我们目前只完成Bike类的属性， 接下来我们还要完成Bike的方法。

# 接下来，我们使用Bike类创建一个实例，调用info方法。
class Bike:
    # 初始化方法 no代表车辆编号、age代表车辆年限、
    # state代表车辆状态，0代表待租借，1代表租借中
    def __init__(self, NO, age, state=0):
        self.NO = NO
        self.age = age
        self.state = state

    def info(self):
        if self.state == 0:
            status = '待租借'
        else:
            status = '租借中'
        return '车辆编号%d 已经运行%d年，车辆状态：%s' % (self.NO, self.age, status)


bike = Bike(1001, 2)
print(bike.info())


# 不过小K要传授给大家一个新方法__str__(self)。 这个方法类似__init__(self)方法，在类中有着特殊功能。
# 它会像__init__(self)方法一样，在类实例化对象时，将此方法绑定到对象中；当我们打印实例化对象时，就会自动打印出__str__(self)方法中的内容。
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


bike = Bike(1001, 2)
print(bike)


# 在上述代码中，我们给Bike类绑定了__str__ (self)方法， 实例化对象bike = Bike(1001,2)后直接打印bike信息，就会发现车辆的所有信息已经全部显示出来。


# Manage类
# 首先，我们完成第一个类方法 menu。
# menu()类方法是系统欢迎界面，我们已经有了欢迎界面的效果。用户输入数字，就会选择相应的功能。
# 1.查询所有车辆
# def info_bike(self):
# #2.共享车辆
# def add_bike(self):
# #3.租借车辆
# def lease_bike(self):
# #4.归还车辆
# def revert_bike(self):
# #5.退出系统
# break


class Manage:
    # 系统菜单
    def menu(self):
        print("欢迎使用共享单车租借系统\n")
        while True:
            print('1.查询所有车辆\n 2.共享车辆\n 3.租借车辆\n 4.归还车辆\n 5.退出系统\n')
            select = int(input('请输入所选功能对应得数字：'))
            if select == 1:
                # 单车信息
                self.info_bike()
            elif select == 2:
                # 共享单车
                self.add_bike()
            elif select == 3:
                # 租借车辆
                self.lease_bike()
            elif select == 4:
                # 归还车辆
                self.revert_bike()
            elif select == 5:
                # 退出系统
                print('期待您下次使用！祝您生活愉快！')
                break


# 我们完成了menu()方法，接下来我们完成查询所有车辆信息，完善info_bike方法，为了能够测试类方法，我们还需要在Manage类初始化时添加几辆车。
# 直接运行一下下面代码,观察终端里的效果。
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


class Manage:
    # 定义一个列表，用来存储所有的车辆
    bike_list = []

    def __init__(self):
        bikeA = Bike(1001, 2)
        bikeB = Bike(1002, 2)
        bikeC = Bike(1003, 1)
        self.bike_list.append(bikeA)
        self.bike_list.append(bikeB)
        self.bike_list.append(bikeC)

    # 系统菜单
    def menu(self):
        print("欢迎使用共享单车租借系统\n")
        while True:
            print('1.查询所有车辆\n 2.共享车辆\n 3.租借车辆\n 4.归还车辆\n 5.退出系统\n')
            select = int(input('请输入所选功能对应得数字：'))
            if select == 1:
                # 单车信息
                self.info_bike()
            elif select == 2:
                # 共享单车
                self.add_bike()
            elif select == 3:
                # 租借车辆
                self.lease_bike()
            elif select == 4:
                # 归还车辆
                self.revert_bike()
            elif select == 5:
                # 退出系统
                print('期待您下次使用！祝您生活愉快！')
                break


# 运行一下， 是不是啥都没有？
# 这是为啥？ 还是那个问题，类已经定义结束， 但是还没有实例化啊。 接下来，你通过Manage类实例化对象，然后调用类方法menu() 。
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


class Manage:
    # 定义一个列表，用来存储所有的车辆
    bike_list = []

    def __init__(self):
        bikeA = Bike(1001, 2)
        bikeB = Bike(1002, 2)
        bikeC = Bike(1003, 1)
        self.bike_list.append(bikeA)
        self.bike_list.append(bikeB)
        self.bike_list.append(bikeC)

    # 系统菜单
    def menu(self):
        print("欢迎使用共享单车租借系统\n")
        while True:
            print('1.查询所有车辆\n 2.共享车辆\n 3.租借车辆\n 4.归还车辆\n 5.退出系统\n')
            select = int(input('请输入所选功能对应得数字：'))
            if select == 1:
                # 单车信息
                self.info_bike()
            elif select == 2:
                # 共享单车
                self.add_bike()
            elif select == 3:
                # 租借车辆
                self.lease_bike()
            elif select == 4:
                # 归还车辆
                self.revert_bike()
            elif select == 5:
                # 退出系统
                print('期待您下次使用！祝您生活愉快！')
                break


getbike = Manage()
getbike.menu()


# 下面，我们一一完成这几个功能。
# 第一个功能，查询所有车辆。
# 查询所有车辆，也就是将车辆列表中的信息全部打印出来即可。
# 打印列表？用循环呀。代码就是：
# 代码片段

#单车信息

    def info_bike(self):
        print("所有车辆信息如下：")
        for bike in self.bike_list:
            print(bike)

# 第二个功能， 共享车辆。
共享车辆，也就是把自己的车辆信息添加到平台中。需要接收车辆编号、车辆使用的年限。
代码如下：
代码片段
1


def add_bike(self):
new_NO = int(input('请输入车辆编码'))
new_age = int(input('请输入车辆使用年限'))
new_bike = Bike(new_NO, new_age)
self.bike_list.append(new_bike)
print('车辆共享成功！')

# 在共享车辆 add_bike(self)方法中，通过Bike类实例化了bike对象。参数写法顺序与Bike类中一致。

# 接下来完成第三个功能，租借车辆。
# 我们通过state属性来控制车辆状态，0代表待租借，1表示租借中。
# 好了，下面我们开始完善租借车辆功能。
# 租借车辆
def lease_bike(self):
    lease_NO = int(input("请输入租借的车辆编号"))
    for bike in self.bike_list:
        # 遍历自行车列表，与用户租借的编号进行匹配
        if bike.NO == lease_NO:
            # 如果单车在平台中存在
            if bike.state == 1:
                # 车辆租借中
                print("你来晚了，车被租走了")
                break
            else:
                # 车辆待租借
                print("租借成功，欢迎您使用绿色出行")
                bike.state = 1
                break
        else:
            print('车辆编号输入错误')
            break

# 代码完成了，但是还存在一个问题。
# 我们在租借车辆时，需要对所有车辆循环遍历进行查询。当归还车辆时，也会遇到同样的问题。
# 因此，我们将这个方法抽离出来，即重新定义一个类方法，完成检查车辆编号是否在车辆列表中。
class Manage:
    # 定义一个列表，用来存储所有的车辆
    bike_list = []
    NO = int(input("请输入租借的车辆编号"))

    def select_bike(self, NO):
        # 遍历整个自行车列表
        for bike in self.bike_list:
            # 如果存在输入编号与车辆列表中的编号一致
            if bike.NO == NO：
            # 返回该车辆信息
            return bike

 #  整合两个方法
#租借车辆
    def lease_bike(self):
        lease_NO = int(input("请输入租借的车辆编号"))
        res = self.select_bike(lease_NO)
        if res != None:
            if res.state ==1:
                #车辆租借中
                print("你来晚了，车被租走了")
            else:
                #车辆待租借
                print("租借成功，欢迎您使用绿色出行")
                res.state =1
        else:
            print("该车辆不存在")

    def select_bike(self,NO):
        #遍历整个自行车列表
        for bike in self.bike_list:
            #如果存在输入编号与车辆列表中的编号一致
            if bike.NO == NO:
                #返回该车辆信息
                return bike

# 定义类方法select_bike(self,NO): ，调用类方法res = self.select_bike(lease_NO)。


# 第四个功能：归还车辆。
# 归还车辆与租借车辆功能类似，也是需要调用select_bike(self,NO)方法。
	#归还车辆
    def revert_bike(self):
     	#输入归还车辆的编号
            revert_NO = int(input("请输入归还的车辆编号"))
      	#进行查询
            res = self.select_bike(revert_NO)
         	#车辆存在
            if res != None:
       	#租借中，还车成功
                if res.state ==1:
                    	#还车成功
                    print("还车成功，期待下次使用")
                    res.state = 0
       		#未租借，等待租借
                else:
                    	#车辆等待租借
                    print("车辆整备完成，等待租借")
      		#车辆不存在
            else:
                print("该车辆不存在,想必您是输错了")



