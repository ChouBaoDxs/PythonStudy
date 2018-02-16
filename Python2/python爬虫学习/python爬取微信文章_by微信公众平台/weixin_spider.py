# -*- coding: UTF-8 -*-
import requests
import json
import re
import random

import time

from data_my import weixin_gzh

gzh_list = weixin_gzh.DATA.gzh_list

with open('cookies.txt','r') as file:
    cookie=file.read()
cookies=json.loads(cookie)
# print cookies

query='华尔街见闻'
url='https://mp.weixin.qq.com/'

headers = {
    'Host':'mp.weixin.qq.com',
    'Referer':'https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2&action=edit&isNew=1&type=10&lang=zh_CN&token=123383238',
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0"
    }

response=requests.get(url,cookies=cookies)
token=re.findall(r'token=(\d+)',str(response.url))[0]
# print token
#查询公众号的url
searchbiz_url='https://mp.weixin.qq.com/cgi-bin/searchbiz?'
#查询公众号里文章的url
appmsg_url = 'https://mp.weixin.qq.com/cgi-bin/appmsg?'

for query in gzh_list:
    search_dict={
        'action':'search_biz',
        'token':token,
        'lang':'zh_CN',
        'f':'json',
        'ajax':'1',
        'random':random.random(),
        'query':query,
        'begin':'0',
        'count':'5',
    }

    #7月份还是用post请求做的
    # search_url='https://mp.weixin.qq.com/cpi-bin/operate_appmsg?sub=check_appmsg_......'
    # search_response=requests.post(search_url,cookies=cookies,data=data,headers=headers)
    # print search_response.text

    #现在已经变成get请求了,url也变了

    search_response = requests.get(searchbiz_url, cookies=cookies, params=search_dict,headers=headers)
    # print(search_response)
    # print(search_response.json())

    try:
        fakeid=search_response.json().get('list')[0].get('fakeid')
    except:
        continue

    appmsg_dict = {
        'token': token,
        'lang': 'zh_CN',
        'f': 'json',
        'ajax': '1',
        'random': random.random(),
        'action': 'list_ex',
        'begin': '0',
        'count': '5',
        'query': '',
        'fakeid': fakeid,
        'type': '9'
    }

    appmsg_response = requests.get(appmsg_url, cookies=cookies, params=appmsg_dict,headers=headers)

    begin = 0;
    query_id_data = {
        'token': token,
        'lang': 'zh_CN',
        'f': 'json',
        'ajax': '1',
        'random': random.random(),
        'action': 'list_ex',
        'begin': '{}'.format(str(begin)),
        'count': '5',
        'query': '',
        'fakeid': fakeid,
        'type': '9'
    }

    query_fakeid_response = requests.get(appmsg_url, cookies=cookies, headers=headers, params=query_id_data)
    fakeid_list = query_fakeid_response.json().get('app_msg_list')

    # 没必要爬太多文章，一个公众号爬最近的两三篇就可以
    flag = 0
    try:
        for item in fakeid_list:
            #decode的作用是将其他编码的字符串转换成unicode编码
            #encode的作用是将unicode编码转换成其他编码的字符串
            print('微信公众号：'.encode('gb2312'), weixin_gzh.DATA.gzh_dict[query].decode('utf-8').encode('gb2312'))
            print('文章标题：', item.get('title')),
            print('文章链接：', item.get('link')),
            print('')
            flag += 1
            time.sleep(random.uniform(5,10))  # 防止操作太快，被屏蔽

            if (flag == 1): break  # 查两篇就直接退出去
    except:
        continue














