# -*- coding: UTF-8 -*-
import json
import urllib2
from lxml import etree

url='https://www.qiushibaike.com/8hr/page/1/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36', }

request=urllib2.Request(url,headers=headers)
html=urllib2.urlopen(request).read()

#响应返回的是字符串，解析为HTML_DOM模式
text=etree.HTML(html)

#返回所有段子的结点位置，contains()模糊查询方法，第一个参数是要匹配的标签,第2个参数是标签部分内容
node_list=text.xpath('//div[contains(@id,"qiushi_tag")]')
items={}
for node in node_list:
    #用户名
    username=node.xpath('./div/a/@title')[0]
    #图片链接
    image=node.xpath('.//div[@class="thumb"]//@src')
    #段子内容
    content=node.xpath('.//div[@class="content"]/span')[0].text
    #点赞
    zan=node.xpath('.//i')[0].text
    #评论
    comments=node.xpath('.//i')[1].text
    items={
        'username':username,
        'image':image,
        'content':content,
        'zan':zan,
        'comments':comments,
    }
    print items
    # with open('qiushi.json','a') as f:
    #     f.write(json.dumps(items,ensure_ascii=False).encode('utf-8')+'\n')












