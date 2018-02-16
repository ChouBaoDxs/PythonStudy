# -*- coding: UTF-8 -*-

import MyDataUtils
import pandas as pd


if __name__=='__main__':

    path = '概念板块编码网址.xlsx'
    table_name = '工作表1'
    concept_dataFrame = MyDataUtils.Load_excel_by_path(path, table_name)
    print concept_dataFrame

    #只需要看下面的代码就好了*********************************************************************
    for each in concept_dataFrame:
        print each
        print type(each)

    for indexs in concept_dataFrame.index:
        print type(indexs)
        print indexs
        print(concept_dataFrame.loc[indexs].values[:])
        print type(concept_dataFrame.loc[indexs].values[1:-1])
        break

    for indexs,each in enumerate(concept_dataFrame.index):
        print indexs
        print each
        break





