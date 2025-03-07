
# 1. 明确项目目的
# 在编程界，一般都是由产品经理提出项目需求，由程序员来实现。项目需求，大家可以简单的理解为项目效果

# 2. 分析流程，拆解项目
# 理清战斗逻辑
# 根据这些元素，我们要做的主要有三步：
# 1、规定李逍遥和拜月教主的属性。
# 2、双方攻击时，失血量根据对方的攻击来计算。
# 3、如果有一方的血量减少到0以下，GAMEu3000OVER。

# 从第一步开始，设定【李逍遥】和【ＢＯＳＳ】的属性，及【血量】和【攻击力】
print('【李逍遥】血量：100攻击力:25')   # 自定义李逍遥角色的血量和攻击
print('【拜月教主】血量：100攻击力:20')   # 自定义拜月教主角色的血量和攻击

# 第二步，双方攻击人工计算各自剩余血量。
print('李逍遥发起了攻击，【拜月教主】剩余血量75') #人工计算拜月教主剩余血量100-25 = 75
print('拜月教主向李逍遥发起了攻击，【李逍遥】剩余血量80') #人工计算李逍遥剩余血量100-20 = 80

# 第三步，继续攻击，人工计算各自剩余血量。
print('李逍遥发起了攻击，【拜月教主】剩余血量50') #人工计算拜月教主剩余血量75-25 = 50
print('拜月教主向李逍遥发起了攻击，【李逍遥】剩余血量60') #人工计算李逍遥剩余血量80-20= 60

# 第四步，继续攻击，人工计算各自剩余血量。
print('李逍遥发起了攻击，【拜月教主】剩余血量25') #人工计算拜月教主剩余血量50-25= 25
print('拜月教主向李逍遥发起了攻击，【李逍遥】剩余血量40') #人工计算李逍遥剩余血量60-20=40

# 第五步，继续攻击，人工计算各自剩余血量
print('李逍遥发起了攻击，【拜月教主】剩余血量0') #人工计算拜月教主剩余血量25-25=0，此时拜月教主血量为0，拜月教主死亡，游戏结束。
print('拜月教主向李逍遥发起了攻击，【李逍遥】剩余血量20') #人工计算李逍遥剩余血量40-20=20
print('拜月教主死了,李逍遥赢了')

# ，让我们看着结果有进程性，让打印的内容间隔出现，我们引入一个类似“延迟时间”的东西。再Python江湖里，我们需要用到两行代码。
import time #调用time模块

print('【李逍遥】血量：100攻击力:25')   # 自定义李逍遥角色的血量和攻击
print('【拜月教主】血量：100攻击力:20')   # 自定义拜月教主角色的血量和攻击
print('-----------------------')
time.sleep(2)

print('李逍遥发起了攻击，【拜月教主】剩余血量75') #人工计算拜月教主剩余血量100-25 = 75
print('拜月教主向李逍遥发起了攻击，【李逍遥】剩余血量80') #人工计算李逍遥剩余血量100-20 = 80
print('-----------------------')
time.sleep(2)

print('李逍遥发起了攻击，【拜月教主】剩余血量50') #人工计算拜月教主剩余血量75-25 = 50
print('拜月教主向李逍遥发起了攻击，【李逍遥】剩余血量60') #人工计算李逍遥剩余血量80-20= 60
print('-----------------------')
time.sleep(2)

print('李逍遥发起了攻击，【拜月教主】剩余血量25') #人工计算拜月教主剩余血量50-25= 25
print('拜月教主向李逍遥发起了攻击，【李逍遥】剩余血量40') #人工计算李逍遥剩余血量60-20=40
print('-----------------------')
time.sleep(2)

print('李逍遥发起了攻击，【拜月教主】剩余血量0') #人工计算拜月教主剩余血量25-25=0，此时拜月教主血量为0，拜月教主死亡，游戏结束。
print('拜月教主向李逍遥发起了攻击，【李逍遥】剩余血量20') #人工计算李逍遥剩余血量40-20=20
print('-----------------------')
time.sleep(2)

print('拜月教主死了,李逍遥赢了')

# V2 改进 随机属性，自动PK
#多运行几次，看看结果是不是随机生成的~
import random
#调用random模块
# num = random.randint(1,100)
# 随机生成1-100范围内（含1和100）的一个整数，并赋值给变量

