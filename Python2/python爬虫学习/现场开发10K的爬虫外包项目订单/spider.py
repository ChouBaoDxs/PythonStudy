# -*- coding: UTF-8 -*-
import urllib,urllib2
import cookielib    #存cookie用的
from json import loads

c=cookielib.LWPCookieJar()
cookie=urllib2.HTTPCookieProcessor(c)
opener=urllib2.build_opener(cookie) #让服务器能认识到请求都是来自同一个浏览器
urllib2.install_opener(opener)

#爬取认证认可业务信息统一查询平台:  cx.cnca.cn


#Referer:来源  就在User-Agent上面复制
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
         'Referer':'http://cx.cnca.cn/rjwcx/web/cert/publicCert.do?progId=10&title=%E8%AE%A4%E8%AF%81%E7%BB%93%E6%9E%9C%0A%09%20%20%20%20%20%20%20%20'
}

def getList():
    req=urllib2.Request('http://cx.cnca.cn/rjwcx/web/cert/queryOrg.do?progId=10')
    req.headers=headers

    #下载验证码的图片   用下面这种方式的话，服务器无法确认验证码和请求来自同一人，所以要通过opener
    # urllib.urlretrieve('http://cx.cnca.cn/rjwcx/checkCode/rand.do?d=1506841797729','code.png')
    with open('code.png','wb') as fn:
        #这个图片地址，直接在验证码那个图片上右键->复制图片地址
        fn.write(opener.open('http://cx.cnca.cn/rjwcx/checkCode/rand.do?d=1506841797729','code.png').read())

    code=input('请输入验证码:')

    data={
        'certNumber':'',
        'orgName':'漳州灿坤实业有限公司',
        'queryType':'public',
        'checkCode':code,    #验证码
    }
    data=urllib.urlencode(data) #post的data不能直接传，要先转换
    # html=urllib2.urlopen(req,data=data).read()
    html=opener.open(req,data=data).read()
    # print u'\u9A8C\u8BC1\u7801\u4E0D\u6B63\u786E'     #'验证码不正确'的Unicode
    # print html
    result=loads(html)  #将标准json形式的字符串转换为json
    return result['data']

def getCertList(orgName,orgCode,checkC,randomCheckCode):
    req=urllib2.Request('http://cx.cnca.cn/rjwcx/web/cert/list.do?progId=10')
    req.headers=headers
    data={
        'orgName': orgName,
        'orgCode': orgCode,
        'method': 'queryCertByOrg',
        'needCheck': 'false',
        'checkC': checkC,
        'randomCheckCode': randomCheckCode,
        'queryType': 'public',
        'page': '1',
        'rows': '10',
        'checkCode':'',
    }
    data = urllib.urlencode(data)  # post的data不能直接传，要先转换
    html=opener.open(req,data=data).read()
    # print html
    result=loads(html)  #将标准json形式的字符串转换为json
    return result['rows']

def getCertInfo(rzjgId,certNo,checkC):
    req=urllib2.Request('http://cx.cnca.cn/rjwcx/web/cert/index.do?url=web/cert/showZyxGy.do%3FrzjgId={}%26certNo={}%26checkC={}'.format(rzjgId,certNo,checkC))
    print 'http://cx.cnca.cn/rjwcx/web/cert/index.do?url=web/cert/showZyxGy.do%3FrzjgId={}%26certNo={}%26checkC={}'.format(rzjgId,certNo,checkC)
    req.headers=headers
    html=opener.open(req).read()
    print html


for i in getList():
    # print i
                            #.encode('utf-8')    把Unicode的数据编码成utf-8
    for n in getCertList(i['orgName'].encode('utf-8'),i['orgCode'],i['checkC'],i['randomCheckCode']):
        getCertInfo(n['rzjgId'],n['certNumber'],n['checkC'])
        break
    #点击证书编号后的url
    #http://cx.cnca.cn/rjwcx/web/cert/show.do?rzjgId=CNCA-R-2002-001&certNo=00114Q26950R7L/3502&checkC=-1535838625
    #http://cx.cnca.cn/rjwcx/web/cert/index.do?url=web/cert/showZyxGy.do%3FrzjgId=CNCA-RF-2002-07%26certNo=R2_130800590SHA-001%26checkC=-536800051
    #http://cx.cnca.cn/rjwcx/web/cert/index.do?url=web/cert/show3C.do%3FrzjgId=01%26certNo=2013010702607951%26checkC=1859215330
    #http://cx.cnca.cn/rjwcx/web/cert/index.do?url=web/cert/showZyxGy.do%3FrzjgId={}%26certNo={}%26checkC={}
    break












