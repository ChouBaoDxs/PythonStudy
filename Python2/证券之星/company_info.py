# -*- coding: UTF-8 -*-
import random
import requests
import re
import time

from bs4 import BeautifulSoup
import xlwt
from xlrd import open_workbook
from xlutils.copy import copy


class ZHENGQUANZHIXING:
    def __init__(self):
        self.company_info_data=[]

    def getHtml_By_Url(self, url, i):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36', }
        response = requests.get(url, headers=headers)
        response.encoding = 'gb2312'
        html = response.text
        # print html

        bs = BeautifulSoup(html, 'lxml', from_encoding='gb2312')
        # 公司信息所在的div
        con_gsjj_wrap = bs.find('div', class_='con gsjj_wrap')
        # print con_gsjj_wrap
        temp = str(con_gsjj_wrap)

        # 公司名称
        pattern = re.compile(r'<td class="thead_1" width="120">公司名称</td>.*?<td>(.*?)<', re.S)
        company_name = re.findall(pattern, temp)
        #如果公司名为空，则说明这个公司已经退市，不存在
        if len(company_name)==0:return
        print company_name[0]

        # 上市日期
        pattern = re.compile(r'<td class="thead_1">上市日期</td>.*?<td>(.*?)</td>', re.S)
        launch_date = re.findall(pattern, temp)
        # print launch_date[0]

        # 注册地址
        pattern = re.compile(r'<td class="thead_1">注册地址</td>.*?<td>(.*?)</td>', re.S)
        registered_address = re.findall(pattern, temp)
        # print registered_address[0]

        # 注册资本
        pattern = re.compile(r'<td class="thead_1">注册资本\(万元\)</td>.*?<td>(.*?)</td>', re.S)
        registered_capital = re.findall(pattern, temp)
        # print registered_capital[0]

        # 法人代表
        pattern = re.compile(r'<td class="thead_1">法人代表</td>.*?<td>(.*?)</td>', re.S)
        legal_representative = re.findall(pattern, temp)
        # print legal_representative[0]

        temp_bs = BeautifulSoup(legal_representative[0], 'lxml')
        # print temp_bs.find('a').get_text()
        legal_representative=temp_bs.find('a').get_text()

        # 董事会秘书
        pattern = re.compile(r'<td class="thead_1">董事会秘书</td>.*?<td>(.*?)</td>', re.S)
        board_secretary = re.findall(pattern, temp)
        # print board_secretary[0]

        temp_bs = BeautifulSoup(board_secretary[0], 'lxml')
        # print temp_bs.find('a').get_text()
        board_secretary=temp_bs.find('a').get_text()

        # 公司简介
        pattern = re.compile(r'<td class="bg_td_3">公司简介</td>.*?<td>(.*?)</td>', re.S)
        company_profile = re.findall(pattern, temp)
        # print company_profile[0]

        #所属行业
        pattern = re.compile(r'<td class="thead_1">所属行业</td>.*?<td>(.*?)</td>', re.S)
        industry = re.findall(pattern, temp)
        # print industry[0]

        temp_bs = BeautifulSoup(industry[0], 'lxml')
        # print temp_bs.find('a').get_text()
        industry=temp_bs.find('a').get_text()

        #所属地域
        try:
            pattern = re.compile(r'<td class="thead_1">所属地域</td>.*?<td>(.*?)</td>', re.S)
            area = re.findall(pattern, temp)
            # print area[0]

            temp_bs = BeautifulSoup(area[0], 'lxml')
            # print temp_bs.find('a').get_text()
            area=temp_bs.find('a').get_text()
        except:
            area=''

        #所属板块
        pattern = re.compile(r'<td class="thead_2">所属板块</td>.*?<td>(.*?)</td>', re.S)
        plate = re.findall(pattern, temp)
        # print plate[0]

        temp_bs = BeautifulSoup(plate[0], 'lxml')
        # print temp_bs.find_all('a')
        plate_string=''
        for each in temp_bs.find_all('a'):
            # print each.get_text(),
            plate_string+=each.get_text()+' '
        # print ''

        #办公地址
        pattern = re.compile(r'<td class="thead_1">办公地址</td>.*?<td>(.*?)</td>', re.S)
        office_address = re.findall(pattern, temp)
        # print office_address[0]

        #联系电话
        pattern = re.compile(r'<td class="thead_1">联系电话</td>.*?<td>(.*?)</td>', re.S)
        telephone = re.findall(pattern, temp)
        # print telephone[0]

        #公司网址
        pattern = re.compile(r'<td class="thead_1">公司网站</td>.*?<td>(.*?)</td>', re.S)
        website = re.findall(pattern, temp)
        # print website[0]

        #电子邮箱
        pattern = re.compile(r'<td class="thead_1">电子邮箱</td>.*?<td>(.*?)</td>', re.S)
        email = re.findall(pattern, temp)
        # print email[0]

        list=[]

        list.append(i)#股票代码
        list.append(company_name)
        list.append(launch_date)
        list.append(registered_address)
        list.append(registered_capital)
        list.append(legal_representative)
        list.append(board_secretary)
        list.append(company_profile)
        list.append(industry)
        list.append(area)
        list.append(plate_string)
        list.append(office_address)
        list.append(telephone)
        list.append(website)
        list.append(email)

        self.company_info_data.append(list)

    def write_to_excel(self,file_name,data_list):
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
                # print col[0]
                # print type(col)
                try:
                    table.write(i+rows, j, col[0].decode('utf-8'))
                except:
                    table.write(i+rows, j, col)

        excel.save(file_name)  # xlwt对象的保存方法，这时便覆盖掉了原来的excel

    def save_data(self):
        #保存到excel
        self.write_to_excel('company_info_sh_B.xls',self.company_info_data)
        # self.write_to_excel('company_info_sh_A.xls',self.company_info_data)


if __name__ == '__main__':

    # for i in range(603000, 604000): #602000-602999都是空的  #上海的A股：600000-6040000
    for i in range(900900,900999): #上海的B股：900900-900999
        zhengquanzhixing = ZHENGQUANZHIXING()
        print i
        time.sleep(random.uniform(1, 2))  # 防止操作太快
        url = 'http://stock.quote.stockstar.com/corp_{}.shtml?yyue=a21bo.50862.201879'.format(i)
        zhengquanzhixing.getHtml_By_Url(url,i)
        zhengquanzhixing.save_data()
