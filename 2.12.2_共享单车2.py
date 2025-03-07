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
            print(' 1.查询所有车辆\n 2.共享车辆\n 3.租借车辆\n 4.归还车辆\n 5.退出系统\n')
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
        # 单车信息

    def info_bike(self):
        for bike in self.bike_list:
            print(bike)

    # 共享单车
    def add_bike(self):
        new_NO = int(input('请输入车辆编码'))
        new_age = int(input('请输入车辆使用年限'))

        new_bike = Bike(new_NO, new_age)
        self.bike_list.append(new_bike)
        print('车辆共享成功！')

    # 租借车辆
    def lease_bike(self):
        lease_NO = int(input("请输入租借的车辆编号"))
        res = self.select_bike(lease_NO)
        if res != None:
            if res.state == 1:
                # 车辆租借中
                print("你来晚了，车被租走了")
            else:
                # 车辆待租借
                print("租借成功，欢迎您使用绿色出行")
                res.state = 1
        else:
            print("该车辆不存在")

    def select_bike(self, NO):
        # 遍历整个自行车列表
        for bike in self.bike_list:
            # 如果存在输入编号与车辆列表中的编号一致
            if bike.NO == NO:
                # 返回该车辆信息
                return bike

    # 归还车辆
    def revert_bike(self):
        # 输入归还车辆的编号
        revert_NO = int(input("请输入归还的车辆编号"))
        # 进行查询
        res = self.select_bike(revert_NO)
        # 车辆存在
        if res != None:
            # 租借中，还车成功
            if res.state == 1:
                # 还车成功
                print("还车成功，期待下次使用")
                res.state = 0
            # 未租借，等待租借
            else:
                # 车辆等待租借
                print("车辆整备完成，等待租借")
        # 车辆不存在
        else:
            print("该车辆不存在,想必您是输错了")


user = Manage()
print(user)
user.menu()