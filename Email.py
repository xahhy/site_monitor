import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email_send(object):
    def __init__(self, msgTo, data2, Subject):
        self.msgTo = msgTo
        self.data2 = data2
        self.Subject = Subject

    def sendEmail(self):
        # (attachment,html) = content
        msg = MIMEMultipart()
        msg['Subject'] = self.Subject
        msg['From'] = 'hhy132831@126.com'
        msg['To'] = self.msgTo
        html_att = MIMEText(self.data2, 'html', 'utf-8')
        # att = MIMEText(attachment, 'plain', 'utf-8')
        msg.attach(html_att)
        # msg.attach(att)
        try:
            smtp = smtplib.SMTP()
            smtp.connect('smtp.126.com', 25)
            smtp.login(msg['From'], 'hehongyuan')  # 改成自己的邮箱密码
            smtp.sendmail(msg['From'], msg['To'].split(','), msg.as_string())
            return ('邮件发送成功')
        except Exception as e:
            print('--------------sss------', e)

    # def curl(self):
    #     import pycurl
    #     c = pycurl.Curl()
    #     # url="www.luoan.com.cn"
    #     # indexfile=open(os.path.dirname(os.path.realpath(__file__))+"/content.txt","wb")
    #     c.setopt(c.URL, url)
    #     c.setopt(c.VERBOSE, 1)
    #     c.setopt(c.ENCODING, "gzip")
    #     # 模拟火狐浏览器
    #     c.setopt(c.USERAGENT, "Mozilla/5.0 (Windows NT 6.1; rv:35.0) Gecko/20100101 Firefox/35.0")
    #     return c
