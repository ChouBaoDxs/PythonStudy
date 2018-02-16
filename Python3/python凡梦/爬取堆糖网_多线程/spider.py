# -*- coding: UTF-8 -*-

#爬取堆糖网搜索'校花'之后的图片

'''
%E6%A0%A1%E8%8A%B1='校花'
https://www.duitang.com/napi/blog/list/by_search/?kw=%E6%A0%A1%E8%8A%B1&type=feed&include_fields=top_comments
%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Csender%2Calbum&_type=&start=24
&_=1506918669225
删除没必要的东西之后：
https://www.duitang.com/napi/blog/list/by_search/?kw=%E6%A0%A1%E8%8A%B1&start=24

自己修改这个链接,增加一个参数，直接取1000张图片，原来默认是24张，但是这个堆糖网上限是一次100张
'https://www.duitang.com/napi/blog/list/by_search/?kw=%E6%A0%A1%E8%8A%B1&start=0&limit=1000'
'''

'''
https://www.duitang.com/search/?kw=%E4%B8%AD%E6%96%87&type=feed
%E4%B8%AD%E6%96%87='中文'
url编码，本质上去ASCII编码
'''

import requests
import urllib.parse

#多线程
import threading
#初始化,设置最大线程锁,一次10个线程,这个线程锁一定要加，不然CPU要爆炸
thread_lock=threading.BoundedSemaphore(value=10)

#通过url获取数据
def get_page(url):
    #requests.get 自带 json.loads
    page=requests.get(url)
    page=page.content
    #将bytes转成字符串
    page=page.decode('utf-8')
    return page

#label是搜索关键字
def pages_from_duitang(label):
    pages=[]
    url='https://www.duitang.com/napi/blog/list/by_search/?kw={}&start={}&limit=1000'
    # 将中文转成url编码，即ASCII编码
    label=urllib.parse.quote(label)
    for index in range(0,3600,100):
        u=url.format(label,index)
        print(u)
        page=get_page(u)
        pages.append(page)
    return pages

#处理字符串的切片函数,把下面那种东西切出url
'"path":"https://b-ssl.duitang.com/uploads/item/201606/11/20160611113213_F5uTh.jpeg"'
def findall_in_page(page,startpart,endpart):
    all_string=[]
    end=0
    while page.find(startpart,end)!=-1: #find函数：从end开始找，找startpart  -1代表找不到
        start=page.find(startpart,end)+len(startpart)
        end=page.find(endpart,start)
        string=page[start:end]
        all_string.append(string)
    return all_string

def pic_urls_from_pages(pages):
    pic_urls=[]
    for page in pages:
        urls=findall_in_page(page,'"path":"','"')
        #extend()接受一个列表参数，把参数列表的元素添加到列表的尾部，append()接受一个对象参数，把对象添加到列表的尾部
        pic_urls.extend(urls)
    return pic_urls

#根据url和名字下载图片
def download_pics(url,n):   #n图片的名字
    r=requests.get(url,timeout=3)
    path='pictures/'+str(n)+'.jpg'
    with open(path,'wb') as f:
        f.write(r.content)
    #下载完解锁
    thread_lock.release()

#label是要下载图片的关键字
def main(label):
    pages=pages_from_duitang(label)
    pic_urls=pic_urls_from_pages(pages)
    n=0 #图片的名字
    for url in pic_urls:
        n+=1
        if(n==50):break #不要爬太多，50张就退出
        print('正在下载第{}张图片'.format(n))
        #先上锁
        thread_lock.acquire()

        t=threading.Thread(target=download_pics,args=(url,n))
        t.start()

main('校花')

