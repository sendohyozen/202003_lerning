

# 单向判断：if
# 为钱包赋值
money = 1000

# 条件：如果有1000块钱以上(包含1000块)，就去吃日料
if money >= 1000:
    # 结果：显示‘你去吃日料’的结果
    print('金刚狼带凤凰女去吃日料')

# 江湖秘籍：在编程武林中，空格不叫空格，而是叫缩进。就如同我们写报告一样，每段开始都要空两格。
# 对于Python而言，缩进是一种语法规则，它会帮助Python更好的分清代码结构与层次，计算机更好的执行Python代码。
# 【注：缩进是四个空格或一个Tab键】
# 在if条件语句中，缩进是不需要手动按空格的。当你用英文输入法打:后按回车，
# 我们的开发工具（用来编写Python代码的程序）为了方便大家编程，会自动实现下一行代码，向右缩进的功能。
# 此时，被缩进的所有内容被称为if语句内的代码块。


# 双向判断：if…else…
# 为钱包赋值
money = 1000

# 条件：如果有1000块钱以上(包含1000块)，就去吃日料
if money >= 1000:
    print('金刚狼带凤凰女去吃日料')

# 条件：当不满足if条件，执行else条件下语句
else:
    print('金刚狼带凤凰女去吃KFC')


# 多向判断：if…elif…else…
# 为钱包赋值
money = 999

# 条件：如果有1000块钱以上(包含1000块)，就去吃日料
if money >= 1000:
    print('金刚狼带凤凰女去吃日料')
# 条件：如果有800-1000块钱之间(包含800块)
elif money >= 800:
    print('金刚狼带凤凰女去吃披萨')
# 不满足条件
else:
    print('金刚狼带凤凰女去吃KFC')

# if嵌套
# if嵌套使用的场景是：在满足基础条件的情况下，在观察是否满足其他额外条件。
contribution=860

if contribution>=600:
    print('特种作战人员')

    if contribution>=800:
        print('王者')

    else:
        print('黄金')

else:
    print('普通作战人员')

    if contribution>400:
        print('白银')

    else:
        print('青铜')

print('结束')


