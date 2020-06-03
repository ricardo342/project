#!/usr/bin/python
#coding=utf8

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
# logging. disable(logging.CRITICAL)    # 禁用日志
logging.debug('Start of program')

import unittest
import requests
import json
import HTMLTestRunner
import openpyxl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

class url():
    def __init__(self):
        self.website = 'xxx'
    
    def type_realm(self, type):
        if type == '测试':
            self.realm = 'https://www.xxx.com'
        elif type == '预发布':
            self.realm = 'https://www.zzz.com'
        elif type == '生产':
            self.realm = 'https://www.xxx.com'
        wegourl = self.realm + self.website
        return wegourl

url = url().type_realm('测试')

class OperationHeader():
    def __init__(self, response):
        self.response = json.load(response)
    
    def get_token(self):
        token = {"data":{"token":self.response['data']['token']}}
        return token

temp_token = OperationHeader('response').get_token()

add_commodity = openpyxl.load_workbook('add_commodity.xlsx')
add_commodity_sheet = add_commodity.get_sheet_by_name('Sheet1')

class test_add_commodity(unittest.TestCase):
    def new_add_commodity(self):
        i = 0
        for i in range(100):
            if i < 2:
                continue
            elif add_commodity_sheet['A' + str(i)].value == None:
                break
            else:
                self.url = url
                self.headers = {'Content-Type':'application/x-www-form-urlencoded'}
                self.form = {'client_type':add_commodity_sheet['A' + str(i)].value,
                            'token': temp_token,
                            'album_id': add_commodity_sheet['C' + str(i)].value,
                            'item_id': add_commodity_sheet['D' + str(i)].value,
                            'title':add_commodity_sheet['E' + str(i)].value,
                            'main_imgs':add_commodity_sheet['F' + str(i)].value,}

                # r = requests.post(self.url, self.headers, data=self.form)
                r = requests.post(self.url, headers=self.headers, data=self.form)
                try:
                    self.assertEqual(r.text, "\"errcode\":9,\"errmsg\":\"user token is expire\",\"status\":9")
                except AssertionError:
                    print("断言出错")

select_commodity = openpyxl.load_workbook('select_commodity.xlsx')
select_commodity_sheet = select_commodity.get_sheet_by_name('Sheet1')

class test_select_commodity(unittest.TestCase):
    def one_commodity(self):
        self.url = url
        self.headers = {'Content-Type':'application/x-www-form-urlencoded', 
                        'Cookie':'UM_distinctid=16f9cc4e342a4d-0368d5f8087051-c383f64-1fa400-16f9cc4e343674; CNZZDATA1275056938=200193292-1578882658-%7C1590455464; JSESSIONID=F415BC22DF2BD2CA93D030E7FD206109; test_token=MEY0QzM4NkJBNzZDREEyOTNGMEQzOEI3MjAyOTM3NzE2ODc4NzNDOUNFOEE0REQ1QzcwODg1OTQ3OUZFQTgyMDgwNjNBRTMyNjM2NkJGQkIxNDBBQUQyODJGRDMzMzMw; client_type=net; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22A202003261356237010009045%22%2C%22first_id%22%3A%2216f9cc4e34a25-072ac86807ac7d-c383f64-2073600-16f9cc4e34bacc%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2216f9cc4e34a25-072ac86807ac7d-c383f64-2073600-16f9cc4e34bacc%22%7D; test_run_to_dev_tomcat='}
        self.form = {'shop_id':select_commodity_sheet['A2'].value,
                     'goods_id':select_commodity_sheet['B2'].value,
                     'token':select_commodity_sheet['C2'].value,}
        r = requests.post(self.url, headers=self.headers, data=self.form)
        self.assertIn(r.text, select_commodity_sheet['C2'].value)
            
def suite(unittest):
    wegoTestCase = unittest.makeSuite()
    wegoTestCase.addTest(test_add_commodity, "testing")
    return wegoTestCase

test_add_commodity().new_add_commodity()

if __name__ == "__main__":
    fr = open("result.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fr, title='测试报告', description='详情')
    runner.run(suite(unittest))

class send_mail():
    def __init__(self, sender, accepter, file):
        self.sender = sender        # 'majiaqin@wegooooo.com'
        self.accepter = accepter    # 'majiaqin@wegooooo.com'
        self.file = file            # 'result.html'
    
    def send_file(self):
        self.smtpObj = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
        self.message = MIMEText(self.file, "html", "utf-8")
        self.smtpObj.ehlo()
        self.smtpObj.login(self.sender, '06257020S')
        self.smtpObj.sendmail(self.sender, self.accepter, 'Subject: 接口测试报告. \n接口测试详情如下: \n ' + self.message.as_string())
        self.smtpObj.quit()
        print("发送成功!")

logging.debug('End of program')
