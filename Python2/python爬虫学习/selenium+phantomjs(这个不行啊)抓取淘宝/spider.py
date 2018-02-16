# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException #超时异常
from bs4 import BeautifulSoup
import json

# driver=webdriver.Chrome(executable_path="/Applications/Google Chrome.app/Contents/MacOS/chromedriver")
driver = webdriver.PhantomJS()      #传说中的无界面浏览器 #不行啊 这个
wait=WebDriverWait(driver,10)   #wait就是打开的浏览器对象

def search(shop=None):
    print u'开始搜索...'
    print '当前是第1页...'
    driver.get('https://www.taobao.com')
    try:
        #判断输入框是否加载完成
        input=wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#q'))
        )
        input.send_keys(u'{}'.format(shop))
        submit=wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button'))
        )
        submit.click()
        get_response()
    except TimeoutException:
        return search(shop)

def get_response():
    #判断当前的商品加载出来没有
    wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#mainsrp-itemlist .items .item'))#css空格：赋值选择器
    )
    html=driver.page_source #获取当前页面的网页源代码
    soup=BeautifulSoup(html,'lxml')#选择用什么解析器来解析网页
    items=soup.find('div',class_='m-itemlist').find_all('div',class_='item')
    for item in items:
        # print item
        product={
            'image':item.find('a').find('img')['src'],   #取得图片地址
            'price':item.find('div',class_='price g_price g_price-highlight').text, #取得价格标签下的文本内容
            'pay_counts':item.find('div',class_='deal-cnt').text[:-3],  #取得付款人数标签下的文本，并去掉'人付款'3个字
            'title':item.find('div',class_='row row-2 title').text, #获取商品名称
            'location':item.find('div',class_='location').text,  #取得地址
        }

        print json.dumps(product, ensure_ascii=False)

def next_page(page):
    print '当前是第{}页...'.format(page)
    try:
        input=wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > input'))
        )[0]    #因为是all_elements 所以要取第一个
        submit=wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit'))
        )
        input.clear()   #清空页码
        input.send_keys(page)
        submit.click()  #点击确定
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(page))
        )
        get_response()
    except TimeoutException:
        return next_page(page)

if __name__=='__main__':
    shop=raw_input('请输入要搜索的商品名称:')
    search(shop)
    for i in range(2,5):    #只输出第2页到第4页
        next_page(i)










