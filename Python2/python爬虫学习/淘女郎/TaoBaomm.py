# -*- coding: UTF-8 -*-

import urllib2
from json import loads
import re
import user_agents

#淘女郎-美人库
#https://mm.taobao.com/search_tstar_model.htm?spm=5679.126488.640745.2.467046dcP692at&style=&place=city%3A

def getUrlList():
    req=urllib2.Request('https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8')
    req.add_header('user-agent',user_agents.headers())
    #这里的data也可以自己组装一下,这一串字符串的取法：在From Data那里
    html=urllib2.urlopen(req,data='q&viewFlag=A&sortType=default&searchStyle=&searchRegion=city%3A&searchFansNum=&currentPage=1&pageSize=100').read().decode('gbk').encode('utf-8')
    # print(html)
    json=loads(html)
    return json['data']['searchDOList']

def getInfo(userid):    #获取主页
    req=urllib2.Request('https://mm.taobao.com/self/aiShow.htm?userId=%s'%userid)
    req.add_header('user-agent',user_agents.headers())
    html=urllib2.urlopen(req).read().decode('gbk').encode('utf-8')
    print(html)

def getAlbumList(userid): #获取相册
    req=urllib2.Request('https://mm.taobao.com/self/album/open_album_list.htm?_charset=utf-8&user_id%%20=%s'%userid)
    req.add_header('user-agent', user_agents.headers())
    html = urllib2.urlopen(req).read().decode('gbk').encode('utf-8')
    # print(html)
    #XHR里请求相册列表的url：https://mm.taobao.com/self/album/open_album_list.htm?_charset=utf-8&user_id%20=176817195
    reg=r'class="mm-first" href="//(.*?)"'
    return re.findall(reg,html)[::2]    #隔一个元素取一个值

for i in getUrlList():
    # print i['userId']
    userId=i['userId']
    # getInfo(userId)   #去模特的主页
    for n in getAlbumList(userId):  #输出模特的相册主页
        print n
    break











