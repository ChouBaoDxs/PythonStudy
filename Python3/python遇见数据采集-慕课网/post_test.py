# -*- coding: UTF-8 -*-

from urllib.request import urlopen
from urllib.request import Request
from urllib import parse

req=Request("http://trains.ctrip.com/TrainBooking/SearchTrain.aspx")

postData=parse.urlencode([
    #注意这里↓必须要有空格
    ("from", "hangzhou"),   #这里要跟逗号
    ("to", "beijing"),      #这里要跟逗号
    ("day", "2")
])

req.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")
resp=urlopen(req,data=postData.encode('utf-8'))

# print(resp.read().decode("utf-8"))
print(resp.read().decode('gb2312')) #为什么是gb2312呢，去那个网页查看源代码，找到charset=gb2312



