# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd

def main():
    #Data Structure：数据结构
    s=pd.Series([i*2 for i in range(1,11)])
    print (type(s))
    dates=pd.date_range("20170301",periods=8)   #定义日期，从20170301开始，共8天
    #index：主键   columns：属性值
    df=pd.DataFrame(np.random.randn(8,5),index=dates,columns=list("ABCDE"))
    print (df)
    df2=pd.DataFrame({"A":1,"B":pd.Timestamp("20170301"),"C":pd.Series(1,index=list(range(4)),dtype="float32"),
                     "D":np.array([3]*4,dtype="float32"),"E":pd.Categorical(["police","student","teacher","doctor"])})
    print (df2)

    #Basic：基本操作
    print '取前3行'
    print (df.head(3))
    print '取后3行'
    print (df.tail(3))
    print '打印主键index'
    print (df.index)
    print '打印出值'
    print (df.values)
    print '转置'
    print (df.T)
    # print '按C列排序'
    # print (df.sort(columns="C"))#按C列排序
    print '按主键降序'
    print (df.sort_index(axis=1,ascending=False))
    print '打印所有统计值'
    print (df.describe())

    #Select
    print '切片：取得A列，含主键'
    print (df["A"])
    print (type(df["A"]))
    print '切片：取得前3行'
    print (df[:3])
    print '切片：20170301-20170304的数据'
    print (df["20170301":"20170304"])
    print '取得20170301的数据'
    print (df.loc[dates[0]])
    print '多对多的选择'
    print (df.loc["20170301":"20170304",["B","D"]])
    print '20170301对应的C列'
    print (df.at[dates[0],"C"])

    print '打印20170302和20170303的C列D列，下标从0开始'
    print (df.iloc[1:3,2:4])
    print '第1行第4列'
    print (df.iloc[1,4])
    print '第1行第4列'
    print (df.iat[1,4])

    print '给定条件筛选数据'
    print (df[df.B>0][df.A<0])
    print (df[df>0])
    print (df[df["E"].isin([1,2])])

    #Setting
    print '新增一列F'
    s1=pd.Series(list(range(10,18)),index=pd.date_range("20170301",periods=8))
    df["F"]=s1
    print (df)

    print '把A列都变成0'
    df.at[dates[0],"A"]=0
    print (df)

    df.iat[1,1]=1
    print '把D列都变成4'
    df.loc[:,"D"]=np.array([4]*len(df))
    print (df)

    print '拷贝'
    df2=df.copy()
    df2[df2>0]=-df2 #把正数都变成负数
    print (df2)

    #Missing Values：缺失值的处理
    print '取df的前4个，列取ABCD，再加一个G'
    df1=df.reindex(index=dates[:4],columns=list("ABCD")+["G"])
    print '给G列的第一行和第二行赋值'
    df1.loc[dates[0]:dates[1],"G"]=1
    print (df1)
    print '丢弃缺失值'
    print (df1.dropna())#丢弃
    print '以2填充缺失值'
    print (df1.fillna(value=2))#填充

    #Statistic：统计
    print '平均值'
    print (df.mean())#平均
    print '方差'
    print (df.var())#方差
    s=pd.Series([2,2,4,np.nan,5,7,9,10],index=dates)
    print (s)
    print '所有值往后移两个位置，即最后两个会被丢弃'
    print (s.shift(2))#所有值往后移两个位置，即最后两个会被丢弃
    print '后一个数减前一个数'
    print (s.diff())#后一个数减前一个数
    print '所有值出现的次数'
    print (s.value_counts())#所有值出现的次数
    print '累加'
    print (df.apply(np.cumsum))#累加
    print '极差'
    print (df.apply(lambda x:x.max()-x.min()))#极差

    #Concat：拼接
    print '取前三行和后三行，拼接起来'
    pieces=[df[:3],df[-3:]]
    print (pd.concat(pieces))

    print '左连接、右连接'
    left=pd.DataFrame({"key":["x","y"],"values":[1,2]})
    right=pd.DataFrame({"key":["x","z"],"values":[3,4]})
    print ("LEFT:",left)
    print ("RIGHT:",right)
    print (pd.merge(left,right,on="key",how="left"))
    print (pd.merge(left,right,on="key",how="inner"))
    print (pd.merge(left,right,on="key",how="outer"))

    print 'sql中的groupby'
    df3=pd.DataFrame({"A":["a","b","c","b"],"B":list(range(4))})
    print(df3.groupby("A").sum())

    #Reshape：透视表
    import datetime
    df4=pd.DataFrame({
        'A':['one','one','two','three']*6,
        'B':['a','b','c']*8,
        'C':['foo','foo','foo','bar','bar','bar']*4,
        'D':np.random.randn(24),
        'E':np.random.randn(24),
        'F':[datetime.datetime(2017,i,1) for i in range(1,13)]+
            [datetime.datetime(2017,i,15) for i in range(1,13)]
    })
    print (pd.pivot_table(df4,values="D",index=["A","B"],columns=["C"]))

    #Time Series：时间序列
    t_exam=pd.date_range("20170301",periods=10,freq="S")
    print (t_exam)
    #Graph  绘图
    ts=pd.Series(np.random.randn(1000),index=pd.date_range("20170301",periods=1000))
    ts=ts.cumsum()
    from pylab import *
    ts.plot()
    show()

    #File：文件操作
    df6=pd.read_csv("./data/test.csv")
    print (df6)
    df7=pd.read_excel("./data/test.xlsx","Sheet1")
    print (df7)
    #保存
    df6.to_csv("./data/test2.csv")
    df7.to_excel("./data/test2.xlsx")


if __name__=="__main__":
    main()















