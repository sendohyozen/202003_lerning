# for循环

#叫号
transformers = ['猛大帅' , '铁甲龙','六面兽', '大力金刚', '救护车','红色警戒', '大无畏', '飞天虎','闪电','冲云霄', '计算王','求雨鬼', '守护神','混天豹', '擎天柱', '威震天','惊破天', '红蜘蛛', '巨无霸福特', '雷霆解救队' ]
for i in transformers:
    print(i+'睡了没？')

for i in [1,2,3,4,5,6]:
    print(str(i)+'取钱')
# 在这里我们存放号这个变量叫做i，为什么用i呢？
# 在for循环里， 这个变量的专有名称叫【元素】，英文item，i是它的简称。其实，你可以给这个号码取任意名字。

# 缩进与代码块
for i in [1,2,3,4,5,6]:
    print(str(i)+'取钱')
print(i)

# 一群排队等着取钱的人
# 字典与循环
city  = {'北京':'天安门','上海':'东方明珠','广州':'珠江'}

for i in city:
    print(i)

# 发现i会逐渐接收字典中的每一个【键】
# for in name：这个循环的过程，在python江湖中称为【遍历】

# 如何获得字典的值
city = {'北京':'天安门','上海':'东方明珠','广州':'珠江'}
for i in city:
    print(city[i])

# range()函数
# for循环经常和range()函数一起搭配使用。
for i in range(5):
    print(i)

for i in range(11,15):
    print(i)

for i in range(7):
    print("每天想你第"+str(i)+"遍")

for i in range(0,100,11):
    print(i)

# for循环办事流程
for i in [1,2,3]:
    print(i*3)

# While循环
x = 0
while x < 6:
    x = x+1
    print(x)

# while循环：设定条件
pwd = ''  # 注：这个''代表空字符串
while pwd != '520666':
    pwd = input('请输入银行卡密码：')
print('卡内还有999999999999元~')

# while循环：办事流程
a=0
while a<4:
    a = a+1
print(a) # print(a)这句代码没有缩进，不在while循环中，