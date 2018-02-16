# -*- coding: UTF-8 -*-

import urllib.request
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

url='https://weibo.com/'

#使用cookies进入网站
data={
    'Cookie':'SINAGLOBAL=5446292130856.13.1506389621601; un=17706440586; wvr=6; httpsupgrade_ab=SSL; YF-V5-G0=4955da6a9f369238c2a1bc4f70789871; SSOLoginState=1506681696; SCF=AvKO4O6hIpdrrjost7dG6k8DzpKqBtWnCj0xUYE0qVIM3SBmGT1t72VKgYd9qJP_KpfBaVijPPQ1tn5Ra2kZQ3E.; SUB=_2A250ylMxDeRhGeNG7FET9CjNzjSIHXVXvsP5rDV8PUNbmtBeLW_ukW9yUe8Cx5UPNYrektsuZfLkDSjBRA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW_GQAb6jgWRD4eBsO4X4F.5JpX5KMhUgL.Fo-RS0eEShqpSKn2dJLoIpjLxKnL1hMLB-BLxK-L12eL1h-LxKBLBonLBoqt; SUHB=0Jvgxew60eTTWA; ALF=1538217695; wb_cusLike_5873246158=N; _s_tentry=login.sina.com.cn; UOR=www.cngold.org,widget.weibo.com,login.sina.com.cn; Apache=5506470788721.225.1506681699069; ULV=1506681699080:2:2:2:5506470788721.225.1506681699069:1506389621606; YF-Page-G0=ab26db581320127b3a3450a0429cde69',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

data_first=urllib.request.Request(url=url,headers=data)
# weibo_data=urllib.request.urlopen(url).read().decode('utf-8','ignore')
weibo_data=urllib.request.urlopen(data_first).read().decode('utf-8')
#在网址前面加上 'view-source:'  就可以看到源代码 针对某些不能右键查看源代码的网站
print(weibo_data)















