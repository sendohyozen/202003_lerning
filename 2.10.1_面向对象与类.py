# 类与对象

# 征途第一站：“类”
# 类：就是多个类似事物组成的群体的统称。类能够帮助我们快速理解和判断事物的归属。
# 直接运行代码
print(type('666'))  # <class'str'>
print(type(6666))  # <class'int'>
print(type([6666]))  # <class'list'>


# 运行上面代码后，我们发现，'666'属于'str'字符串类；6666属于'int'整数类；[6666]属于'list'类。
# 在Python的编程江湖中，每个类都有很多实例。比如520、1314都是整数类；3.1415926、9.85都属于浮点数类；'hi'、'hello'都属于字符串类。
# 在Python的江湖中，我们把类的个例叫做“实际的例子” 简称“实例”。


# 看一下，你对类掌握清楚了吗？ 请问：汽车、BMW汽车、马云的迈巴赫汽车、str、'hello'分别是： A：类、类、类、类、类 B：类、实例、实例、类、实例 C：类、类、实例、类、实例 不好意思，你答错了，选C。
# 汽车属于一个类别；BMW汽车也属于一个类别，虽然它比汽车类小，但是它还有BMW3系5系类别，所以它也属于类；马云的迈巴赫汽车，这就是特指马云的那辆迈巴赫汽车，就是特指，实际举出了，它就是实例；str是字符串类别；’hello
# ’就是一个具体的字符串，它属于实例。


# 一切皆“对象”
# 在Python江湖中，它把所有的事物都称为对象， 对象包含类与实例；也就是说，类叫做对象，实例也叫做对象。比如str是类对象，'hello’就是实例对象。 一切皆对象。

# 创建类与调用类
# 我们都是音乐人
# 羽泉、你、我都是音乐人------这句话，在Python江湖中翻译过来就是: 羽泉、你、我都属于“音乐人”这个类，羽泉、你、我都是“音乐人”这个类中的实例；我们都存在一些相同点：喜欢音乐、艺名、会唱歌、能跳舞。
# 这些共同点，就是我们区别于其他类的依据。其实，我们还可以对这些相同点进行细分：
# 第一种，用来描述事物性质的，比如：喜欢音乐、艺名；
# 第二种，用来描述事物能做什么，比如：会唱歌、能跳舞。

# 在Python江湖中，我们把第一种共同点称为属性(what)，第二种共同点称为方法(how)。
# 比如，我们认识的字符串，属性有：引号，下标；方法有：都可以进行拼接操作。
# Python中，每个类都有自己的独特的属性attribute和方法method，是这个类的所有实例都共享的。换言之，每个实例都可以调用类中所有的属性和方法。

# 类的创建
# 类名称的首字母要大写！！！
class Musician:
    loveMusic = True

    def sing(self):
        print('我在唱歌')


class Star:
    glasses = "墨镜"

    def photo(self):
        print("与粉丝拍照")


# 类的调用
class Musician:
    loveMusic = True

    def sing(self):
        print('我在唱歌')


laoFan = Musician()
print("音乐人老樊")
laoFan.sing()  # 关键在于后三行代码，laoFan = Musician() 这就是通过音乐人这个类创建laoFan这个实例。这个过程叫做类的实例化。


class Musician:
    loveMusic = True

    def sing(self):
        print('我在唱歌')


laoFan = Musician()
print(laoFan)
print(type(laoFan))


# 打印的第一行，<__main__.Musician object at 0x00000215D560FCC0>(备注：at后的内容可能不一致，这属于正常现象，每个人的电脑不同)就是通过Musician这个类创建的laoFan这个实例，这是这个实例在电脑上中的内存地址；
# 第二行说明了laoFan这个实例属于Musician这个类。


# 当laoFan这个实例创造出来之后，它可以调用Musician这个类中的属性与方法。
class Musician:
    loveMusic = True

    def sing(self):
        print('我在唱歌')


laoFan = Musician()
print("音乐人老樊")
print(laoFan.loveMusic)
laoFan.sing()


# 通过print(laoFan.loveMusic)这句代码，打印出了True这个结果。这就是调用类的属性。 首先通过laoFan.loveMusic获取到属性loveMusic的值True，再使用print()函数打印出来。
# 通过laoFan.sing()这句代码，调用了类方法sing()，直接打印出“我在唱歌”。

# 1、调用类属性： 实例名.属性名 2、调用类方法： 实例名.方法名()


# 既然说类是相似实例的统称，那么能不能创建多个实例。
class Musician:
    loveMusic = True

    def sing(self):
        print('我在唱歌')


laoFan = Musician()
print("音乐人老樊")
print(laoFan.loveMusic)
laoFan.sing()
diamond = Musician()
print("音乐人张碧晨")
print(diamond.loveMusic)
diamond.sing()


# 类就像工厂一样，可以通过一条生产线制造多个商品。因此，类也被称为“实例工厂”。

# 创建类的两大要素
# 揭秘self参数
# 首先明确下self的作用：self会在类的实例化中接收传入的数据， 在代码中运行。
class Musician:
    name = '羽泉'

    def sing(self, person):
        print(person + '是音乐人')


