# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import requests

# #时间戳
import time
# print time.time()     #1507276201.25
# print time.ctime()    #Fri Oct  6 15:50:01 2017
# print time.time() * 1000  #取毫秒

#把验证码写入文件，自己手动打开观看
def captcha(captcha_data):
    with open('captcha.jpg','wb') as f:
        f.write(captcha_data)
    text=raw_input('请输入验证码:')
    return text

def zhihuLogin():
    #构建一个Session对象，可以保存Cookie
    sess=requests.Session()
    headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',}

    #首先获取登录页面，找到需要POST的数据(_xsrf),同时会记录当前网页的Cookie值
    html=sess.get('https://www.zhihu.com/#signin',headers=headers).text
    #不用Session的话,是requests.get()

    bs=BeautifulSoup(html,'lxml')
    #获取页面里_xsrf值，_xsrf的作用是防止CSRF攻击(跨站请求伪造),通常叫跨域攻击，是利用网站对用户的一种信任机制来做坏事
    #跨域攻击通常是通过伪造成网站信任的用户的请求(利用Cookie)，盗取用户信息，欺骗web服务器
    #所以网站hi用过设置一个隐藏字段来存放这个字符串(通常是MD5)，这个字符串用来校验用户Cookie和服务器Session
    _xsrf=bs.find('input',attrs={'name':'_xsrf'}).get('value')
    # print _xsrf

    captcha_url='https://www.zhihu.com/captcha.gif?r=%d&type=login&lang=cn'% (time.time() *1000)
    # print captcha_url
    #拿到验证码的数据流
    captcha_data=sess.get(captcha_url,headers=headers).content
    #获取验证码里的文字，需要手动输入
    text=captcha(captcha_data)

    data={
        '_xsrf':_xsrf,
        'phone_num':'17706440586',
        'password':'d826842697',
        'captcha':text
    }

    response=sess.post('https://www.zhihu.com/login/email',data=data,headers=headers)
    # print response.text

    # #这样cookie就拿到了sess里，可以访问个人主页了
    # response=sess.get('xxxxxxxx',headers=headers)
    # # print response.text
    # # #写入文件
    # with open('my.html','w') as f:
    #     f.write(response.text.encode('utf-8'))

if __name__=='__main__':
    zhihuLogin()

















