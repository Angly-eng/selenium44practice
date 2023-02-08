# -*- coding = utf-8 -*-
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome(r'D:\Google\Chrome\Application\chromedriver.exe')

# 打开注册网址
driver.get('https://d2.shopxo.vip/regster.html')

# 定位登录框并输入
driver.find_element('xpath', "//input[@name='accounts']").send_keys("zxcdc1997")

# 定位密码框并输入
driver.find_element('xpath', "//input[@name='pwd']").send_keys("123123")
# 勾选同意协议
driver.find_element('xpath', "//i[@class='am-icon-checked']").click()
sleep(6)
# 点击注册
driver.find_element('xpath', "//form[@class='am-form form-validation-username']//button[text()='注册']").click()
sleep(3)
driver.close()