# -*- coding: UTF-8 -*-

import urllib,urllib2

#通过抓包的方式获取url，并不是浏览器上显示的url
url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom='
headers = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
    'Referer':'http://fanyi.youdao.com/',
}

key=raw_input("请输入需要翻译的文字:")        #只能输入 '我爱python'

formdata={
    'i':key,
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt':'1507193861907',
    'sign':'b33757877a6cd6c59c4bb49da00b8fb4',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_CLICKBUTTION',
    'typoResult':'true',
}

data=urllib.urlencode(formdata)#对数据进行编码

request=urllib2.Request(url,data=data,headers=headers)

print urllib2.urlopen(request).read()











