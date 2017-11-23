from Email import Email_send
if __name__ == '__main__':
    # from urllib import request
    # resonse = request.urlopen(r'http://adadlfas.adfaf')
    # print(resonse)
    email=Email_send('1014596312@qq.com','这是使用python发送的第一封邮件','这是使用python发送的第一封邮件')
    ret = email.sendEmail()
    print(ret)
