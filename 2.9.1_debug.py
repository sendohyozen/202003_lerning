while True:
        try:
            age = int(input('你今年多大了？'))
            break
        except ValueError:
            print('你输入的不是数字')
if age < 18:
    print('不可以抽烟喝酒烫头哦')

# 这段代码:
# 1、不知道用户什么时候会输入正确，什么时候会输入错误， 设置while循环来接收输入， 只要用户输入的不是数字就一直循环，用户输入数字后就break跳出循环。
# 2、 使用try…except…异常捕获机制， 用户输入不正确时会一直提示。