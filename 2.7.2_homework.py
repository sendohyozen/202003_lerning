# 今年业绩不错，KFC餐厅要给员工发奖金，定义一个函数，当输入员工姓名与年限时，打印该员工今年拿多少奖金。
# 奖金规则制定如下： 工作年限<1年的，发1000元奖金; 工作年限≥1年但<3年的，发3000元奖金 工作年限≥3年的，发10000元奖金 比如输入姓名 ‘老王’，年限‘3’；就会打印出“老王你好，今年你拿10000元奖金”。
def bonus(name, years):
    if years < 1:
        money = 1000
    elif years >= 1 and years < 3:  # 可以写成  1<=year<3
        money = 3000
    else:
        money = 10000
    print("%s你好，今年你拿%d元奖金" % (name, money))


name = input("请输入你的姓名：")
years = float(input("请输入你的工作年限："))
bonus(name, years)


# 现在KFC餐厅的奖金激励政策变了，变成如下：
# 1.工作时间＜1年的，发放1000元
# 2.工作年限≥1年但<3年的，发放奖金3000*年数（年数四舍五入，输入时只输入整数）如1年半为 3000*2 = 6000
# 3.工作年限≥3年的，发放奖金5000*年数（年数四舍五入，输入时只输入整数） 如3年为 5000*3 = 15000

# 定义两个函数第一个函数功能为根据工作年数返回奖金额，
# 第二个函数功能为打印出'XX员工来了X年，获得奖金XXX元'。 比如输入姓名 ‘老王’，年限‘3’；就会打印出“老王来了3年，获得奖金15000元”。
def money(years):
    if years < 1:
        money = 1000
    elif 1 <= years < 3:
        money = 3000 * years
    else:
        money = 5000 * years
    return money


def bonus_2(name, years):
    print("%s员工来了%d年，获得奖金%d元" % (name, years,money(years)))


name = input("输入姓名:")
years = float(input("年限:"))
# print(money(years))
bonus_2(name, years)


# 答案
name = input('请输入姓名')
year = int(input('请输入工作年限，数字'))
money=0    # 多设置了初始化
def bonus(year):
   if year<1:
     money = 1000
   elif 1<=year<3:
     money = 3000*year
   else:
     money = 5000*year
   return money

def res(name,year):
   cash = bonus(year) #另外引入一个变量
   print('%s来了%d年,获得奖金%d元' %(name,year,cash))
res(name,year)