# -*- coding: UTF-8 -*-
import cookielib
import urllib2

url="http://www.baidu.com/"
# url='http://weibo.com/cnstock'
print '第一种方法'
response1=urllib2.urlopen(url)
print response1.getcode()
print len(response1.read())

print '第二种方法'
request=urllib2.Request(url)
request.add_header('User-Agent','Mozilla/5.0')#把爬虫伪装成一个浏览器
response2=urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

print '第三种方法'
url='http://weibo.com/cnstock?is_all=1'
cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3=urllib2.urlopen(url)
print response3.getcode()
print cj
# print response3.read()


import urllib
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

html = getHtml("http://blog.sina.com.cn/")
html = getHtml("http://weibo.com/cnstock?is_all=1")#不行啊
html = getHtml("http://www.baidu.com")#不行啊
# print html

import requests
html = requests.get("https://weibo.com/")
print html.text