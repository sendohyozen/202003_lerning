# input()函数依然是向用户询问，“请输入你喜欢人的名字”，用户在终端中输入内容，
# 无论输入什么内容，这个内容都将会赋值给name这个变量，此时name这个容器里面存储的就是用户输入的内容。
name = input('请输入你喜欢人的名字：')
print(name)

name = input('请输入你喜欢人的名字：')
print(name+'I love you')


# input()函数的数据类型
name = input('请输入你喜欢人的名字：')
print(type(name))
hobby = input('她喜欢1.逛街，2.旅游，3.美食。输入数字：')
print(type(hobby))

# 江湖秘籍：不管输入的回答是什么, 不管输入的是整数1234，还是字符串，input()函数的输入值，都会被强制性的转换为字符串类型。
hobby = input('她喜欢1.逛街，2.旅游，3.美食。输入数字：')
hobby = int(hobby)
if hobby ==1:
     print('拿我的卡，使劲花')
elif hobby==2:
     print('带你去浪漫的土耳其，还有东京和巴黎')
else:
     print('吃嘛嘛香')