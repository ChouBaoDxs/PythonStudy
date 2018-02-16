# -*- coding: UTF-8 -*-
#json模块提供了四个功能：dumps、dump、loads、load
#dumps：python——>json    #序列化时默认是ascii编码，可以添加参数ensure-ascii=False禁用ascii，按utf-8编码
#loads：json——>python


import urllib2
import json         #json的解析库，对应到lxml
import jsonpath     #json的解析语法，对应到Xpath
url='http://www.lagou.com/lbs/getAllCitySearchLabels.json'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36', }

request=urllib2.Request(url,headers=headers)
response=urllib2.urlopen(request)
html=response.read()

#把json形式的字符串转换成python形式的Unicode字符串
unicodestr=json.loads(html)

#python形式的列表
city_list=jsonpath.jsonpath(unicodestr,'$..name')

for item in city_list:
    print item

# json.dumps(city_list,ensure_ascii=False)  #禁用ascii编码
array=json.dumps(city_list,ensure_ascii=False)

with open('lagou_city.json','w') as f:
    f.write(array.encode('utf-8'))











