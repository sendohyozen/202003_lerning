# 有多个男嘉宾去参加非诚勿扰活动，要在活动上,介绍自己的姓名\年龄与籍贯。
#
# 第二步:分析过程
# 创建一个类叫Maleguests，这个类中具有一个方法叫sayHi，sayHi方法可以介绍自己的姓名\年龄与籍贯。例如“各位女嘉宾好我叫张三，我今年28岁，我来自广州籍贯是可以根据需要改变的。

class Maleguests:
    def __init__(self, name, age, hometown):
        self.name = name
        self.age = age
        self.hometown = hometown

    def intr(self):
        print("各位女嘉宾好我叫%s, 我今年%d岁，我来自%s" %(self.name, self.age, self.hometown))

zhangsan =  Maleguests ("张三",28,"广州")
zhangsan.intr()

Lisi =  Maleguests ("李四",26,"上海")
Lisi.intr()