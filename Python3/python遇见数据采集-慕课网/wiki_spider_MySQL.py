# -*- coding: UTF-8 -*-

#引入开发包
import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql.cursors

# resp=urlopen("https://en.wikipedia.org/wiki/Main_Page").read().decode("utf-8")
# resp=request.urlopen("https://baike.baidu.com/")

#请求URL并把结果用UTF-8编码
resp=urlopen("https://en.wikipedia.org/wiki/Main_Page",context=ssl._create_unverified_context()).read().decode("utf-8")

#使用BeautifulSoup去解析
soup=BeautifulSoup(resp,"html.parser")
# print(soup)

#获取所有有以/wiki/开头的a标签的href属性
listUrls=soup.findAll('a',href=re.compile("^/wiki/"))

#输出所有词条对应的名称和URL
for url in listUrls:
    #过滤.jpg或.JPG结尾的URL
    if not re.search("\.(jpg|JPG)$",url["href"]):   #如果href是.jpg或.JPG结尾的，就不输出了，过滤掉
        # print(url["href"])
        # print(url.get_text(),"<---->",url["href"])
        #输出URL的文字和对应的链接
        print(url.get_text(),"<---->","https://en.wikipedia.org"+url["href"])
        #string只能获取一个文字   get_text()可以获取标签下所有的文字

        # 获取数据库链接
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            db='wikiurl',
            charset='utf8mb4'
        )

        try:
            #获取会话指针
            with connection.cursor() as cursor:
                #创建一条sql语句  这个反单引号是ESC下面那个按键
                sql="insert into `urls`(`urlname`,`urlhref`) values (%s,%s)"
                #执行sql语句
                cursor.execute(sql,(url.get_text(),"https://en.wikipedia.org"+url["href"]))
                #提交
                connection.commit()
        finally:
            connection.close()




















