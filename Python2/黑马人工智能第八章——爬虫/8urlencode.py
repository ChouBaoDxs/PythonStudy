# -*- coding: UTF-8 -*-

import urllib
import urllib2

url='http://www.baidu.com/'

keyword=raw_input('请输入需要查询的字符串:')

wd={'wd':keyword}
wd=urllib.urlencode(wd)     #解码的话是urllib.unquote(str).decode('utf-8')
print wd

headers={"User-Agent":"Mozalla....."}

fullurl=url+'s?'+wd

resquest=urllib2.Request(fullurl,headers=headers)
response=urllib2.urlopen(resquest)
print response.read()
















