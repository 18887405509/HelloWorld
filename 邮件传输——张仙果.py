Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #coding=utf-8
>>> import smtplib
>>> from email.mime.text import MIMEText
>>> msg_from='5782008@qq.com'
>>> msg_from='3290477997@qq.com'
>>> passwd='rdlpmjgucvvhcieb'
>>> msg_to='57820048@qq.com'
>>> subject="2019144135 张仙果"
>>> content="黄老师，您好，我是2019144135张仙果，我查询到学校公网IP地址为220.164.161.126，学校私网IP地址为10.128.67.14，本机公网IP地址为117.136.84.4，本机私网IP地址为20.46.112.26"
>>> msg=MIMEText(content)
>>> msg['Subject']=subject
>>> msg['From']=msg_from
>>> msg['To']=msg_to
>>> try:
	s=smtplib.SMTP_SSL("smtp.qq.com",465)
	s.login(msg_from,passwd)
	s.sendmail(msg_from,msg_to,msg.as_string())
	print("发送成功")
except(s.SMTPException,e):
	print("发送失败")
finally:
	s.quit()
