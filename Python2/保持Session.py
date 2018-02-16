# -*- coding: UTF-8 -*-

#requests的会话保持
import requests
#实例化一个Session对象
request=requests.Session()

#使用用一个实例化对象去执行get或post请求
request.get()
request.post()

#返回结果为json类型数据时，可以直接下面那样取
response=request.get()
json_data=response.json()
data=json_data['data']['userid']


#urllib2的会话保持
import urllib2
import cookielib
c=cookielib.LWPCookieJar()
cookie=urllib2.HTTPCookieProcessor(c)
opener=urllib2.build_opener(cookie)

url='http://www.baidu.com'
req=urllib2.Request(url)
#原本方式
html=urllib2.urlopen(req).read()
#保持会话
html=opener.open(req).read()

#返回结果为json类型数据时，可以直接下面那样取
import json
json_data=json.loads(html)





