# -*- coding: UTF-8 -*-
import urllib,urllib2
from lxml import etree

#失败了，不可用

def loadPage(url):
    """
        作用：根据url发送请求，获取服务器响应文件
        url：需要爬取的url地址
        filename：处理的文件名
    """
    print "正在下载..."
    headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',}
    request=urllib2.Request(url,headers=headers)
    html=urllib2.urlopen(request).read()
    #解析HTML文档为HTML DOM模型
    content=etree.HTML(html)
    #返回所有匹配成功的列表集合
    link_list=content.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')    #失败了，匹配不到东西
    print link_list
    for link in link_list:
        fulllink='http://tieba.baidu.com'+link
        print fulllink
        # loadImage(fulllink)

#取出每个帖子里的每个图片链接
def loadImage(link):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36', }
    request=urllib2.Request(link,headers=headers)
    html=urllib2.urlopen(request).read()
    content=etree.HTML(html)
    #返回帖子里所有的图片链接的列表集合
    link_list=content.xpath('//img[@class="BED_Image"/@src')
    for link in link_list:
        writeImage(link)

def writeImage(link):
    """
        作用：将html内容写入到本地
        html：服务器相应文件内容
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36', }
    request=urllib2.Request(link,headers=headers)
    image=urllib2.urlopen(request).read()
    filename=link[-10:]
    with open(filename,'w') as f:
        f.write(image)
    print '-'*30

def tiebaSpider(url,beginPage,endPage):
    """
        作用：贴吧爬虫调度器，负责组合处理每个页面的url
        url：贴吧url的前部分
        beginPage：起始页
        endPage：结束页
    """
    for page in range(beginPage,endPage+1):
        pn=(page-1)*50
        filename='第'+str(page)+'页.html'
        fullurl=url+"&pn="+str(pn)
        # print fullurl
        loadPage(fullurl)
    print '谢谢使用'

if __name__=='__main__':
    kw=raw_input("请输入要爬取的贴吧名:")
    beginPage=int(raw_input("请输入起始页:"))
    endPage=int(raw_input("请输入结束页:"))

    #http://tieba.baidu.com/f?kw=macbookpro&pn=0
    url='http://tieba.baidu.com/f?'
    key=urllib.urlencode({"kw":kw})
    fullurl=url+key
    tiebaSpider(fullurl,beginPage,endPage)














