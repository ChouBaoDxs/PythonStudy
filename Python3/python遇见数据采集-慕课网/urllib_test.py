# -*- coding: UTF-8 -*-

from urllib import request
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

#方法一：
resp=request.urlopen("http://www.baidu.com")
print(resp.read())
print(resp.read().decode("utf-8"))

#方法二：
#模拟真实浏览器
#携带User-Agent头
'''
req=request.Request(url)
req.add_header(key,value)
resp=request.urlopen(req)
print(resp.read().decode("utf-8"))
'''
req=request.Request("http://www.baidu.com")
#如何查看User-Agent呢，谷歌浏览器地址栏里输入about:version，用户代理那几行就是
req.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")
resp=request.urlopen(req)
print(resp.read().decode("utf-8"))

#方法三：
#使用urllib发送POST请求
#导入urllib库下面的parse
"from urllib import parse"
#使用urlencode生成post数据
'''
postData=parse.urlencode([
    (key1,val1)
    (key2,val2)
    (key3,val3)
])
'''
#使用postData发送post请求
"request.urlopen(req,data=postData.encode('utf-8'))"
#得到请求状态
"resp.status"
#得到服务器的类型
"resp.reason"







