# 下面，使用for循环将九九乘法表中的前三行打印出来。
# 我的
for i in range(1,10):
    str_1 = ''  # 初始化，初始化的位置很重要，否则从每个都从1开始放置
    for j in range(1,i+1):  #嵌套循环
        str_1 = str_1 + str(j)+'*'+str(i)+'='+str(i*j)+' '
    print(str_1)

# 课程代码
for i in range(1,2):
    print('%d X %d = %d' % (i, 1, i*1))
for i in range(1,3):
    print('%d X %d = %d' % (i,2,i*2))
for i in range(1,4):
	print('%d X %d = %d' % (i,3,i*3))

# 我们需要的是不让print()打印的时候换行。
# 找百度啊。去百度搜一搜怎么办。
# 搜嘎，原来要想让print()不换行，末尾加end=’’就可以啊。
print('hi',end='')
print('Python')

print('hi',end='  ')
print('Python')

print('hi',end='!')
print('Python')

# 江湖秘籍：使用print(‘’)来控制换行。
for i in range(1,2):
    print('%d X %d = %d' % (i, 1, i*1), end='  ')
print('')
for i in range(1,3):
    print('%d X %d = %d' % (i,2,i*2), end='  ')
print('')
for i in range(1,4):
    print('%d X %d = %d' % (i,3,i*3), end='  ')


# 改成嵌套循环
for i in range(1,10):
    for j in range(1,i+1):
        print( '%d X %d = %d' % (j,i,i*j),end = '  ' )
    print('  ')
