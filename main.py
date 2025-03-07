import mytest #导入mytest模块
print("我是a模块")
if __name__ == '__main__':
    print(mytest.strtest)  # 打印mytest模块中变量strtest

    mytest.hello()  # 运行mytest模块中函数hello()

    shaonian = mytest.Test()  # mytest模块中Test类的实例化
    print(shaonian.strClass)  # 打印实例属性
    shaonian.go()  # 调用实例方法go方法