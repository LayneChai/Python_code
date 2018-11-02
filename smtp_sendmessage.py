#email 负责构造邮件 smtplib负责发送邮件
from email.mime.text import MIMEText
msg = MIMEText("纯文本内容",'plain','utf-8')
#MIMEText 第一个参数是邮件正文  ,第二个是邮件MIME的类型 因为是纯文本'text/plain' 最后编码类型 'utf-8'
#输入发送的账号和密码 
from_addr = '发送端邮箱账户@163.com'#input('From:')
password = '邮箱授权码'#input('Password:')

#输入收件人地址
to_addr= '接收端邮箱账户@qq.com'#input('To:')
# msg中要包含发送邮件和接收邮件的地址
#邮箱发送端在信息中包含一下
msg['From'] = from_addr
#邮箱接收端在信息中包含一下
msg['To'] = to_addr
#邮箱标题
msg['Subject'] = 'The message is a test'
#输入SMTP服务器地址
smtp_server = 'smtp.163.com'  #input('SMTP server:')
 
import smtplib
server = smtplib.SMTP(smtp_server,25)  #smtp 协议默认的是25端口
server.set_debuglevel(1) #可以打印出和SMTP服务器交互的所有信息
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
#sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str
server.quit()
  
 

update：：：



#email 负责构造邮件 smtplib负责发送邮件
from email.mime.text import MIMEText
from email.header import Header
from email import encoders
from email.utils import parseaddr,formataddr
from email.mime.multipart import  MIMEMultipart   #生成包括多个部分的邮件体
from email.mime.multipart import MIMEBase         #附件的对象
import smtplib

def _format_addr(s):
    name,addr = parseaddr(s)    #把对应的字符串拆分成对应的用户名和邮件地址
    return formataddr((Header(name,'utf-8').encode(),addr))    #这个formataddr会返回一个字符串
#这个formataddr中的第一个name应该是RFC 2047类型的所以需要Header的encode（）转换但是name可以是str utf-8 charset三种类型的一种

#输入发送的账号和密码
# from_addr = '发送邮箱地址@qq.com'#input('From:')
# password = '发送授权码'#input('Password:')
from_addr ='发送邮箱地址@163.com'
password = '发送授权码'

#输入收件人地址
to_addr= '接收邮箱地址@qq.com'#input('To:')
"""
msg信息
# msg = MIMEText("I am cyl.",'plain','utf-8')
#当我们发送html邮件的时候就把对应的plain 换成html就可以了
# msg = MIMEText('<html><body><h1>Hello</h1>' 
#MIMEText 第一个参数是邮件正文  ,第二个是邮件MIME的类型 因为是纯文本'text/plain' 最后编码类型 'utf-8'
#     '<p>send by <a href="http://www.baidu.com">百度</a>...</p>' +
#     '</body></html>','html','utf-8')
"""
#发送邮件时候带一个附件
# 带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身，所以，可以构造一个MIMEMultipart对象代表邮件本身，
# 然后往里面加上一个MIMEText作为邮件正文，再继续往里面加上表示附件的MIMEBase对象即可：
msg = MIMEMultipart()
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>','html','utf-8'))

# msg中要包含发送邮件和接收邮件的地址
msg['From'] = _format_addr('CYL_163 <%s>'%from_addr)
# 注意不能简单地传入name <addr@example.com>，因为如果包含中文，需要通过Header对象进行编码
msg['To'] = _format_addr('CYL_QQ <%s>'%to_addr)   #但是这个接收端的名字可能被对方服务器改成接收端在对方服务器的名字
msg['Subject'] = Header('The message come from CYL_163','utf-8').encode()
#当主题中包含汉字时候，就要用Header().encode()进行编码变成RFC 2047
with open('ctw.png','rb') as f:
    # 设置附件的MIME和文件名，这里是png(二进制类型)类型: MIME能够支持非ASCII字符、二进制格式附件等多种格式的邮件消息
    mime = MIMEBase('image','png',filename='ctw.png')
    #加上必要的头信息
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    #把附件的内容读进来
    mime.set_payload(f.read())
    #使用Base64编码
    encoders.encode_base64(mime)
    #添加到MIMEMultipart中
    msg.attach(mime)

#输入SMTP服务器地址
# smtp_server = 'smtp.163.com'#input('SMTP server:')
#
# server = smtplib.SMTP(smtp_server,25)  #smtp 协议默认的是25端口
smtp_server = 'smtp.163.com'
smtp_port = 25
server = smtplib.SMTP(smtp_server, smtp_port)
# server.starttls()        #加密传输
server.set_debuglevel(1) #可以打印出和SMTP服务器交互的所有信息
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
#sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str
server.quit()
  
 
