# -*- coding: UTF-8 -*-
import os,sys
import urllib2,re,time,random
from bs4 import BeautifulSoup

def get_html(url):
    headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',}
    request=urllib2.Request(url,headers=headers)
    return urllib2.urlopen(request).read()

def mkdir(path):
    ie=os.path.exists(path)
    if not ie:
        os.makedirs(path)

def get_imgurl(html):
    soup=BeautifulSoup(html,'lxml', from_encoding='utf-8')
    gril=soup.find_all('div',class_='article-content')
    # print gril
    for img_url in gril:
        # print img_url
        try:
            imgurl=img_url.find('img')['data-original-image-url']
            img_urllist.append(imgurl)
            # print imgurl
        except:
            continue
    return img_urllist

def get_name(html):
    soup=BeautifulSoup(html,'lxml', from_encoding='utf-8')
    title=soup.find_all('div',class_='article-content')
    # print title
    for name in title:
        # print name
        try:
            name=name.find_all('a')[1].find('img')['alt']
            # print name
            title_list.append(name)
        except Exception as e:
            print '错误:',e
            continue
    return title_list

def saveimg(path,imgurl):
    if not os.path.exists(path):
        print '图片不存在'
        content=urllib2.urlopen(imgurl).read()
        with open(path,'wb') as f:
            f.write(content)
    else:
        print '这个图片url已经下载过了'

def main():
    #全局引用
    global img_urllist,title_list
    url='http://baozoumanhua.com/all/hot?page=1&sv=1514295901&yyue=a21bo.50862.201879'
    html=get_html(url)
    # print html
    get_imgurl(html)
    get_name(html)
    # print img_urllist
    # print title_list
    for i,j in zip(img_urllist,title_list):
        #拼接路径
        # print os.getcwd()
        # print type(os.getcwd())
        path=os.path.join(os.getcwd(),'暴走漫画') #os.getcwd()——获得当前路径
        # print path,j
        # print type(path)
        # print type(j.encode('utf-8'))
        try:
            # print path+'/'+j.encode('utf-8')
            mkdir(path+'/{}'.format(j.encode('utf-8')))
        except:
            print '创建文件失败'
            continue

        try:
            path=path+'/%s'%j.encode('utf-8')+'/%s'%i[-11:] #图片名取倒数11个长度
            print path
            print '正在保存文件',j
            saveimg(path,i)
        except Exception as e:
            print '保存图片失败','原因',e
            continue

    time.sleep(2)
    img_urllist=[]
    title_list=[]


if __name__=='__main__':
    img_urllist=[]
    title_list=[]
    main()






