# -*- coding: UTF-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import ssl
import re
ssl._create_default_https_context=ssl._create_unverified_context

url='http://news.sina.com.cn/china/'
res=urllib.request.urlopen(url)
html=res.read().decode('utf-8')
# print(html)

soup=BeautifulSoup(html,'html.parser')


#这里代码抓的是主页中间部分的新闻
# news=soup.select('.blk12') #因为blk12是class，所以要加.
# # print(news)
# # print(news.select('a'))
# list=news[0].select('a')
# for l in list:
#     print(l['href'],end="  ")
#     print(l.getText())

#这里抓的是下翻一点后的    '最新消息'
for news in soup.select('.news-item'):
    if len(news.select('h2'))>0:
        h2=news.select('h2')[0].text
        time=news.select('.time')[0].text
        href=news.select('a')[0]['href']
        print(time,h2,href)

print("")

newsurl='http://news.sina.com.cn/c/nd/2017-09-27/doc-ifymksyw4335029.shtml'
res=urllib.request.urlopen(newsurl)
html=res.read().decode('utf-8')
# print(html)
soup=BeautifulSoup(html,'html.parser')

# print(soup.find(id='artibodyTitle'))  #两句一样的
# print(soup.select('#artibodyTitle'))

#获取标题
print(soup.select('#artibodyTitle')[0].text)    #因为是id，所以前面要加#

#取得时间和来源
# print(soup.select('.time-source')[0])      #因为是class，所以前面要加.
print(soup.select('.time-source')[0].contents)

# print(soup.select('.time-source')[0].contents[0].strip())   #取得时间并去除空格
timesource=soup.select('.time-source')[0].contents[0].strip()

#字符串转换成时间
from datetime import datetime
dt=datetime.strptime(timesource,'%Y年%m月%d日%H:%M')
print(dt)
#时间转换成字符串
print(dt.strftime('%Y-%m-%d'))

#取得来源
print(soup.select('.time-source span a')[0])
print(soup.select('.time-source span a')[0].text)




#获取正文
# print(soup.select('#artibody'))#找到正文所在的id为artibody的东西
# print(soup.select('#artibody p'))#找到id为artibody下面的p标签
# print(soup.select('#artibody p')[:-2])#最后两个没用，扔掉

#\u3000是空白的控制码
article=[]
for p in soup.select('#artibody p')[:-2]:
    article.append(p.text.strip())
print(article)

# print(' '.join(article))#以空格间隔方式连接list中的元素
# print('\n'.join(article))#以换行间隔方式连接list中的元素

#使用Python中著名的'一行文'来实现上面相同的效果
# print([p.text.strip() for p in soup.select('#artibody p')[:-2]])
print(' '.join([p.text.strip() for p in soup.select('#artibody p')[:-2]]))




#抓取编辑
print(soup.select('.article-editor')[0].text)
print(soup.select('.article-editor')[0].text.lstrip('责任编辑：'))   #去除'责任编辑：'5个字符

#抓取评论数
print(soup.select('#commentCount1'))    #从这里可以发现，数字并抓不到，可以确定是从javascript里来的
#经过谷歌浏览器分析，评论数藏在Network->JS->info.verson...的一个文件里，里面的Request URL为：
#http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-fymksyw4335029&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20&jsvar=loader_1506507136264_68898177
#所以我们解析上面的url即可

#评论的url
# newsurl='http://comment5.news.sina.com.cn/page/info?version=1&format=js\
#     &channel=gn&newsid=comos-fymksyw4335029&group=&compress=0&ie=utf-8&\
#     oe=utf-8&page=1&page_size=20&jsvar=loader_1506507136264_68898177'
评论url='http://comment5.news.sina.com.cn/page/info?version=1&format=js\
    &channel=gn&newsid=comos-fymksyw4335029&group=&compress=0&ie=utf-8&\
    oe=utf-8&page=1&page_size=20'   #去掉类似时间戳的东西  也没问题
#原新闻网页url：http://news.sina.com.cn/c/nd/2017-09-27/doc-ifymksyw4335029.shtml
res=urllib.request.urlopen(评论url)
comments=res.read().decode('utf-8')     #打开上面的url，实际上得到的是json数据
# print(html)

import json
jd=json.loads(comments.strip('var data=')) #去掉开头的'var data='
print(jd)
#取得总评论数量
print(jd['result']['count']['total'])

新闻url='http://news.sina.com.cn/c/nd/2017-09-27/doc-ifymksyw4335029.shtml'
newsid=新闻url.split('/')[-1].rstrip('.shtml').lstrip('doc-i')    #提取、切割字符串
print(newsid)
#用正则表达式的方式提取
m=re.search('doc-i(.+).shtml',newsurl)
print(m)
print(m.group(0))   #取得所有比对到的部分
print(m.group(1))   #取得比对到的第1个子组的部分

commentURL='http://comment5.news.sina.com.cn/page/info?version=1&format=js\
    &channel=gn&newsid=comos-{}&group=&compress=0&ie=utf-8&\
    oe=utf-8&page=1&page_size=20'
#注意上面留了个{}，可以直接塞东西，如下：
print(commentURL.format(newsid))



#定义获取评论数的方法
def getCommentCounts(newsurl):
    m = re.search('doc-i(.+).shtml', newsurl)
    newsid=m.group(1)
    评论url=commentURL.format(newsid)
    # print(评论url)
    res = urllib.request.urlopen(评论url)
    comments = res.read().decode('utf-8')
    jd = json.loads(comments.strip('var data='))  # 去掉开头的'var data='
    # print(jd)
    # 取得总评论数量
    # print(jd['result']['count']['total'])
    return jd['result']['count']['total']

newsurl='http://news.sina.com.cn/c/nd/2017-09-27/doc-ifymeswe0395550.shtml'
print(getCommentCounts(newsurl))

#整理抓取新闻信息的方法
def getNewsDetail(newsurl):
    result={}
    res = urllib.request.urlopen(newsurl)
    html = res.read().decode('utf-8')
    soup=BeautifulSoup(html,'html.parser')
    result['title']=soup.select('#artibodyTitle')[0].text
    result['newssource']=soup.select('.time-source span a')[0].text
    timesource=soup.select('.time-source')[0].contents[0].strip()
    result['dt']=datetime.strptime(timesource,'%Y年%m月%d日%H:%M')
    result['article']=' '.join([p.text.strip() for p in soup.select('#artibody p')[:-2]])
    result['editor']=soup.select('.article-editor')[0].text.lstrip('责任编辑：')
    result['comments']=getCommentCounts(newsurl)
    return result

newsurl='http://news.sina.com.cn/c/nd/2017-09-27/doc-ifymeswe0395550.shtml'
print(getNewsDetail(newsurl))














