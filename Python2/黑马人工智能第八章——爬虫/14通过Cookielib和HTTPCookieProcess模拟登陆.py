# -*- coding: UTF-8 -*-
import urllib
import urllib2
import cookielib

#通过CookieJar()类构建一个cookieJar()对象，用来保存cookie的值
cookie=cookielib.CookieJar()

#通过HTTPCookieProcessor()处理器类构建一个处理器对象，用来处理cookie
#参数就是构建的CookieJar()对象
cookie_handler=urllib2.HTTPCookieProcessor(cookie)

#构建一个自定义的opener
opener=urllib2.build_opener(cookie_handler)

#自定义opener的addheaders的参数，可以赋值HTTP报头参数
opener.addheaders=[('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')]

#人人网的登陆接口
url='http://www.renren.com/PLogin.do'
# url='http://www.renren.com/SysHome.do'

#需要登陆的账号密码
data={'email':'17706440586','password':'d826842697'}

#通过urlencode()编码转换
data=urllib.urlencode(data)

request=urllib2.Request(url,data)

#发送的第一次请求是post请求，登陆成功的话，cookie会保存
response=opener.open(request)

print response.read()


#登陆之后访问其他人的主页   这一次是get请求
# response2=opener.open('....................')
#
# print response2.read()