# 江湖秘籍：变量命名应使用英文来表达，如果是多个单词，单词与单词之间需要使用英文下划线_来分隔。
import random
freeLi_life = random.randint(100,150)
#表示李逍遥血量
freeLi_attack = random.randint(20,30)
#表示李逍遥攻击
print(freeLi_life)
print(freeLi_attack)

import time
import random
#也可合并写成一行：import time,random

# 生成随机属性
freeLi_life = random.randint(100,150) # “freeLi_life” 代表李逍遥血量
freeLi_attack = random.randint(20,30) # “freeLi_attack” 代表李逍遥攻击
BOSS_life = random.randint(100,150) # “BOSS_life” 代表拜月教主血量
BOSS_attack = random.randint(20,30) # “BOSS_attack” 代表拜月教主攻击

# 展示双方角色的属性
print('【李逍遥】\n'+'血量：'+str(freeLi_life)+'\n攻击：'+str(freeLi_attack))
#freeLi_life和freeLi_attack的数据类型都是整数，所以拼接时需要先用str()转换
print('------------------------')
time.sleep(1)
#暂停一秒再执行后续代码
print('【拜月教主】\n'+'血量：'+str(BOSS_life)+'\n攻击：'+str(BOSS_attack))
print('------------------------')

 # 我们就来实现“自动PK”
# 自动PK阶段
# 自动PK阶段
while(freeLi_life>0) and (BOSS_life>0):
    freeLi_life = freeLi_life - BOSS_attack
    BOSS_life = BOSS_life - freeLi_attack

    print('李逍遥发起了攻击，【拜月教主】剩余血量'+str(BOSS_life))
    #freeLi_life是整数，所以拼接时要先用str()转换
    print('拜月教主向李逍遥发起了攻击，【李逍遥】剩余血量'+str(freeLi_life))
    print('------------------------')
    time.sleep(2)
    # 为了体现出战斗回合，这里停顿2秒

# 打印战果
if freeLi_life > 0 and BOSS_life <= 0:
    print('拜月教主挂了，李逍遥赢了')
elif freeLi_life <= 0 and BOSS_life > 0:
    print('悲催，拜月教主把李逍遥干掉了！')
else:
    print('哎呀，李逍遥和拜月教主同归于尽了！')

# 对比2.0版本，在3.0版本中，我们想要增加的功能是：1、打印战果：每局战斗后，根据胜负平的结果打印出不同的提示。2、三局两胜：双方战斗三局，胜局多的为最终赢家。
# 三局两胜，引入for循环
import time
import random
#也可合并写成一行：import time,random
for i in range(1,4):
    time.sleep(1)  # 让局与局之间有较明显的有时间间隔
    print(' \n——————现在进行第'+str(i)+'局，3，2，1，go!——————')  # 作为局的标记

    # 生成随机属性
    freeLi_life = random.randint(100,150) # “freeLi_life” 代表李逍遥血量
    freeLi_attack = random.randint(20,30) # “freeLi_attack” 代表李逍遥攻击
    BOSS_life = random.randint(100,150) # “BOSS_life” 代表拜月教主血量
    BOSS_attack = random.randint(20,30) # “BOSS_attack” 代表拜月教主攻击

    # 展示双方角色的属性
    print('【李逍遥】\n'+'血量：'+str(freeLi_life)+'\n攻击：'+str(freeLi_attack))
    #freeLi_life和freeLi_attack的数据类型都是整数，所以拼接时需要先用str()转换
    print('------------------------')
    time.sleep(1)
    #暂停一秒再执行后续代码
    print('【拜月教主】\n'+'血量：'+str(BOSS_life)+'\n攻击：'+str(BOSS_attack))
    print('------------------------')

    # 自动PK阶段
    while(freeLi_life>0) and (BOSS_life>0):
        freeLi_life = freeLi_life - BOSS_attack
        BOSS_life = BOSS_life - freeLi_attack

        print('李逍遥发起了攻击，【拜月教主】剩余血量'+str(BOSS_life))
        #freeLi_life是整数，所以拼接时要先用str()转换
        print('拜月教主向李逍遥发起了攻击，【李逍遥】剩余血量'+str(freeLi_life))
        print('------------------------')
        time.sleep(2)
        # 为了体现出战斗回合，这里停顿2秒

    # 打印战果
    if freeLi_life > 0 and BOSS_life <= 0:
        print('拜月教主挂了，李逍遥赢了')
    elif freeLi_life <= 0 and BOSS_life > 0:
        print('悲催，拜月教主把李逍遥干掉了！')
    else:
        print('哎呀，李逍遥和拜月教主同归于尽了！')

