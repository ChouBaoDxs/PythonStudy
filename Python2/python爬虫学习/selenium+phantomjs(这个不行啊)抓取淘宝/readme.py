# -*- coding: UTF-8 -*-
#selenium：第三方模块 能够驱动大部分主流的浏览器   就是模拟用户操作
#phantomjs：无界面的浏览器

# from selenium import webdriver
# import time

# driver=webdriver.Chrome(executable_path="/Applications/Google Chrome.app/Contents/MacOS/chromedriver")
# driver.get('https://www.baidu.com')

# driver操作页面的基本方法    定位网页元素
# 常见的定位方法：id class css xpath
# find_element_by_name
# find_element_by_xpath
# find_element_by_link_text
# find_element_by_css_selector

# driver.find_element_by_id('kw').send_keys('pyhton')
# time.sleep(2)
# driver.find_element_by_id('su').click()
# time.sleep(2)
# driver.quit()

#页面等待   很重要
#动态加载：ajax  js   这样程序就不能确定我们定位的元素是否已经加载出来
#time.sleep()   不推荐，其实也不能确定页面是否已经加载完全
#显示等待：指满足某一个条件之后再执行后面的代码，可以设置最长的等待时间

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #WebDeriverWait库 负责循环等待
# from selenium.webdriver.support.ui import WebDriverWait
# #expected_conditions类 负责条件
# from selenium.webdriver.support import expected_conditions as EC
#
# driver=webdriver.Chrome(executable_path="/Applications/Google Chrome.app/Contents/MacOS/chromedriver")
# driver.get('http://www.baidu.com/')
# try:
#     #页面会一直循环，直到id=mydynmicElement出现
#     #格式：WebDriverWait(driver,time).until(EC.条件(By.id,''))
#     element=WebDriverWait(driver,10).until(
#         EC.presence_of_all_elements_located(By.ID,'mydynmicElement')
#     )
# finally:
#     driver.quit()

# presence_of_all_element_located 判断页面的元素是否已经加载出来
# elements_to_be_clickable    判断当前的这个元素是否可以点击

#css定位
#id属性 class标签来定位，可以组合一起
#   '#'表示id属性   '.'表示class  标签直接使用  还有很多其他的属性
# driver.find_element_by_css_selector('#kw')
# driver.find_element_by_css_selector('.s_ipt')
# driver.find_element_by_css_selector('input')
# #其他属性的定位方式
# driver.find_element_by_css_selector('[其他属性="other"]')
# #类似的，id的定位也可以这样写
# driver.find_element_by_css_selector('[id="kw"]')
#
# #组合形式的
# driver.find_element_by_css_selector('input.s_ipt')
# driver.find_element_by_css_selector('input[ad="sss"]')
# #层级关系
# driver.find_element_by_css_selector('input > span > a')

# BeautifulSoup
# find 匹配一个元素，没有就是None
# find_all 匹配所偶有元素，返回一个list
