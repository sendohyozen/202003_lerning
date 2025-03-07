# 字符串
# 字符串类型必须有引号。字符串没有引号，就会向你吐槽的。
movie = '美国队长2'
name = 'The Winter Soldier'
price = "7.14"
word = '''≡(▔﹏▔)≡'''
print(movie)
print(name)
print(price)
print(word)

# 整数
# 常见的数据类型第二种：整数， 英文为integer， 简称int。
# Python江湖的整数和我们现实数学中定义的一样：整数是正整数、零和负整数的统称。说白了，就是没有小数点的数字。
age = 18
height = 192
weight = 80
# 打印整数
print(521)
# 以下报错
# num=老铁666
# print(num)

# 浮点数
# Python江湖中，将带有小数点的纯数字定义为浮点数。 它是我们从常见的数据类型之一。
print(0.35+0.11)

# 数学运算
print(999.99*56-103*50)
print((55+22)*99+(38-21)*10)

# 字符串的拼接
hero = '美国队长'
title = '漫威漫画'
action = '取材于'
print(hero+action+title)

# 只有字符串与字符串才能拼接。
# name = '美国队长'
# num= 2
# print(name+num)

# 数据类型的查询—type()函数
name = '美国队长'
num = 2
print(type(name))
print(type(num))

# 数据转换
# str()
name = '美国队长'
num = 2
print(name+str(num))

name = '美国队长'
add = '的'
height = '身高'
gaodu = 198
print(name+add+height+str(gaodu))

# int()函数
# 可以将其他类型的数据转换成整数类型，像str()一样，你只需要将转换的数据放进int()中。
# 只有字符串中的内容是纯数字时，才能够使用int()函数进行强制转换
num1 = '3'
num2 = '6'
print(int(num1)+int(num2))

# 江湖秘籍: 浮点类型的字符串是无法使用int()进行数据转换的。
# print(int('9.9')) # 虽然浮点形式的字符串不能使用int()函数转换, 但是浮点数是可以使用int()函数来转换的。
print(int(9.9))  # int()函数的本质是将数据转换整数，对于浮点数，就是取整处理，也就是只拿走整数部分。 不会做四舍五入操作。


# float()函数
# float()函数可以将整数和字符串转换成浮点数类型，但前提是，这个字符串中的内容一定是数字形式。
height = 198.2
weight = 97
age = '30'
print(float(height))
print(float(weight))
print(float(age))
