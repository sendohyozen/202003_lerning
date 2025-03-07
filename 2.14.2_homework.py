# 第一步:明确目标
# 学习使用time时间模块，计算某个函数执行所用的时间 。
#
# 第二步:分析过程
# 计算函数def test()运行时所需要的时间， 首先在函数执行前打印记录下时间， 函数执行结束后打印记录下时间， 结束时间-开始时间就是函数运行所需的时间。

def test():
    time.sleep(3)


import time

a1 = time.time()
test()
a2 = time.time()
print(a2 - a1)

# 使用Python中的csv模块, 在csv文件中写九宫格
# 题目讲解
# 回顾总结本节课csv的使用方法, 然后通过Python在test.csv文件中写入如下九宫格, 补全practice_csv.py中的代码:
import csv

with open("mytest.csv", 'a')  as r:
    writer = csv.writer(r)
    writer.writerow([41, 42, 43])
    writer.writerow([51, 52, 53])
    writer.writerow([61, 62, 63])

print("写入完毕！")
