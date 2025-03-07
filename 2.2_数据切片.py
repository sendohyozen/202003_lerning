# 两种新的数据类型——列表和字典
# 列表

# 1.1什么是列表
list = ['李雷','韩梅梅',180,3.5]
print(list)

# 你会发现，列表的胸怀很宽广， 各种类型的数据（字符串、整数、浮点数）都能放在里面。

# 1.2从列表中提取单个元素
transformers = ['擎天柱','大黄蜂','救护车']
print(transformers[1])

# 1.3从列表中提取多个元素。
transformers = ['擎天柱','大黄蜂','救护车','巨无霸福特','红蜘蛛']

print(transformers[:])

print(transformers[2:])

print(transformers[:2])

print(transformers[1:3])

print(transformers[2:4])

# 这种通过冒号来截取列表元素的操作叫切片，就是将列表的某个片段，通过切割下标的方式来提取多个元素。
# 【江湖秘籍：冒号左边空，就要从下标为0的元素开始取。右边空，就要取到列表的最后一个元素。
#  后半句：冒号左边数字对应的元素要拿，右边的不动。】

# 1.4给列表添加/删除元素
# 增加
transformers = ['擎天柱','大黄蜂','救护车','巨无霸福特','红蜘蛛']

transformers.append('萨克巨人')

print(transformers)

# 删除
transformers = ['擎天柱','大黄蜂','救护车','巨无霸福特','红蜘蛛']

del transformers[2]

print(transformers)


# 数据类型：字典
# 2.1什么是字典
transformers = ['擎天柱','大黄蜂','救护车','巨无霸福特','红蜘蛛']

fc = { '擎天柱': 95 ,'大黄蜂':90 ,'救护车':86, '巨无霸福特':80,'红蜘蛛':80  }
# 字典的元素由键与值组成，组成形式 键:值，冒号还是英文的冒号。'擎天柱': 95， 我们把'擎天柱'称为键，把95称为值。
# 这样键:值的形式，我们统称为键值对。那么，fc这个字典里有5个键值对 ： '擎天柱': 95、'大黄蜂':90、'救护车':86、 '巨无霸福特':80、'红蜘蛛':80。

# 如果你不想查， 你还可以使用len()函数来得到字典或列表的长度。len()函数括号里放字典或列表的名字。
transformers = ['擎天柱','大黄蜂','救护车','巨无霸福特','红蜘蛛']

fc = { '擎天柱': 95 ,'大黄蜂':90 ,'救护车':86, '巨无霸福特':80,'红蜘蛛':80  }

print(len(transformers))

print(len(fc))

# 2.2 从字典中提取元素
fc = { '擎天柱': 95 ,'大黄蜂':90 ,'救护车':86, '巨无霸福特':80,'红蜘蛛':80  }
print(fc['擎天柱'])

# 2.3给字典增加/删除元素
fc = { '擎天柱': 95 ,'大黄蜂':90 ,'救护车':86, '巨无霸福特':80,'红蜘蛛':80  }

del fc['巨无霸福特']

print(fc)

fc['巨无霸福特'] = 50

print(fc)

fc = { '擎天柱': 95 ,'大黄蜂':90 ,'救护车':86, '巨无霸福特':80,'红蜘蛛':80  }
fc['铁皮'] = 90
print(fc)