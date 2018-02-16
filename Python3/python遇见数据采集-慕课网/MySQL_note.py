# -*- coding: UTF-8 -*-

#存储数据到MySQL 存储数据到MySQL  存储数据到MySQL  存储数据到MySQL  存储数据到MySQL

#引入开发包
import pymysql.cursors

#获取数据库链接
connection=pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    db='wikiurl',
    charset='utf8mb4'
)
#获取会话指针
cursor=connection.cursor()
#执行SQL语句
# cursor.execute(sql,(参数1,参数2...参数3))
#提交
connection.commit()
#关闭
connection.close()

#读取MySQL数据  读取MySQL数据   读取MySQL数据   读取MySQL数据   读取MySQL数据

#得到总记录数 返回值是int
cursor.execute()
#查询下一行  直接执行的话，就是查询第1条 第二次就第2条
cursor.fetchone()
#得到指定大小 limit
cursor.fetchmany(size=None)
#得到全部
cursor.fetchall()
#关闭
connection.close()



