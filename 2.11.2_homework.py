# 每个人都有多重身份，
# 比如说一个学生， 他在学校里的身份就是学生，进行学习；
# 回到家里，他的身份就是儿子，需要照顾父母；
# 他不仅有着学生的属性与方法，还有着儿子的属性与方法。


# 创建一个学生类，拥有属性（stu_no学号），方法（study,会使用Python语言）
# 创建一个孩子类，拥有属性（status身份），方法（care，照顾父母）
# 创建一个儿子类，继承于学生类与孩子类， 拥有两个类的属性与方法
class student():
    stu_no = '学号'
    def Study(self):
        print('会使用Python语言')

class child():
    status = '身份'
    def care(self):
        print("照顾父母")

class son(student, child):
    pass

xiaoMing = son()
print(xiaoMing.stu_no)
print(xiaoMing.status)
xiaoMing.Study()
xiaoMing.care()


# # 中西兼备的厨师
# 题目要求
# 有一个徒弟厨师，跟着师父学做煎饼果子，师父教给徒弟做传统的煎饼果子，与台湾手抓饼；
# 徒弟在学习后又出国深造了几年，不仅仅能做手抓饼，还可以做中西方口味融合的煎饼果子。
#
# 题目讲解
# 创建一个师父类master，这个类中具有两个方法；一个方法叫cake，cake方法可以制作手抓饼，
# 一个方法叫cook，cook方法可以制作传统的煎饼果子。而徒弟类继承了师父的cake方法，可以制作手抓饼，也继承了师父的cook方法，
# 但是徒弟进行改进，可以制作中西方口味融合的煎饼果子。

print("#"*20)

class master():
    def cake(self):
        print("制作手抓饼")
    def cook(self):
        print("制作传统的煎饼果子")

class student(master):
    def cook(self):
        print("制作中西方口味融合的煎饼果子")

laoZhang = master()
laoZhang.cake()
laoZhang.cook()

xiaoLi = student()
xiaoLi.cake()
xiaoLi.cook()