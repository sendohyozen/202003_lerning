# 小K的朋友买车需要贷款，贷款的周期按1年、2年、3年、4年、5年进行贷款，不同周期的贷款利率不同，具体利率如下:
# 车贷贷款在贷款生效后，需要每个月（简称：每期）都进行还款，每月还款的金额包含偿还的本息、偿还的本金、偿还的利息。
# 小K 的朋友需要将每期还款情况及最终还款的总额列一个明细出来。


# 这个项目可以分三步走：
# 第一步：用户只需要将贷款金额与贷款年限输入到程序中，就可以自动计算；此两项数据来源于用户。
# 第二步：我们的程序要根据用户的贷款金额与贷款年限进行计算，得到每期数据，含偿还的本息、偿还的本金、偿还的利息。
# 第三步：之后，将所有的数据写入到excel表中。

# 收集用户输入的内容
total_loan = int(input('请输入贷款总额（贷款总额为整数）：'))
total_loan_year = int(input('银行贷款基准利率：1年期6.56%；2年期6.65%；3年期6.65%；4年期6.90%；5年期6.90%；请选择还款年限，输入数字即可：'))

# 计算数据
# 获得计算公式：每项数据的计算中，都需要【月利率】与【还款月数】。
# 月利率
year_rate = 0  # 年利率初始化
if total_loan_year == 1:
    year_rate = 0.0656
elif total_loan_year == 2:
    year_rate = 0.0665
elif total_loan_year == 3:
    year_rate = 0.0665
elif total_loan_year == 4:
    year_rate = 0.0690
elif total_loan_year == 3:
    year_rate = 0.0690
else:
    print("只能选1-5年！")

month_rate = year_rate / 12
# print(month_rate)

# 还款月数
total_months = total_loan_year * 12

# 接下来，我们就可以开始庞大的计算了。
# 在这个程序中，我们需要计算每月还款的金额包含偿还的本息、偿还的本金、偿还的利息。 如果是1年期，就计算1月-12月的数据，如果2年期就计算24个月的。
# 循环计算所有月份的数据
# 累计还款总额计算

sum_money = 0  # 累计还款总额初始化

for i in range(1, total_months + 1):
    print("这是第%d期贷款还款情况：" % i)
    # 每月还款总额
    month_money = total_loan * month_rate * (1 + month_rate) ** total_months / ((1 + month_rate) ** total_months - 1)
    # 每月偿还本金
    month_capital = total_loan * month_rate * (1 + month_rate) ** (i - 1) / ((1 + month_rate) ** total_months - 1)
    # 每月偿还利息
    month_interest = month_money - month_capital
    print("本息为%f，本金为%f，利息为%f" % (month_money, month_capital, month_interest))

    sum_money = sum_money + month_money

print("#" * 50)
# 累计还款总额
print("还款总额为：%f" % sum_money)
# 本金
print("贷款本金为：%f" % total_loan)
# 累计利息
print("累计利息为：%f" % (sum_money - total_loan))

# 太棒了，至此，我们的程序已经将所有的数据都计算出来。接下来，我们就需要考虑将所有的数据写入到excel文件中。
# 写入数据
# 还记得我们之前用Python读写excel吗？调用CSV是最佳选择。

import csv

with open('loan.csv', 'a', newline='', encoding='GBK') as loanlist:
    writer = csv.writer(loanlist, dialect='excel')  # 使用csv.writer（）函数创建writer对象，用于写入
    header = ['期次', '偿还本息（元）', '偿还本金（元）', '偿还利息（元）']  # 列表头部第一行的字段
    writer.writerow(header)
    sum_money = 0  # 累计还款总额初始化

    for i in range(1, total_months + 1):
        print("这是第%d期贷款还款情况：" % i)
        # 每月还款总额
        month_money = total_loan * month_rate * (1 + month_rate) ** total_months / (
                    (1 + month_rate) ** total_months - 1)
        # 每月偿还本金
        month_capital = total_loan * month_rate * (1 + month_rate) ** (i - 1) / ((1 + month_rate) ** total_months - 1)
        # 每月偿还利息
        month_interest = month_money - month_capital
        print("本息为%f，本金为%f，利息为%f" % (month_money, month_capital, month_interest))
        writer.writerow(['第'+str(i)+'期', month_money, month_capital, month_interest])
        # 计算累计还款总额
        sum_money = sum_money + month_money

    # 总计累计总额本金利息
    writer.writerow(['总期次', '还款总额', '贷款本金', '累计利息'])
    writer.writerow([str(total_months)+'期', sum_money, total_loan, sum_money - total_loan])

# 其他需求
# 2.将所有显示金钱的数据，保留2位小数；四舍五入。
# 进行四舍五入，保留2位小数, 使用round()函数 round(month_money,2)