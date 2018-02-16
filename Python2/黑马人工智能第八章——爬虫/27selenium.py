# -*- coding: UTF-8 -*-
from selenium import webdriver

driver=webdriver.Chrome(executable_path="/Applications/Google Chrome.app/Contents/MacOS/chromedriver")
driver.get('https://www.baidu.com')
driver.save_screenshot('图片.png')        #把页面保存为图片       快照

from selenium.webdriver.common.keys import Keys

driver.find_element_by_id('kw').send_keys(u'bilibili')

driver.find_element_by_id('su').click()

print driver.page_source()  #输出页面源码

print driver.get_cookies()  #输出cookie

#ctrl+a全选输入框内容
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')

#ctrl+x剪切输入框的内容
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')

#模拟回车
# driver.find_element_by_id('kw').send_keys(Keys.RETURN)

#清除输入框
# driver.find_element_by_id('kw').clear()

#取得当前的url
# driver.current_url

#弹窗处理：获取弹窗
# alert=driver.switch_to_alert()

#页面前进后退
# driver.forward()
# driver.back()

#显式等待
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# #直到目标元素出现，最多等10秒
# try:
#     element=WebDriverWait(driver,10).until(
#         EC.presence_of_all_elements_located(By.ID,'myDynamicElement')
#     )
# finally:
#     driver.quit()

#隐式等待   #设定全局的等待时间为10秒
# driver.implicitly_wait(10)








