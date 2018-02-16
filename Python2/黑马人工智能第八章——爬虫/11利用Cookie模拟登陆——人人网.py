# -*- coding: UTF-8 -*-
import urllib,urllib2

url='http://www.renren.com/959769247/profile'
headers={
    'Accept':'*/*',
    # 'Accept-Encoding':'gzip, deflate',    #解压缩，绝对不要弄这个
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Content-Type':'application/x-www-form-urlencoded',
    #↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    'Cookie':'anonymid=j8ean22h-90s6ye; depovince=GW; _r01_=1; JSESSIONID=abcLThlFvQqYHhUSo-R7v; ick_login=4d86643d-595a-4c5b-b2a6-ffad0b11ff74; t=8910ca84cf523d167d693aa0da07bff97; societyguester=8910ca84cf523d167d693aa0da07bff97; id=959769247; xnsid=1402b508; jebecookies=7d219991-6eb4-4a28-bc46-9fb6834016ee|||||; ch_id=10016; springskin=set; jebe_key=c26c740b-3473-47a6-bf47-49a1acdc4ed5%7C80b227b0646aff5b53fb830735eaa6f5%7C1507197803686%7C1%7C1507197803941; XNESSESSIONID=a20c0a54417c; WebOnLineNotice_959769247=1; wp_fold=0',
    'Host':'www.renren.com',
    # 'Referer:http':'//www.renren.com/959769247/profile',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
}

request=urllib2.Request(url,headers=headers)

response=urllib2.urlopen(request)

print response.read()