# 最后结果记分
if freeLi_life > 0 and BOSS_life <= 0:
        freeLi_score=freeLi_score+1
        print('拜月教主挂了，李逍遥赢了')
    elif freeLi_life <= 0 and BOSS_life > 0:
        BOSS_score = BOSS_score +1
        print('悲催，拜月教主把李逍遥干掉了！')
    else:
        print('哎呀，李逍遥和拜月教主同归于尽了！')


# 最终版
import time
import random

freeLi_score = 0
# 存放李逍遥赢的局数。
BOSS_score = 0
# 存放拜月教主赢的局数

# 也可合并写成一行：import time,random
for i in range(1, 4):
    time.sleep(1)  # 让局与局之间有较明显的有时间间隔
    print(' \n——————现在进行第' + str(i) + '局，3，2，1，go!——————')  # 作为局的标记

    # 生成随机属性
    freeLi_life = random.randint(100, 150)  # “freeLi_life” 代表李逍遥血量
    freeLi_attack = random.randint(20, 30)  # “freeLi_attack” 代表李逍遥攻击
    BOSS_life = random.randint(100, 150)  # “BOSS_life” 代表拜月教主血量
    BOSS_attack = random.randint(20, 30)  # “BOSS_attack” 代表拜月教主攻击

    # 展示双方角色的属性
    print('【李逍遥】\n' + '血量：' + str(freeLi_life) + '\n攻击：' + str(freeLi_attack))
    # freeLi_life和freeLi_attack的数据类型都是整数，所以拼接时需要先用str()转换
    print('------------------------')
    time.sleep(1)
    # 暂停一秒再执行后续代码
    print('【拜月教主】\n' + '血量：' + str(BOSS_life) + '\n攻击：' + str(BOSS_attack))
    print('------------------------')

    # 自动PK阶段
    while (freeLi_life > 0) and (BOSS_life > 0):
        freeLi_life = freeLi_life - BOSS_attack
        BOSS_life = BOSS_life - freeLi_attack

        print('李逍遥发起了攻击，【拜月教主】剩余血量' + str(BOSS_life))
        # freeLi_life是整数，所以拼接时要先用str()转换
        print('拜月教主向李逍遥发起了攻击，【李逍遥】剩余血量' + str(freeLi_life))
        print('------------------------')
        time.sleep(2)
        # 为了体现出战斗回合，这里停顿2秒

    # 打印战果
    if freeLi_life > 0 and BOSS_life <= 0:
        freeLi_score = freeLi_score + 1
        print('拜月教主挂了，李逍遥赢了')
    elif freeLi_life <= 0 and BOSS_life > 0:
        BOSS_score = BOSS_score + 1
        print('悲催，拜月教主把李逍遥干掉了！')
    else:
        print('哎呀，李逍遥和拜月教主同归于尽了！')

if freeLi_score > BOSS_score:
    time.sleep(1)
    print('【 大战3个回合：李逍遥赢了！】')
elif BOSS_score > freeLi_score:
    print('【大战3个回合：李逍遥输了！】')
else:
    print('【大战3个回合：平局！】')

# Python为我们提供了一种不同数据类型的拼接方式，使用【格式符%】来处理。
print('【李逍遥】\n血量:%s\n攻击力:%s' %( freeLi_life, freeLi_attack))
print('【拜月教主】\n血量:%s\n攻击力:%s' %(BOSS_life, BOSS_attack))

# 江湖秘籍：【%】后面的类型码用什么，取决于你希望这个【%】占住的这个位置的数据以什么类型展示出来，
# 如果你希望它以字符串形式展示，那就写【%s】，如果你希望它以整数形式展示，那就写【%d】。