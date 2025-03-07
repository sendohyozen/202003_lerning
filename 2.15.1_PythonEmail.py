# 明确项目目的
# 今天小K带大家搞定一个能够发送邮件的程序, 这样就不用每次都去登录邮箱发送邮件了。

# 分析流程，拆解项目
# 完成简单邮件
# 首先, 来看一下1.0版本。

# 也就是说email模块负责构造邮件；smtplib模块负责发送邮件，这就是这节课要使用的模块解决的问题。
# 江湖秘籍: 使用什么样的模块, 在于你的需求。根据需求要实现的功能,再去采用对应的模块。
# SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
from email.mime.text import MIMEText
import smtplib
msg = MIMEText('hello, Python auto send email', 'plain', 'utf-8')
# 在这里, 我们把email模块与smtplib模块引入进来,我们还使用MIMEText构造了邮件内容。
# MIMEText对象中然后通过SMTP发送邮件出去。
# 现在有了邮件的正文, 但是还缺少, 发件人,收件人; 接下来,我们向用户收集信息。
# 输入Email地址和口令:
from_addr = input('From: ')
password = input('Password: ')
# 输入SMTP服务器地址:
smtp_server = input('SMTP server: ')
# 输入收件人地址:
to_addr = input('To: ')

# SMTP服务器地址，实际上就是代收发服务器地址，是由邮箱服务商提供的。说白了,你用哪家公司的邮箱, 就是哪家公司收发邮件服务器的地址。
# # 在本节课中, 我们编写的程序以QQ邮箱来测试. 我们使用QQ邮箱的收发邮件服务器的地址。
# # QQ邮箱SMTP服务器地址：smtp.qq.com, 端口465, QQ邮箱默认的端口是25, 我们这里使用的是加密端口465。
# # 好了, 接下来我们要开始配置SMTP服务了.
server = smtplib.SMTP_SSL(smtp_server, 465) # SMTP协议加密端口是465
server.set_debuglevel(1)               #调试级
# 用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。

# 好了,接下来我们就要想着发送邮件了, 完成SMTP发送邮件功能
# 代码片段
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
# login()方法用来登录SMTP服务器，参数有两个, from_addr是用户输入的发件邮箱, password是发件邮箱的密码。
# login()方法用来登录SMTP服务器，参数有两个, from_addr是用户输入的发件邮箱, password是发件邮箱的密码。
# sendmail()方法就是发邮件,需要引入三个参数:
# 第一个参数:from_addr是发件人的邮箱地址
# 第二个参数:[to_addr] 是收件人的邮箱地址, 是列表形式。因为邮件可能一次发给多个人,使用列表,如果发送多个人,就写多个邮箱,中间使用逗号隔开。
# 第三个参数:msg.as_string()把邮件内容MIMEText对象变成str。


from email.mime.text import MIMEText
import smtplib
msg = MIMEText('hello, Python auto send email', 'plain', 'utf-8')
# 输入Email地址和口令:
from_addr = input('请输入发件人的邮箱号码From: ')
password = input('请输入发件人的邮箱密码Password: ')
# 输入SMTP服务器地址:
smtp_server = input('请输入邮箱服务器地址SMTP server: ')
# 输入收件人地址:
to_addr = input('请输入收件人邮箱地址To: ')

import smtplib
server = smtplib.SMTP_SSL(smtp_server, 465) # SMTP协议加密端口是465
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit() # server.quit()语句,是邮件发送结束后,停止服务的意思.


# 完整邮件
# 仔细观察上图， 你会发现，现在还存在如下两个问题： 1.邮件没有主题； 2.收件人的名字没有显示为友好的名字，比如Mr Green ；
# 这是因为邮件主题、如何显示发件人、收件人等信息并不是通过SMTP协议发给MTA，而是包含在发给MTA的文本中的，
# 所以，我们必须把From、To和Subject添加到MIMEText中，才是一封完整的邮件：
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( Header(name, 'utf-8').encode(), addr))
# 输入Email地址和口令:
from_addr = input('请输入发件人的邮箱号码From: ')
password = input('请输入发件人的邮箱密码Password: ')
# 输入SMTP服务器地址:
smtp_server = input('请输入邮箱服务器地址SMTP server: ')
# 输入收件人地址:
to_addr = input('请输入收件人邮箱地址To: ')

msg = MIMEText('hi,小课让学习更轻松', 'plain', 'utf-8')
msg['From'] = _format_addr(u'开课吧 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自小K的问候……', 'utf-8').encode()

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
#
# 这次引入的模块文件有点多，增加了四个模块。
# 1、encoders模块负责编码
# 2、Header模块负责处理邮件头
# 3、MIMEText模块负责处理文本
# 4、parseaddr模块与formataddr模块 负责将输入的内容格式化

# 在这段代码中，我们还构建一个类用来处理格式化文本，将格式化的结果作为返回值传出去
# 代码片段
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
# 后对输入的内容进行格式化操作，将格式化后的内容赋值给变量
msg = MIMEText('hi,小课让学习更轻松', 'plain', 'utf-8')
msg['From'] = _format_addr(u'开课吧 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自小K的问候……', 'utf-8').encode()

# 现在，我们的内容有点少，能不能多写点内容。
# 可以啊。 下面，我们将邮件内容丰富起来。
# 我们使用字符串增加邮件内容，使用三引号的字符串，就可以原样显示字符串内容。
content = '''
亲爱的学员朋友：
    你好！
    恭喜大家学习坚持到现在!
    开课吧只为赋能人才，小课让学习更轻松！
'''

msg = MIMEText(content, 'plain', 'utf-8')
# 使用三引号字符串，将邮件内所有内容放入content变量中；将msg中的内容，换成content变量；将msg中的内容，换成content变量。
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( Header(name, 'utf-8').encode(), addr))
# 输入Email地址和口令:
from_addr = input('请输入发件人的邮箱号码From: ')
password = input('请输入发件人的邮箱密码Password: ')
# 输入SMTP服务器地址:
smtp_server = input('请输入邮箱服务器地址SMTP server: ')
# 输入收件人地址:
to_addr = input('请输入收件人邮箱地址To: ')

content = '''
亲爱的学员朋友：
    你好！
    恭喜大家学习坚持到现在!
    开课吧只为赋能人才，小课让学习更轻松！
'''

msg = MIMEText(content, 'plain', 'utf-8')
msg['From'] = _format_addr(u'开课吧 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自小K的问候……', 'utf-8').encode()

server = smtplib.SMTP_SSL(smtp_server,465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
