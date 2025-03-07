# 第一步:明确目标
# 改造今天代码，可以群发软件。
#
# 第二步:分析过程
# 在今天Python发送邮件的案例中， 我们目前收件邮件只能写一个，远远还不能达到要求。
# 有没有办法，在输入一个收件邮箱结束后，弹出输入框询问用户是否需要继续输入邮箱，如果需要输入收件邮箱，按其他按键继续；如果不再需要输入收件邮箱，那直接按n退出，开始发送邮件。


from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

# 接受Email


# 发送邮件
# 创建空列表
from_addr = []
password = []
smtp_server = []
to_addr = []

while True:
    choice = input('请选择是否继续输入邮箱地址。按n退出： ')
    if choice != 'n':
        # 添加列表信息
        # 输入Email地址和口令:
        from_addr.append(input('请输入发件人的邮箱号码From: '))
        password.append(input('请输入发件人的邮箱密码Password: '))
        # 输入SMTP服务器地址:
        smtp_server.append(input('请输入邮箱服务器地址SMTP server: '))
        # 输入收件人地址:
        to_addr.append(input('请输入收件人邮箱地址To: '))
    else:
        break

# 调试，查看列表信息
# print(from_addr)
# print(password)
# print(smtp_server)
# print(to_addr)


# 构造表头格式化函数
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( Header(name, 'utf-8').encode(), addr))

content = '''
亲爱的学员朋友：
    你好！
    恭喜大家学习坚持到现在!
    开课吧只为赋能人才，小课让学习更轻松！
'''

i = len(from_addr)
# print(i)
for i in range(0, i):
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = _format_addr(u'开课吧 <%s>' % from_addr[i])
    msg['To'] = _format_addr(u'管理员 <%s>' % to_addr[i])
    msg['Subject'] = Header(u'来自小K的问候……', 'utf-8').encode()

    server = smtplib.SMTP_SSL(smtp_server[i], 465)
    server.set_debuglevel(1)
    server.login(from_addr[i], password[i])
    server.sendmail(from_addr[i], [to_addr[i]], msg.as_string())
    server.quit()





