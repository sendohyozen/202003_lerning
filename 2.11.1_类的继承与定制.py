# 类的基本使用。
class Musician:    #创建类
    glasses = "墨镜"   #创建类属性

    def __init__(self,city):  #创建初始化方法
        self.city = city      #赋值属性
        print('组织语言中……')

    def intr(self):      #创建类方法
        print('我来自%s' % self.city)

hebe = Musician('中国台湾')  #类实例化对象
print(hebe.glasses)
hebe.intr()   #调用类方法

# 类的继承
# 用一句话让计算机知道 X类属于Y类，在Python江湖中的行话就是“X类继承了Y类”。

# 类的继承语法
class Musician:
    glasses = "墨镜"
    loveMusic = True

    def sing(self):
        print('我在唱歌')
class Rapper(Musician):
    pass # pass表示'跳过'，不执行其他操作
mcHotdog = Rapper()
print(mcHotdog.glasses)
mcHotdog.sing()
# 看到没? 实例mcHotdog(热狗)是通过Rapper这个类创建的实例，却调用了Musician这个类中的glasses属性与sing()方法。
# 这是为什么呢？就是因为class Rapper(Musician)这一句，使得Rapper继承了Musician，这样Rapper类就具有了Musician类的属性与方法。
# 通过一个小括号，就能让子类一夜暴富，拥有了父类所拥有的一切。

#补全代码
class Car:
    wheel = 4
    def run(self):
        print('有%d个轮子,可以飞速的行驶'%self.wheel)
class BMW(Car):
    pass
BMW530 = BMW()
print('*'*40)
print(BMW530.wheel)
BMW530.run()
# 但是，好多类，在创建的时候没有括号啊，就像class Car: ，难道Car这个类没有父类吗？
# 其实Car也是有父类的。当创建的类没有小括号时，这个类的父类就是Object。
# Object是所有类的父类，称其为根类。(说白了，就是所有类的祖宗)


# 我们使用Python的一个法宝，isinstance()函数来判断一下某个实例是否属于某个类。
print('*'*40)
BENZ600 = Car()  #使用Car类创建奔驰600
BMW320 = BMW()   #使用BMW类创建BMW320
print("验证:子类创建的实例也属于父类")
print(isinstance(BENZ600,Car))
print(isinstance(BMW320,Car))
print("验证:父类创建的实例不属于不属于不属于子类")
print(isinstance(BENZ600,BMW))
print("验证:所有类创建的实例都属于根类")
print(isinstance(BENZ600,object))
print(isinstance(BMW320,object))
# 江湖秘籍: 类的继承中，子类属于父类；子类创建的实例也属于父类。

# 多层继承
# 就说乾隆皇帝吧， 乾隆皇帝继承了雍正皇帝的皇位， 继承了雍正的财产；可是， 雍正留下的财产中，还有一些是康熙帝留下的， 这样乾隆皇帝不仅仅继承了雍正皇帝的财产， 也继承了康熙皇帝的财产。
# 也就是说，子类不仅仅可以继承父类， 还可以继承父类的父类、父类的父类的父类……
#明星类
class Star:
    glasses = "墨镜"

#音乐人继承了明星
class Musician(Star):
    loveMusic = True

# Rapper继承了音乐人
class Rapper(Musician):
    pass

csunYuk = Rapper()
print(csunYuk.glasses)
print(csunYuk.loveMusic)
# 在这个例子中，实例csunYuk是类Rapper创建， 它可以调用父类Musician的属性，也可以调用父类的父类Star的属性。
# 子类可以调用父类的属性与方法，也可以调用父类的父类的属性与方法。这就是多层继承。

# 多重继承
# # 一个类可以继承多个类， 语法是class Z(X,Y) 。
# 比如我们将“说唱家”定义成一个类Rapper，它继承于音乐人与演说家两个类。 那么它的语法就是 class Rapper(Musician，Orator)。
# Rapper是Musician的子类，也是Orator的子类。
# class Rapper(Musician，Orator)括号内的父类是有顺序区别的， 与子类Rapper关系更近的父类放在左边。 也就是Rapper类与父类Musician更为相似。
#音乐人
class Musician():
    loveMusic = True
    def intr(self):
        print("我喜欢音乐")
        print("我来自音乐界")
#演说家
class Orator():
    speak = "流利的说"
    def intr(self):
        print("我喜欢演说")
        print("我来自演讲界")
# Rapper继承了音乐人与演说家
class Rapper(Musician,Orator):
    pass

csunYuk = Rapper()
print(csunYuk.loveMusic)
print(csunYuk.speak)
csunYuk.intr()
# csunYuk继承了父类Musician的属性loveMusic，也继承了父类Orator的属性speak；
# 当两个父类都具有intr()类方法时，它会优先继承左边的父类，也就是父类Musician的方法。
# 江湖秘籍: 多重继承中， 子类继承于多个父类的属性与方法， 但是优先继承于左边父类的属性与方法。

# 类的定制
# 说唱家除了继承音乐人的属性与方法外，它还创建了自己独有的属性与方法，比如说唱家喜欢饶舌(属性)，还能够作词(方法)。
# 甚至，说唱家还可以改变继承到的属性或方法，比如说唱家唱歌的时候会加进一些演说词。
# 这些操作，都可以说是说唱家在继承的基础上进行定制。
# 也就是说，子类可以在继承父类的基础上进行定制: 可以创建新属性、新方法；也可以改变继承到的属性或方法。

# 定制，新增代码
#音乐人
class Musician():
    loveMusic = True
    def intr(self):
        print("我喜欢音乐")
        print("我来自音乐界")
    def sing(self):
        print("我在唱歌")
# Rapper继承音乐人
class Rapper(Musician): #类的继承
    garrulous = True    #类的定制 ， 增加属性
    def composition(self):  #类的定制， 增加方法
        print("我可以创作简单的歌词")

csunYuk = Rapper()
print(csunYuk.loveMusic)
print(csunYuk.garrulous)
csunYuk.composition()


# 除此之外，还有一种方式：更改父类代码。
# 定制，更改代码
# 重写代码，就是在子类中，对父类的属性或者方法进行修改。
#音乐人
class Musician():
    loveMusic = True
    def intr(self):
        print("我喜欢音乐")
        print("我来自音乐界")
    def sing(self):
        print("我在唱歌")
# Rapper继承音乐人
class Rapper(Musician): #类的继承
    def sing(self):  #类的定制， 更改方法
        print("我以说的形式进行歌唱")

csunYuk = Rapper()
csunYuk.sing()
# csunYuk是通过 Rapper实例化的对象， Rapper类继承Musician类，自然会继承Musician类的方法sing；
# 但是Rapper类将sing方法进行改写，造成csunYuk.sing()运行结束后， 打印的结果是“我以说的形式进行歌唱”
# 这就是类的定制，在继承父类的基础上，又可以进行改变。
