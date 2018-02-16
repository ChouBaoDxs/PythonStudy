# -*- coding: UTF-8 -*-

#导入开发包
import pymysql.cursors

#获取链接
connection = pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            db='wikiurl',
            charset='utf8mb4'
        )

try:
    #获取会话指针
    with connection.cursor() as cursor:
        #查询语句 避免使用*查询
        sql="select `urlname`,`urlhref` from urls where `id` is not null"
        count=cursor.execute(sql)
        print(count)

        #查询数据
        # result=cursor.fetchall()#查询全部    如果执行了这里的查询全部，那么之后的查询语句就查询不到东西了
        # print(result)

        result=cursor.fetchmany(size=3) #查询3条
        print(result)

        result=cursor.fetchone()    #查询下一条  因为上面已经查询了3条，所以这里是第4条
        print(result)

finally:
    connection.close()






