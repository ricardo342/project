#!/usr/bin/env python
# -*- coding:utf-8 -*-



import smtplib
import os
import datetime
import threading

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from commonApp import DeleteFile


accepter_list = ['XXX@galanz.com','XXX@galanz.com']


def send_mail():
    files = "C:\\Users\\Administrator\\Downloads\\小B直供系统-未解决Bug.html"
    mail_host = 'mail.galanz.com'  # 设置服务器
    mail_port = 25  # SMTP端口号
    #mail_accepter = 'yaoxs@galanz.com'
    mail_accepter = accepter_list
    accepter = 'XXX'  # 接收者简称
    mail_sender = 'XXX@galanz.com'  # 发送邮箱
    mail_password = 'yXS940113'  # 邮箱密码

    with open(files, 'r',encoding="utf-8") as file:
        mail_body = file.read()
        sender = 'XXX@galanz.com'
        text = MIMEText(mail_body, 'html', 'utf-8')
        """创建一个带附件的实例"""
        message = MIMEMultipart('mixed')
        message.attach(text)

    today = str(datetime.date.today())
    name = 'XXX遗留BUG <每日提醒' + '_' + today + '>'
    message['Subject'] = name
    message['From'] = sender
    message['To'] = "".join(accepter)

    try:
        s = smtplib.SMTP(mail_host, mail_port)
        s.login(mail_sender, mail_password)
        s.sendmail(sender, mail_accepter, message.as_string())
        s.close()
        # os.remove(files)
        print("邮件发送成功！")
    except Exception as e:
        raise e

    # 清除缓存
    path = "C:\\Users\\Administrator\\Downloads"
    end_with = ".html"
    # files_front = [file for file in os.listdir(path)]
    # print(f"files_front={files_front}")
    DeleteFile.del_file(end_with, path)
    # files_behind = [file for file in os.listdir(path)]
    # print(f"files_behind={files_behind}")


cookie_list = [{'domain': '172.1.1.125', 'httpOnly': False, 'name': 'qaBugOrder', 'path': '/', 'secure': False, 'value': 'id_desc'}, {'domain': '172.1.1.125', 'expiry': 1599617032, 'httpOnly': False, 'name': 'preProductID', 'path': '/', 'secure': False, 'value': '67'}, {'domain': '172.1.1.125', 'expiry': 1599617032, 'httpOnly': False, 'name': 'preBranch', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '172.1.1.125', 'httpOnly': False, 'name': 'windowHeight', 'path': '/', 'secure': False, 'value': '926'}, {'domain': '172.1.1.125', 'expiry': 1599617032, 'httpOnly': False, 'name': 'lastProduct', 'path': '/', 'secure': False, 'value': '67'}, {'domain': '172.1.1.125', 'httpOnly': False, 'name': 'windowWidth', 'path': '/', 'secure': False, 'value': '1920'}, {'domain': '172.1.1.125', 'httpOnly': False, 'name': 'bugModule', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '172.1.1.125', 'expiry': 1599617032, 'httpOnly': False, 'name': 'lang', 'path': '/', 'secure': False, 'value': 'zh-cn'}, {'domain': '172.1.1.125', 'expiry': 1599617032, 'httpOnly': False, 'name': 'theme', 'path': '/', 'secure': False, 'value': 'default'}, {'domain': '172.1.1.125', 'expiry': 1599617032, 'httpOnly': False, 'name': 'device', 'path': '/', 'secure': False, 'value': 'desktop'}, {'domain': '172.1.1.125', 'httpOnly': False, 'name': 'zentaosid', 'path': '/', 'secure': False, 'value': 'gs7dfbdi0mqva745165iihfji6'}]

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://172.1.1.125/user-login.html")

for cookie in cookie_list:
    driver.add_cookie(cookie)
driver.get("http://172.1.1.125/user-login-L2J1Zy1icm93c2UtNjcuaHRtbA==.html")

driver.find_element_by_xpath("/html/body/main/div/div[3]/div[2]/form/div[2]/table/thead/tr/th[3]/a").click()
sleep(1)
driver.find_element_by_xpath("/html/body/main/div/div[2]/div[2]/a[7]/span[1]").click()
sleep(1)
driver.find_element_by_xpath("//*[@id=\"mainMenu\"]/div[3]/div/button").click()
driver.find_element_by_xpath("//*[@id=\"exportActionMenu\"]/li/a").click()
sleep(2)

driver.switch_to.frame('iframe-triggerModal')
driver.find_element_by_xpath("//*[@id=\"fileType\"]/option[3]").click()
sleep(1)
driver.find_element_by_xpath("//*[@id=\"template_chosen\"]/a/div[1]").click()
sleep(1)
driver.find_element_by_xpath("//*[@id=\"template_chosen\"]/div/ul/li[3]").click()
sleep(1)
driver.find_element_by_xpath("//button[contains(.,'导出')]").click()

ActionChains(driver).key_down(Keys.ENTER).perform()
sleep(6)
driver.close()

# send_mail("C:\\Users\\Administrator\\Downloads\\XXX系统-未解决Bug.html")
# file = "C:\\Users\\Administrator\\Downloads\\XXX系统-未解决Bug.html"

# 定时器
now_time = datetime.datetime.now()

# 获取明天时间
next_time = now_time + datetime.timedelta(days=+1)
next_year = next_time.date().year
next_month = next_time.date().month
next_day = next_time.date().day

# 获取明天0点的时间
next_time = datetime.datetime.strptime(str(next_year) + "-" + str(next_month) + "-" + str(next_day) + " 00:01:00","%Y-%m-%d %H:%M:%S")

# 获取距离明天的时间（s)
timer_start_time = (next_time - now_time).total_seconds()

# for debug
timer_start_time1 = 60

print(f'******DEBUG>>>total_seconds={timer_start_time}<<<DEBUG******')

timer = threading.Timer(timer_start_time,send_mail)
timer.start()




