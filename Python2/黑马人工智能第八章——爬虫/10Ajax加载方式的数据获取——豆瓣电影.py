# -*- coding: UTF-8 -*-
import urllib,urllib2
#https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=50&page_start=0
url='https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend'
headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
}

formdata={
    'page_limit':'20',
    'page_start':'0',
}

data=urllib.urlencode(formdata)

request=urllib2.Request(url,data=data,headers=headers)

print urllib2.urlopen(request).read()












