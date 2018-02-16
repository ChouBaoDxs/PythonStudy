# -*- coding: UTF-8 -*-
import urllib2

#代理开关，表示是否启用代理
proxy_switch=True

#构建一个Handler处理器对象，参数是一个字典类型，包括{'代理类型':'代理服务器ip:端口号'}
httpproxy_handler= urllib2.ProxyHandler({'http':'218.56.132.154:8080'})     #这里使用的是免费代理     开放代理

# httpproxy_handler= urllib2.ProxyHandler({'http':'dxs:mm@218.56.132.154:8080'})     #私密代理的用法，比如账号为dxs 密码为mm

#构建了一个没有代理的处理器对象
nullproxy_handler= urllib2.ProxyHandler({})

if proxy_switch:
    opener=urllib2.build_opener(httpproxy_handler)
else:
    opener=urllib2.build_opener(nullproxy_handler)

#构建一个全局的opener，之后所有的请求都可以用urlopen()方式去发送,也附带Handler的功能
urllib2.install_opener(opener)


request=urllib2.Request('http://www.baidu.com/')
response=urllib2.urlopen(request)
print response.read()











