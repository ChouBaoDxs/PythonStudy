# -*- coding: UTF-8 -*-
import json
import urllib
from bs4 import BeautifulSoup
import requests
import re

class Wx_Spider(object):

    def __init__(self,key):
        self.key=key
        #搜索地址
        self.sougou_search_url='http://weixin.sogou.com/weixin?query={}&_sug_type_=&s_from=input&_sug_=n&type=1&page={}&ie=utf8'
        # print self.sougou_search_url.format('python',1)
        self.headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
        #代理池接口
        self.proxy_url='http://172.16.85.110:8000'   #设置代理ip  应该从ip池里面随机返回一个ip地址

    def get_proxy(self):
        #请求代理池，随机返回ip
        text=requests.get(self.proxy_url).text  #text就是ip
        proxy={
            'http':'http://{}'.format(text),
            'https':'https://{}'.format(text)
        }
        print ('当前代理是：http://{}'.format(text))
        return proxy

    def get_search_response(self,url,proxy=None,total=3):
        if total==0:
            return None
        try:
            content=requests.get(url,headers=self.headers,proxies=proxy).content
        except Exception as e:
            print '代理异常，重试'
            total-=1
            return self.get_search_response(url,proxy=self.get_proxy(),total=total)

        if '输入验证码' in content:
            total-=1
            return self.get_search_response(url,proxy=self.get_proxy(),total=total)
        else:
            return content

    def get_wx_hkmovie(self,sougou_response):
        soup=BeautifulSoup(sougou_response,'lxml')
        return [i.find('p',class_='tit').find('a')['href'] for i in soup.find_all('div',class_='txt-box')]
        #上面的一行文相当于
        # for i in soup.find_all('div',class_='txt-box'):
        #     i.find('p').find('a')['href']

    def get_wx_article(self,response):
        req=re.compile(r'var msgList = (.*?}}]});',re.S)    #忽略换行
        article_urls=re.findall(req,response)
        # print (article_urls)
        return json.loads(article_urls[0])

    def parse_article(self,response):
        article_list=response.get('list')
        articles=[]
        for article in article_list:
            # print article
            article_author=article.get('app_msg_ext_info').get('author')
            article_url=article.get('app_msg_ext_info').get('content_url')
            article_title=article.get('app_msg_ext_info').get('title')
            article_addtime=article.get('comm_msg_info').get('datetime')#时间戳
            print article_author
            print article_url
            print article_title
            # print article_addtime
            break

    def main(self):
        content=self.get_search_response(self.sougou_search_url.format(self.key,1)) #只拿第一页
        # print (self.get_wx_hkmovie(content))
        for url in (self.get_wx_hkmovie(content)):
            html=self.get_search_response(url)
            article_dict=self.get_wx_article(html)
            self.parse_article(article_dict)
            break

# if __name__=='__main__':#判断是不是当前文件执行
#     print (__name__)

key='华尔街见闻'
print key
spider=Wx_Spider(key)
spider.main()

#代理是本地不能访问之后再加的










