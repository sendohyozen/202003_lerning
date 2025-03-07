# 模块的定义
# 今天我们学习一下模块，这个就是江湖中争夺的储物戒指，因为它比函数、类强大很多，能够封装更多的功能代码。
# 用句专业术语来讲: 模块是最高级别的程序组织单元，它将程序代码和数据封装起来以便重用。也就是模块可以封装任何数据、代码。
# 每一个后缀名为.py的文件都是模块。
# 模块作用就是将数据、代码封装起来，以便再使用。模块不仅仅我们自己使用，也可以把它给别人使用，就像传递文件一样那么简单。

# 方式一:使用自己的模块
# 建立模块，就是建立.py文件。在其中一个.py文件中引入另一个.py文件。

# import语句
import mytest  # 导入mytest模块

print(mytest.strtest)  # 打印mytest模块中变量strtest

mytest.hello()  # 运行mytest模块中函数hello()

shaonian = mytest.Test()  # mytest模块中Test类的实例化
print(shaonian.strClass)  # 打印实例属性
shaonian.go()  # 调用实例方法go方法

# 在main.py文件中，使用其他模块的代码需要注意: 模块名.变量or函数or类；实例化后，调用类的属性or方法不需要加模块名

# import还有另外一种用法，就是import…as… 先看一下下面例子。
import mytest as ts
print(ts.strtest) #打印mytest模块中变量strtest

ts.hello()        #运行mytest模块中函数hello()

shaonian = ts.Test()   #mytest模块中Test类的实例化
print(shaonian.strClass)   #打印实例属性
shaonian.go()       #调用实例方法go方法
# 如果你嫌mytest名字太长，就可以使用import…as…语句，可以将mytest的名字变成ts，这样在后面需要使用mytest模块名的地方，就可以换成ts名字使用。
# 还有，当我们需要导入多个模块时，我们可以使用逗号，将模块名隔开。
# 例如: import x,y,z 就是将X.py文件，Y.py文件，Z.py文件同时引入。


# from … import … 语句
# from…import…语句可以将某一模块的部分代码导入到另一个模块中。
from mytest import hello
from mytest import strtest
print("*"*50)
hello()
print(strtest)
# 我们将mytest.py文件中的变量与函数引导main.py中使用，这样使用时无需加入”模块名”前缀。
# 可以简写成: from mytest import hello,strtest

# if __name__ == '__main__'
# Python与其他语言一样，程序都要有一个运行入口。当我们运行某个py文件时，就能启动整个程序。那么这个py文件就是程序的入口。
# 当我们有很多py文件在一个程序中，但是你只能指定一个程序入口。这样你就需要使用if __name__ == '__main__':来指定某个py文件为程序入口。
# 第一种情况：加上这一句代码，程序和原来一样：
print("*"*50)
import mytest #导入mytest模块
if __name__ == '__main__':
    print(mytest.strtest)  # 打印mytest模块中变量strtest

    mytest.hello()  # 运行mytest模块中函数hello()

    shaonian = mytest.Test()  # mytest模块中Test类的实例化
    print(shaonian.strClass)  # 打印实例属性
    shaonian.go()  # 调用实例方法go方法

# 运行first.py代码，你会发现，只能输出”我是a模块”。
# 这是因为，此时mian.py文件已经不再是程序的入口。
# main.py文件导入到了first.py文件中，first.py文件运行的时候，只会执行mian.py文件中本身代码，不会执行if __name__ == '__main__':后面的代码。
print("*"*50)
import main



# 方式二：使用他人的模块
import time
print("hello")
time.sleep(3)
print("python")

import random
num = random.randint(1,30)  # 随机从1-30之间抽取一个数字
print(num)

# 探究他人模块
# 自学模块

# 学习CSV模块
import csv

with open("mytest.csv",encoding='utf-8-sig')  as r:
    print("内容如下\n")
    reader = csv.reader(r)
    # 使用csv的reader()方法，创建一个reader对象
    for content in reader:
    #遍历reader对象的每一行
        print(content)

print("读取完毕！")


# 写入
import csv
with open("mytest1.csv",'a')  as r:
    writer = csv.writer(r)
    writer.writerow([41,42,43])
print("写入完毕！")
# writer是实例化对象，writerow()是写入的方法,括号内的数据是列表形式。


















