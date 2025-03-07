# 用数据做判断：布尔值
# 在while循环之前，我们学过if…elif…else语句，这其中也涉及到用数据做判断。
# 但是，if语句中的条件与while语句中的条件有区别：if语句中的条件只判断一次，while语句中的判断会一直循环执行。

# 用数据做判断：布尔值
while False:
    print('我是Fasle,打印不出来')

print(3<6)
print(3>6)
print('北京'=='北京')
print('北京'=='首都')

print('以下数据判断结果都是【真】：')
print(bool(True))
print(bool(10))
print(bool('xyz'))

print('以下数据判断结果都是【假】：')
print(bool(False))
print(bool(0))
print(bool(''))
print(bool(None))

# 布尔值之间的运算
# 你会接触到and、or、not、in、not in五种运算。
# 请先阅读代码，然后直接运行
a = 5
b = -5

print('以下是and运算')
if a==5 and b==5:    # 【b实际上是-5】
    print('True')
else:
    print('False')

print('以下是or运算')
if a==5 or b==5:  # 【b实际上是-5】
    print('True')
else:
    print('False')


list = [1,2,3,4]
a = 1
b = 10
c = 0
print(bool(a in list))
print(bool(b in list))
print(bool(c in list))

# break语句
# break语句的意思就是“打破”，在Python江湖中用来结束循环的。
# 注意好缩进哦。
for i in range(1,10):
    if(i>5):
        break
    print(i)

x = 0
while x<10:
    if(x>4):
        break
    x=x+1
    print(x)

# continue语句
# continue的意思是“继续”。这个语句也是在循环内部使用的。当某个条件被满足的时候，触发continue语句，结束本次循环, 从下一次循环继续执行。
for i in range(1,11):
    if i==5:
        continue
    print(i)

x = 0
while x<10:
    x=x+1
    if x==5:
        continue
    else:
        print(x)

# pass语句
age = int(input('请输入你的年龄:'))
if age >= 18:
    pass
else:
    print('你未成年，不得进入网吧')

# 这个代码的意思是：当age>=18的时候，跳过，什么都不做。其他情况age<18的时候，执行 print('你未成年，不得进入网吧')语句。
# pass语句就是占据一个位置“什么都不做”，满足我的条件，就跳过。

# else语句
# else语句不仅能够在if语句中使用，还能够和循环搭配使用。
for i in range(3):
    num = int(input('请输入0结束循环，你有3次机会:'))
    if num == 0:
        print('你触发了break语句，导致else语句不会生效。')
        break
else:
	print('3次循环你都错过了，else语句生效了。')


num=0
while num<3:
    n = int(input('请输入0结束循环，你有3次机会:'))
    if n == 0:
        print('你触发了break语句，导致else语句不会生效。')
        break
    num+=1
else:
    print('3次循环你都错过了，else语句生效了。')
