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
  
 
