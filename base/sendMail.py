# coding:utf-8

from common.config import PATH
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import codecs
import pandas as pd
import os

# 测试报告的路径
reportPath = PATH("../Report/result.xls")
htmlReportPath = PATH("../Report/Report.html")


#收件人
recvaddress = ['15168208716@163.com']

#发件人
sendaddr_name = '此处填写邮箱'
sendaddr_pswd = '邮箱密码'


class SendMail:
    def __init__(self, recver=None):
        """接收邮件的人："""
        if recver is None:
            self.sendTo = recvaddress
        else:
            self.sendTo = recver

    def __take_messages(self):
        '''
        生成测试报告内容
        :return:
        '''
        xd = pd.ExcelFile(reportPath)
        pd.set_option('display.max_colwidth', 30)  # 设置列的宽度，以防止出现省略号

        df = xd.parse()
        '将excel转化成html'
        with codecs.open(htmlReportPath, 'w') as html_file:
            html_file.write(df.to_html(header=True, index=False))

        """生成邮件的内容，和html报告附件"""
        xlsxpart = MIMEApplication(open(reportPath, 'rb').read())
        xlsxpart.add_header('Content-Disposition', 'attachment',
                                filename=('gbk', '', "Report.xlsx"))  # 注意：此处basename要转换为gbk编码，否则中文会有乱码。
        with open(os.path.join(htmlReportPath), 'rb') as f:
            mailbody = f.read()
        att1 = MIMEText(mailbody, 'html', 'gbk')


        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="接口测试报告.html"'
        self.msg = MIMEMultipart('related')
        self.msg.attach(xlsxpart)
        self.msg['Subject'] = '接口测试报告'
        self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
        self.msg.attach(att1)

    def send(self):
        """发送邮件"""
        self.__take_messages()
        self.msg['from'] = sendaddr_name
        try:
            smtp = smtplib.SMTP('smtp.lcare.net', 25)
            smtp.login(sendaddr_name, sendaddr_pswd)
            smtp.sendmail(self.msg['from'], self.sendTo, self.msg.as_string())
            smtp.close()
            print("发送邮件成功")
        except Exception:
            print('发送邮件失败')
            raise


if __name__ == '__main__':
    sendMail = SendMail()
    sendMail.send()

