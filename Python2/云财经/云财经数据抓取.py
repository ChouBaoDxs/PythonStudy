# -*- coding: UTF-8 -*-

#http://www.yuncaijing.com/story/details/id_1.html
#http://www.yuncaijing.com/story/details/id_578.html

import random
import requests
import re
import time

from bs4 import BeautifulSoup
import xlwt
from xlrd import open_workbook
from xlutils.copy import copy

class YUNCAIJING:
    def init(self):
        self.concept_info_data=[] #存储各个概念信息的列表
        self.company_info_data=[]    #存储各个企业的列表
        self.invalid_url_data=[]  #存储无效url的列表

    def main(self,x):
        # for i in range(1,3000):  #云财经概念网址有3000个左右，有效1600左右
        for i in range(x,x+100):
            # time.sleep(random.uniform(2, 5))  # 防止操作太快
            time.sleep(random.uniform(1, 1))  # 防止操作太快
            url='http://www.yuncaijing.com/story/details/id_{}.html'.format(i)
            try:
                self.getHtml_By_Url(url)
            except:
                print '这个页面无效:'+str(i)
                list=[]
                list.append(url)
                self.invalid_url_data.append(list)

            # break
        # url = 'http://www.yuncaijing.com/story/details/id_29.html'
        # getHtml_By_Url(url)

    def getHtml_By_Url(self,url):
        headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',}
        response=requests.get(url,headers=headers)
        response.encoding = 'utf-8'
        html = response.content
        # print html
        # print type(html)
        print url
        bs = BeautifulSoup(html, 'lxml', from_encoding='utf-8')
        # print '概念名称和简介:'
        page_title = bs.find('nav', class_='page-title')
        # print page_title
        # print '*******************'
        temp = str(page_title.find('h1'))
        # print temp
        # print '*******************'
        pattern = re.compile(r'>(.*?)<span data-module="layer">', re.S)
        concept_name = re.findall(pattern, temp)
        concept_name = concept_name[0].strip().replace("\n", "").replace("概念", "")
        # print '概念名称:' + concept_name
        # print '*******************'
        pattern2 = re.compile(r'<span data-content="">(.*?)</span>', re.S)
        concept_abstract = re.findall(pattern2, temp)
        concept_abstract = concept_abstract[0].strip().replace("\n", "")
        # print '概念简介:' + concept_abstract

        # print '*******************'
        # print '最新进展:'
        abreast_of_advances = bs.find('article')
        '''
        temp=str(abreast_of_advances.get_text().strip().replace("\n", "").encode('utf-8'))
        # print temp
        print re.sub(r' +',' ',temp)
        '''
        try:
            a = abreast_of_advances.find('a').get_text().strip().replace("\n", "").replace(" ", "").encode('utf-8').replace("最新进展：",                                                                                                       "")
        except:
            a='此概念无最新进展'
        # print '最新进展:' + a

        try:
            span = abreast_of_advances.find('span').get_text().strip().replace("\n", "").encode('utf-8')
        except:
            span='此概念无最新进展'
        # print '时间:' + span

        try:
            p = abreast_of_advances.find('p').get_text().strip().replace("\n", "").encode('utf-8')
        except:
            p='此概念无最新进展'
        # print '详情:' + p

        #将该概念加入概念信息列表
        concept_element = [url,concept_name,concept_abstract,a,span,p]
        self.concept_info_data.append(concept_element)

        # print '*******************'
        # print '相关股票:'
        container_right = bs.find('div', class_='container-right')
        # print container_right
        related_stocks = container_right.find('tbody')
        # print related_stocks
        related_stocks_list = related_stocks.find_all('tr')
        # print related_stocks_list
        for each in related_stocks_list:
            # print each
            info = each.find_all('td')
            # 股票名称
            stock_name = info[0].get_text().strip().replace("\n", "").encode('utf-8')
            # print '股票名称:' + stock_name,
            # 股票价格
            stock_price = info[1].get_text().strip().replace("\n", "").encode('utf-8')
            # print '股票价格:' + stock_price,
            # 涨跌幅
            price_rise_and_fall = info[2].get_text().strip().replace("\n", "").encode('utf-8')
            # print '涨跌幅:' + price_rise_and_fall,
            # 关联原因
            associated_cause = info[3].find_all('span')[1].get_text().strip().replace("\n", "").encode('utf-8')
            # print '关联原因:' + associated_cause,
            # 关联度
            correlation_degree = info[4].get_text().strip().replace("\n", "").encode('utf-8')
            # print '关联度:' + correlation_degree,
            # print ''

            #将该公司加入公司信息列表
            company_element=[concept_name,stock_name,associated_cause,correlation_degree]
            self.company_info_data.append(company_element)


    def save_data(self,x):
        #保存到excel
        write_to_excel('concept_info_data.xls',self.concept_info_data)
        write_to_excel('company_info_data{}.xls'.format(x),self.company_info_data)
        write_to_excel('invalid_url_data.xls',self.invalid_url_data)

def write_to_excel(file_name,data_list):
    '''
    根据文件名和数据列表将数据写入到excel
    :param file_name:读写的文件名
    :param data_list:要追加写入的列表型数据
    :return:
    '''
    try:
        rexcel = open_workbook(file_name)  # 用wlrd提供的方法读取一个excel文件
    except:
        #打开失败说明还不存在这个excel,那就新建一个
        workbook = xlwt.Workbook(encoding='utf-8')
        booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
        workbook.save(file_name)
        rexcel = open_workbook(file_name)

    rows = rexcel.sheets()[0].nrows  # 用wlrd提供的方法获得现在已有的行数
    excel = copy(rexcel)  # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
    table = excel.get_sheet(0)  # 用xlwt对象的方法获得要操作的sheet

    for i, row in enumerate(data_list):
        for j, col in enumerate(row):
            # print col
            # print type(col)
            table.write(i+rows, j, col.decode('utf-8'))

    excel.save(file_name)  # xlwt对象的保存方法，这时便覆盖掉了原来的excel

if __name__=='__main__':

    x=0
    i=0
    while x<3000:
        print x
        yuncaijing = YUNCAIJING()
        yuncaijing.init()
        yuncaijing.main(x)
        yuncaijing.save_data(i)
        x+=100
        i+=1











