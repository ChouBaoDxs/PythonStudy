# -*- coding: UTF-8 -*-
import requests
import re
from my_utils.cut import Cut_Label

import pymysql
db=pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    db='movie',
    charset='utf8',
)

cursor=db.cursor()

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
#爬取电影天堂

#http://www.dytt8.net/html/gndy/dyzz/index.html

def getMovieList(page):
    # response=requests.get('http://www.dytt8.net/html/gndy/dyzz/index.html')#post get
    response=requests.get('http://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'.format(page))#post get
    response.encoding='gb2312'
    # print (response.text)
    html=response.text
    # print html
    # <a href="/html/gndy/dyzz/20170926/55117.html" class="ulink">2017年高分科幻动作《蜘蛛侠：英雄归来》HD中英双字幕</a>
    reg=r'<a href="(.*?)" class="ulink">(.*?)</a>'
    reg=re.compile(reg)
    # print (re.findall(reg,html))
    return re.findall(reg,html)

def getMovieContent(url,title):
    response=requests.get('http://www.dytt8.net{}'.format(url))
    response.encoding='gb2312'
    html=response.text
    # print html

    # reg=r'<div class="co_content8">([\s\S]*?)<center></center>'       #和下面两句一样的效果

    reg=r'<div class="co_content8">(.*?)<strong>.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(.*?)">'
    reg=re.compile(reg,re.S)

    #不断搜索的过程中可能出现下标越界的问题，这里直接try
    try:
        content,link=re.findall(reg,html)[0]
        content=Cut_Label.cut(content).replace('\n','')
        sql="insert into `dianyingtiantang`(`title`,`content`,`link`) values (%s,%s,%s)"
        cursor.execute(sql,(title,content.replace("'","\\'"),link))#执行sql语句             #注意字段的编码也要是utf-8
        db.commit()
    except:
        return

    print '*****************************'
    print '标题:',title
    print '*****************************'
    print '说明:',content
    print '*****************************'
    print '下载地址:',link


count=0
for page in range(1,166):
    for url,title in getMovieList(page):
        # print (url,title)
        getMovieContent(url,title)
        count+=1
        if count==2:break
        # break

    break

db.close()










