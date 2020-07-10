import yaml,xlrd
import smtplib
from email.mime.text import MIMEText
#from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.header import Header
from log.log import Logger
import openpyxl


def read_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        yaml_data = yaml.load(f, Loader=yaml.FullLoader)  # 或者yaml.full_load()
        print(yaml_data)
        return yaml_data



class SendEmail:
    def send_email(self,email_path):
        message = MIMEMultipart()
        #邮件内容
        text = """
        请输入你想说的邮件内容
        """
        message.attach(MIMEText(_text=text, _subtype='plain', _charset="utf-8"))
        #需要发送的附件的路径
        with open(email_path, 'rb') as f:
            content = f.read()
        att1 = MIMEText(content, "base64", "utf-8")
        att1["Content-Type"] = 'application/octet-stream'
        att1['Content-Disposition'] = 'attachment; filename = "report.html"'
        message.attach(att1)

        #邮件主题
        message["Subject"] = Header("主题", "utf-8").encode()
        message["From"] = Header("tianmeng", "utf-8")
        message["To"] = Header('tianmeng_wxk', "utf-8")

        try:
            smtp = smtplib.SMTP()
            #smtp = smtplib.SMTP_SSL('smtp.163.com', 465)
            smtp.connect(host="smtp.qq.com", port=587)
            smtp.login(user="3394788013@qq.com", password="lizceyidpekpdbhd")
            sender = "3394788013@qq.com"
            receiver = ['tianmeng_wxk@163.com']
            smtp.sendmail(sender, receiver, message.as_string())
            Logger().log().info("发送邮件成功")
        except smtplib.SMTPException as e:
            Logger().log().info("发送邮件失败，失败信息：{}".format(e))

class ReadExcel:
    def __init__(self, excel_path, sheet_name):
        self.workbook = xlrd.open_workbook(excel_path)
        self.worksheet = self.workbook.sheet_by_name(sheet_name)
        self.rownum = self.worksheet.nrows
        self.colnum = self.worksheet.ncols
    #xlrd读取excel
    def dict_data(self):
        if self.rownum <= 1:
             print("表格行数小于等于1，不能进行自动化")
        else:
             list = []
             self.headers = self.worksheet.row_values(0)
             #self.headers = self.worksheet.row_values(0)
             #j = 1#从1开始
             for i in range(1, self.rownum):
                 s = {}
                 values = self.worksheet.row_values(i)

                 for x in range(self.colnum):
                    s[self.headers[x]] = values[x]
                 list.append(s)
                 #j += 1
             return list


#openpycl读取excel
class ReadExcel2:
    def load_excel(self,excel_path):
        excel = openpyxl.load_workbook(excel_path)
        return excel

    def load_sheets(self,excel):
        sheets = excel.sheetnames
        return sheets

    def save_excel(self, excel, excel_path):
        excel.save(excel_path)

    def close_excel(self, excel):
        excel.close()






