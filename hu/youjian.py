#!/usr/bin/python
#-*-coding:utf-8-*-
import smtplib  #封装smtp协议
import email.mime.text   #处理正文中的数据
import email.mime.multipart  #邮件的格式
sender = '13781147317@163.com'
reser = ['1423493690@qq.com','492104931@qq.com']
server = 'smtp.163.com'
#授权码
passwd = 'qweasd123'
#创建一个空的邮件
message = email.mime.multipart.MIMEMultipart()
message['from']=sender
message['To']=','.join(reser)
message['Subject']='python_learn'
aa="""我好帅啊
"""
cc=email.mime.text.MIMEText(aa)
#定义发送的附件的文件名，文件可以是任何格式的
att1=email.mime.text.MIMEText(open(r'E:\PycharmProjects\untitled\害羞.jpg','rb').read(),'base64','jpg')
#附件携带的字段和值
att1["Content-Type"]='application/octet-stream'
#附件携带的字段和值  这里的filename可以任意写，写什么名字，邮件中就是什么名字
att1["Content-Disposition"]='attachment;filename="害羞.jpg"'
#将附件添加到邮件里
message.attach(att1)
#将正文添加到邮件里
message.attach(cc)
#定义发送邮件的服务器和端口号
smtp123=smtplib.SMTP_SSL(server,465)
#登录服务器
smtp123.login(sender,passwd)
#发送邮件
smtp123.sendmail(sender,reser,message.as_string())
#断开连接
# smtp123.close()

