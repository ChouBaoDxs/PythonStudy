# -*- coding: UTF-8 -*-

'''
模块：urllib，urllib2，re

1.反反爬：伪装浏览器
2.打开网址——获取网页源码
3.正则表达式匹配找到笑话：发布人+内容+阅读量+评论
4.缓存笑话
'''

import urllib,urllib2,re
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

class QSBK:
    #构造方法
    def __init__(self):
        self.pageIndex=1    #第一页
        self.user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        self.headers={'User-Agent':self.user_agent}
        self.stories=[]     #存放笑话的列表
        self.enable=False   #存放程序是否继续运行的变量

    #获取每一页的源码
    def getPage(self,pageIndex):
        try:
            url='https://www.qiushibaike.com/8hr/page/'+str(pageIndex)
            request=urllib2.Request(url,headers=self.headers)
            response=urllib2.urlopen(request)
            pageCode=response.read().decode('utf-8')
            # print pageCode
            return pageCode
        except urllib2.URLError,e:
            print u"链接糗事百科失败，错误原因",e

    #获取笑话
    def getPageItems(self,pageIndex):
        pageCode=self.getPage(pageIndex)    #调用方法获取页面源码
        if not pageCode:
            print "页面加载失败..."
            return None
        pattern=re.compile('<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?"number">(.*?)</i>.*?"number">(.*?)</i>',re.S)#提高效率 re.S:匹配换行符
        items=re.findall(pattern,pageCode)
        pageStories=[]
        for item in items:#发布人+内容+阅读量+评论
            it=item[1].replace('<span>',' ')
            it=it.replace('</span>',' ')
            # print item[0],it,item[2],item[3]
            pageStories.append([item[0].replace("\n",""),it.replace("\n",""),item[2].replace("\n",""),item[3].replace("\n","")])
        return pageStories

    #加载缓存，缓冲
    def loadPage(self):
        if self.enable==True:
            if len(self.stories)<2:
                pageStories=self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex+=1

    #敲回车输出段子
    def getOneStroy(self,pageStories,page):
        n=0
        for story in pageStories:
            input=raw_input('') #等待用户输入
            n+=1
            self.loadPage()
            if input=="Q":
                self.enable=False
                return
            print u"第%d页\t第%d条 发布人：%s\t%s" % (page,n,story[0],story[1])
            print u"这条糗事百科的阅读量是%s，评论是%s条" %(story[2],story[3])

    #开始方法
    def start(self):
        print u"正在读取糗事百科，按回车查看新段子，Q退出"
        self.enable=True
        self.loadPage()#加载一页内容
        nowPage=0
        while self.enable:
            if len(self.stories)>0:
                pageStories=self.stories[0]
                nowPage+=1
                del self.stories[0]
                self.getOneStroy(pageStories,nowPage)

spider=QSBK()
spider.start()




