strtest = '驭风少年'

def hello():
    intro = "你好,我是驭风少年函数"
    print("hello函数正在运行")

class Test:
    strClass = "我是类,我是驭风少年"
    def go(self):
        print("类在运行")

print(strtest) #打印变量strtest

hello()        #运行函数hello()

shaonian = Test()   #Test类的实例化
print(shaonian.strClass)   #打印实例属性
shaonian.go()       #调用实例方法go方法


# 这是一段测试

# 这是测试2

# 这是测试3

# 这是测试4