singer = Musician()
print(singer.name)
singer.sing('羽泉')


# 只要在sing()方法内部调用类属性，就可以实现同样的功能，没有必要把参数再传递一遍。
class Musician:
    name = '羽泉'

    def sing(self):
        print(self.name + '是音乐人')


singer = Musician()
print(singer.name)
singer.sing()


# 这就是self的独特之处，它的作用就是先在类方法中占一个位置，当实例创建调用类方法的时候，它就会将self.name也就是类中的name放入方法中，也就会把’羽泉’放入方法中。
# 这就是类方法中调用类属性需要使用self。


# 同理，如果类中的一个类方法需要调用另一个类方法，依然需要使用self。
class Musician:
    name = '羽泉'

    def hello(self):
        print('hello,大家好')

    def sing(self):
        self.hello()
        print(self.name + '是音乐人')


singer = Musician()
singer.sing()


# 江湖秘籍：类方法中调用类内部属性或者是其他方法时，需要使用self来代表实例。


# 下面，我们看一下创建类的另一个要素，初始化方法。
# 每个类中都存在一个初始化方法，这个方法不需要调用，在通过类创建实例对象的时候初始化方法会自动执行。
# 定义初始化方法：def __init__(self): ，init两边是双下划线。

class Musician:
    def __init__(self):
        print('你好,这里是初始化方法init')


liRongHao = Musician()


# 是不是很神奇？我们创建了liRongHao = Musician() 这个实例，init初始化方法就自动执行了。
# 利用init初始化方法的特点，我们可以在初始化方法中完成类属性的创建及类属性的赋初值。
class Musician:
    def __init__(self):
        self.glass = "墨镜"
        self.microphone = "many"

    def intr(self):
        print('我出门必须戴%s' % self.glass)
        print('我有%s个麦克风' % self.microphone)


silence = Musician()
silence.intr()


# 初始化方法中，除了可以设置固定值之外，还可以接收其他参数，使得传入的数据灵活多变。
class Musician:
    def __init__(self, name, anotherName, music):
        self.name = name
        self.anotherName = anotherName
        self.music = music

    def intr(self):
        print('各位歌迷好,我是%s' % self.name)
        print('熟悉我的朋友都叫我%s' % self.anotherName)

    def sing(self):
        print('我为大家唱一首%s' % self.music)


jam = Musician('萧敬腾', '雨神', '王妃')
jam.intr()
jam.sing()
# 在这里我们通过init初始化方法，传入多个参数。
# __init__(self,name,anotherName,music)与Musician('萧敬腾','雨神','王妃')。
# 大家会发现，定义初始化方法中，拥有self,name,anotherName,music四个参数，在类创建实例的时候，只传入了三个参数。
# 这是因为self属性只会在方法创建的时候出现，方法调用时就不需出现了。
# 因此下面的类方法会通过self.属性名一一获取传入的数据。
# 这就是初始化方法init的使用。


# 面向对象编程
# 面向对象编程与之前面向过程编程是有很大的区别。
# 在之前的面向过程编程，我们需要分析出解决问题的步骤，及首先干什么，然后干什么，最后干什么；

# 而面向对象编程，会将程序看成是对象的集合(一切皆对象)。
# 面向对象编程，不考虑实现功能的步骤；而是考虑实现这个功能需要设计什么样的类，这个类中有哪些属性和方法。
# 然后，通过这个类创建一个实例对象，让对象来调用类属性与类方法。

# 快递配送调配小程序：
import math


class Program:
    def __init__(self):
        self.key = 1

    # 工时计算
    def BOSS_input(self):
        # 设置默认参数
        self.types = int(input('请选择需要计算的工作：1-配送次数计算，2-快递员数计算，请选择'))
        self.sizes = float(input('请输入项目大小：1代表标准，还可以输入其他倍数或小数'))
        if self.types == 1:
            self.others = int(input('请输入投入的快递员数，请输入整数'))
        else:
            self.others = int(input('请输入快递次数，请输入整数'))

    # 计算工作量
    def calculate_job(self):
        print('计算结果如下')
        if self.types == 1:
            # 工时计算过程
            self.num = math.ceil(round((self.sizes * 100 / 20 / self.others), 2))
            print('%.1f个标准集装箱大的快递项目，使用%d位快递员配送，则需要配送次数%d次' % (self.sizes, self.others, self.num))
        elif self.types == 2:
            # 人力计算过程
            self.person = math.ceil(round((self.sizes * 100 / 20 / self.others), 2))
            print('%.1f个标准集装箱大的快递项目，%d次配送完毕，则需要快递员数：%d位' % (self.sizes, self.others, self.person))

    def again(self):
        num = input('是否继续计算？继续请输入y，输入其他键将结束程序。')
        if num != 'y':
            # 如果用户不输入'y'，则把key赋值为0
            self.key = 0

    def res(self):
        print('欢迎BOSS使用配送计算小程序')
        while self.key == 1:
            self.BOSS_input()
            self.calculate_job()
            self.again()
        print('工作辛苦。')


pro = Program()
pro.res()