from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header

mail_Info = {
    "from": "37809131@qq.com",
    "to": "wubo@paicaifu.com",
    "hostName": "smtp.qq.com",
    "userName": "37809131",
    "password": "*************",
    "mailSubject": "test",
    "mailText": "hello world",
    "mailEncoding": " utf-8"
}

smtp_obj = SMTP_SSL(mail_Info["hostName"])
smtp_obj.ehlo(mail_Info["hostName"])
smtp_obj.login(mail_Info["userName"], mail_Info["password"])

msg = MIMEText(mail_Info["mailText"], "plain", mail_Info["mailEncoding"])
msg["Subject"] = Header(mail_Info["mailSubject"], mail_Info["mailEncoding"])
msg["From"] = mail_Info["from"]
msg["To"] = mail_Info["to"]
print(msg.as_string())
try:
    smtp_obj.sendmail(mail_Info["from"], mail_Info["to"], msg.as_string())
finally:
    smtp_obj.quit()
