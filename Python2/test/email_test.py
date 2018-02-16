# -*- coding: UTF-8 -*-
# qq邮箱授权码：nkxoznvnnszabdgc

import smtplib
from email.mime.text import MIMEText

_user = "826842697@qq.com"
_pwd = "nkxoznvnnszabdgc"
_to = "826842697@qq.com"    #目标邮箱

msg = MIMEText("Test")          #正文
msg["Subject"] = "python test"  #主题
msg["From"] = _user
msg["To"] = _to

try:
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(_user, _pwd)
    s.sendmail(_user, _to, msg.as_string())
    s.quit()
    print "Success!"
except smtplib.SMTPException, e:
    print "Falied,%s" % e
