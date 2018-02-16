# -*- coding: UTF-8 -*-
#爬这个http://www.neihan8.com/

import urllib2
import re

class Spider:
    def __init__(self):
        #初始化页码
        self.page=2

    def loadPage(self,page):
        """
            下载页面
        """
        if page==1:
            url='http://www.neihan8.com/article/index.html'
        else:
            url='http://www.neihan8.com/article/index_{}.html'.format(page)
        headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',}
        request=urllib2.Request(url,headers=headers)
        response=urllib2.urlopen(request)
        html=response.read()
        pattern=re.compile(r'<div class="desc">(.*?)</div>',re.S)
        content_list=pattern.findall(html)
        # for each in content_list:
        #     print each
        self.dealPage(content_list)

    def dealPage(self,content_list):
        """
            处理每页的段子
        """
        for each in content_list:
            each=each.replace('　','')
            # print each
            self.writePage(each)

    def writePage(self,content):
        """
            把每条段子逐个写入文件里
        """
        print '正在写入数据...'
        with open('duanzi.txt','a') as f:    #追加
            f.write(content+'\n')

    def startWork(self):
        """
            控制爬虫运行，即调度器
        """
        while True:
            command=raw_input('如果继续爬取，请按回车(退出输入quit):')
            if command=='quit':
                break
            self.loadPage(self.page)
            self.page+=1
        print '谢谢使用!'

if __name__=='__main__':
    spider=Spider()
    spider.startWork()










