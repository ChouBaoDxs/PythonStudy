# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/4 下午8:17'

import requests
import re
import pandas as pd
#http://hotel.elong.com/ajax/list/asyncsearch
url='http://hotel.elong.com/ajax/list/asyncsearch'

#这里是第2页
form_data={
    'code':7868460,
    'listRequest.areaID':'',
    'listRequest.bookingChannel':5,
    'listRequest.cardNo':192928,
    'listRequest.checkInDate':'2018-01-05 00:00:00',
    'listRequest.checkOutDate':'2018-01-06 00:00:00',
    'listRequest.cityID':'0101',
    'listRequest.cityName':'北京市',
    'listRequest.customLevel':11,
    'listRequest.distance':20,
    'listRequest.endLat':0,
    'listRequest.endLng':0,
    'listRequest.facilityIds':'',
    'listRequest.highPrice':0,
    'listRequest.hotelBrandIDs':'',
    'listRequest.isAdvanceSave':'false',
    'listRequest.isAfterCouponPrice':'true',
    'listRequest.isCoupon':'false',
    'listRequest.isDebug':'false',
    'listRequest.isLimitTime':'false',
    'listRequest.isLogin':'false',
    'listRequest.isMobileOnly':'true',
    'listRequest.isNeed5Discount':'true',
    'listRequest.isNeedNotContractedHotel':'false',
    'listRequest.isNeedSimilarPrice':'false',
    'listRequest.isReturnNoRoomHotel':'true',
    'listRequest.isStaySave':'false',
    'listRequest.isTrace':'false',
    'listRequest.isUnionSite':'false',
    'listRequest.keywords':'',
    'listRequest.keywordsType':0,
    'listRequest.language':'cn',
    'listRequest.listType':0,
    'listRequest.lowPrice':0,
    'listRequest.orderFromID':5485,
    'listRequest.pageIndex':3,      #翻页
    'listRequest.pageSize':20,      #每页的数量
    'listRequest.payMethod':0,
    'listRequest.personOfRoom':0,
    'listRequest.poiId':0,
    'listRequest.promotionChannelCode':0000,
    'listRequest.proxyID':'ZD',
    'listRequest.rankType':0,
    'listRequest.returnFilterItem':'true',
    'listRequest.sellChannel':1,
    'listRequest.seoHotelStar':0,
    'listRequest.sortDirection':1,
    'listRequest.sortMethod':1,
    'listRequest.starLevels':'',
    'listRequest.startLat':0,
    'listRequest.startLng':0,
    'listRequest.taRecommend':'false',
    'listRequest.themeIds':'',
    'listRequest.ctripToken':'5478aa46-5d24-4a41-a7b0-cffc6d949e81',
    'listRequest.elongToken':'jc0gny13-fc61-45da-9da0-7e76a4505a58',
}

header = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Content-Length':'1601',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    #cookie在这里没用
    'Cookie':'CookieGuid=76f2b354-2306-4246-a831-9027ebbcba37; ADHOC_MEMBERSHIP_CLIENT_ID1.0=a90de50f-c9e5-02fb-aac5-5c54fedf1702; s_visit=1; _fid=jc0gny13-fc61-45da-9da0-7e76a4505a58; _RF1=36.22.155.227; _RSG=1f49TPaguH51w9bjn_pmUA; _RDG=283b381f93a9e1206437cc2f4b747350a6; _RGUID=5478aa46-5d24-4a41-a7b0-cffc6d949e81; CitySearchHistory=0101%23%E5%8C%97%E4%BA%AC%E5%B8%82%23beijing%23; ShHotel=CityID=0101&CityNameCN=%E5%8C%97%E4%BA%AC%E5%B8%82&CityName=%E5%8C%97%E4%BA%AC%E5%B8%82&OutDate=2018-01-06&CityNameEN=beijing&InDate=2018-01-05; UM_distinctid=160c123aff78fb-05c12d50a66896-32607e02-1aeaa0-160c123aff89d0; CNZZDATA1264090578=763917975-1515068082-%7C1515068082; newjava1=03eb38321f47362048ca1230c8f58cac; JSESSIONID=F610063FCFB642F5B0DFE59E583ED543; SessionGuid=5bca5e74-1b3d-4778-8709-c6d11c5fcfe2; Esid=7e7f2d0e-c88e-4d40-8b29-b661b4559d34; fv=pcweb; s_cc=true; com.eLong.CommonService.OrderFromCookieInfo=Status=1&Orderfromtype=5&Isusefparam=0&Pkid=5485&Parentid=5000&Coefficient=0.0&Makecomefrom=0&Cookiesdays=0&Savecookies=0&Priority=9000; s_sq=elongcom%3D%2526pid%253Dhotel.elong.com%25252Fbeijing%2526pidt%253D1%2526oid%253Djavascript%25253Avoid(0)%2526ot%253DA',
    'Host':'hotel.elong.com',
    'Origin':'http://hotel.elong.com',
    'Referer':'http://hotel.elong.com/beijing/?yyue=a21bo.50862.201879',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
}

html=requests.post(url,data=form_data,headers=header)
# print html.json()

hotel_price=re.findall('<span class="h_pri_num ">(.*?)</span>',html.json()['value']['hotelListHtml'])
hotel_name=re.findall('target="_blank" title="(.*?)"><span',html.json()['value']['hotelListHtml'])

#lambda :匿名函数
data=list(map(lambda x:(hotel_price[x],hotel_name[x]),range(len(hotel_name))))
print(data)

df=pd.DataFrame(data)

#header：列名     index：序号     mode：读写方式   a+：追加
df.to_csv(r'yilong.csv',header=False,index=False,mode='a+',encoding='utf-8')

#lambda
f=lambda x:x*2
print(f(2))
list(map(f,range(10)))
print("******")
print( list(map(lambda x:str(x),range(1,50)))  )