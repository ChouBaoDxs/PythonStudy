# -*- coding: UTF-8 -*-

import json
from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="/Applications/Google Chrome.app/Contents/MacOS/chromedriver")
driver.get('https://mp.weixin.qq.com')

driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[1]/div[1]/div/span/input').clear()  #定位到账号输入框  清除
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[1]/div[1]/div/span/input').send_keys('2720961338@qq.com')  #输入账号
time.sleep(2)
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[1]/div[2]/div/span/input').clear()  #定位到密码输入框  清除
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[1]/div[2]/div/span/input').send_keys('d826842697')  #输入密码
time.sleep(2)
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[3]/label').click()  #点击记住密码
time.sleep(2)
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[4]/a').click()    #点击登录
time.sleep(15)

cookies=driver.get_cookies()    #获取登录之后的cookies
cookie={}

for item in cookies:
    cookie[item.get('name')] = item.get('value')

#保存cookie
with open('cookies.txt','w') as file:
    file.write(json.dumps(cookie))#写入转成字符串的close

driver.close()









