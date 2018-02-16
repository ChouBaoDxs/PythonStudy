# -*- coding: UTF-8 -*-
import urllib2

test='test'
password='123456'
webserver='192.168.21.52'

#构建一个密码管理对象，可以用来保存和HTTP请求相关的授权账户信息
passwordMgr=urllib2.HTTPPasswordMgrWithDefaultRealm()

#添加授权账户信息，第一个参数信息如果没有指定就写None，后三个分别是站点ip、账户、密码
passwordMgr.add_password(None,webserver,test,password)

#HTTPBasicAuthHandler()——————HTTP基础验证处理器类
httpauth_handler=urllib2.HTTPBasicAuthHandler(passwordMgr)

# proxyauth_handler=urllib2.ProxyBasicAuthHandler(passwordMgr)  #处理代理ip基础验证的写法

opener=urllib2.build_opener(httpauth_handler)   #可以写多个处理器(httpauth_handler,proxyauth_handler)

request=urllib2.Request('http://'+webserver)

# response=opener.open(request)
response=urllib2.urlopen(request)

print response.read()













