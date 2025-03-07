# 在今天案例中，我们已经完成了使用Python发送邮件的功能，但是现在邮件发送成功与否，
# 只能通过用户接收到的邮件才能判断；能否增添一个功能，当发送邮件结束后，返回发送成功或发送失败的提示。

# 第二步:分析过程
# 在今天案例中，我们已经完成了使用Python发送邮件的功能，但是现在邮件发送成功与否，
# 只能通过用户接收到的邮件才能判断；能否增添一个功能，当发送邮件结束后，返回发送成功或发送失败的提示。

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# 输入Email地址和口令:
from_addr = input('请输入发件人的邮箱号码From: ')
password = input('请输入发件人的邮箱密码Password: ')
# 输入SMTP服务器地址:
smtp_server = input('请输入邮箱服务器地址SMTP server: ')
# 输入收件人地址:
to_addr_list = []

while True:
    a = input('请输入收件人邮箱：')
    to_addr_list.append(a)
    b = input('是否继续输入，n退出，任意键继续：')
    if b == 'n':
        break
# print(to_addr_list)

content = '''
亲爱的学员朋友：
    你好！
    恭喜大家学习坚持到现在!
    开课吧只为赋能人才，小课让学习更轻松！
'''


def mail():
    ret = []
    try:
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = _format_addr(u'开课吧 <%s>' % from_addr)
        msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
        msg['Subject'] = Header(u'来自小K的问候……', 'utf-8').encode()

        server = smtplib.SMTP_SSL(smtp_server, 465)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        server.quit()
        ret.append(True)

    except Exception:  # 如果try中的语句没有执行，则会执行下面的ret=False
        ret.append(False)

    return ret


for i in range(0, len(to_addr_list)):
    to_addr = to_addr_list[i]
    ret = mail()
    # print(ret)
    if ret:
        print("ok")  # 如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
    else:
        print("filed")  # 如果发送失败则会返回filed
