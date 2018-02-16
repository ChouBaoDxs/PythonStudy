# -*- coding: UTF-8 -*-
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def open51job(url,keys):
    driver = webdriver.Chrome(executable_path="/Applications/Google Chrome.app/Contents/MacOS/chromedriver")
    # driver = webdriver.PhantomJS()      #传说中的无界面浏览器
    driver.implicitly_wait(10)  # 最多给10秒钟寻找元素
    driver.get(url)
    print u'进入'+driver.title
    #进入页面，找到搜索框
    elem=driver.find_element_by_id('kwdselectid')#定位到搜索框并赋值
    elem.clear()
    # print keys
    elem.send_keys(keys.decode('utf-8'))    #中文要编码

    #把城市那里清空
    time.sleep(2)
    elem.find_element_by_xpath('//*[@id="work_position_input"]').click()    #点击城市
    time.sleep(2)
    elem.find_element_by_xpath('//*[@id="work_position_click_multiple_selected_each_080200"]').click() #点击删除城市信息
    time.sleep(2)
    elem.find_element_by_xpath('//*[@id="work_position_click_bottom_save"]').click()    #点击确定
    time.sleep(2)
    elem.find_element_by_xpath('//*[@id="kwdTypeSelUl"]/li[1]').click()#点击全文
    time.sleep(2)
    elem.find_element_by_xpath('//*[@id="kwdTypeSelUl"]/li[2]/a').click()#点击公司
    time.sleep(2)
    elem.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/button').click()   #点击搜索

    # #获取所有窗口
    # for handle in driver.window_handles:
    #     driver.switch_to_window(handle)

    return driver

#匹配数据
def searchJob(driver):
    data=driver.page_source
    content=BeautifulSoup(data,'lxml')  #也可以是html.parse
    #匹配信息
    position=content.find_all('p',{"class":"t1"})     #职位名称
    # position=content.find_all('p',class_='t1')
    company=content.find_all('span',{"class":"t2"})   #公司
    # company = content.find_all('span', class_='t2')
    location=content.find_all('span',{"class":"t3"})  #地址
    # location = content.find_all('span', class_='t3')
    salary=content.find_all('span',{"class":"t4"})    #工资
    # salary = content.find_all('span', class_='t4')
    publish=content.find_all('span',{"class":"t5"})   #发布日期
    # publish = content.find_all('span', class_='t5')

    i=0
    for each in position:
        print '*****第'+str(i+1)+'个job*****'
        print u'职位名:'+each.a.get('title')    #下面只有一个a，所以
        print u'职位链接:'+each.a.get('href')
        print u'公司名:'+company[i+1].string #获取文本内容
        print u'工作地点:'+location[i+1].string #获取文本内容
        try:
            print u'薪资:'+salary[i+1].string   #获取文本内容
        except:
            pass
        print u'发布时间:'+publish[i+1].string  #获取文本内容
        print '\n'
        i+=1

    return driver

def nextPage(driver):
    try:
        page_num=driver.find_elements_by_link_text('下一页')       #通过文本找到链接           #这里有个bug，会报错，无法点击下一页
        # page_num=driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/ul/li[8]')
        page_num.click()
    except NoSuchElementException:
        print u'搜索完毕'
        flag=0
        return

if __name__=='__main__':
    url='http://www.51job.com'
    keys=raw_input('请输入搜索工作的关键字:')
    num=1
    driver=open51job(url,keys)
    while True:
        print u'*****第'+str(num)+u'页*****'
        driver=searchJob(driver)
        # flag=nextPage(driver)
        # if flag==0:
        #     break
        # num+=1
        break

    time.sleep(10)
    driver.close()





