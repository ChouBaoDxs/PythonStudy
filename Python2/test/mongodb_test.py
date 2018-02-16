# -*- coding: UTF-8 -*-
from pymongo import MongoClient

client=MongoClient()    #连接默认主机和端口
# client=MongoClient('localhost', 27017)
# client = MongoClient('mongodb://localhost:27017/')

# db=client.first #此处的first为数据库名
# collection=db.second#此处的first为表名
# collection.insert({'name':'dxs','age':21,'addr':'wenzhou'})

db = client.finance_database  # 此处的finance_database为数据库名
collection = db.eastern_viewpoint  # 此处的eastern_viewponit为表名
data={
            'title':'title',
            'url':'url',
            'info':'info',
            'time':'time',
            'abstract':'abstract',
            'content':'content',
        }
collection.insert(data)

client.close()
client=None



'''
from pymongo import MongoClient

#建立MongoDB数据库连接
client = MongoClient('localhost',27017)

#连接所需数据库,test为数据库名
db=client.test

#连接所用集合，也就是我们通常所说的表，test为表名
collection=db.test

#接下里就可以用collection来完成对数据库表的一些操作

#查找集合中所有数据
for item in collection.find():
    print item

#查找集合中单条数据
print collection.find_one() 

#向集合中插入数据
collection.insert({name:'Tom',age:25,addr:'Cleveland'})

#更新集合中的数据,第一个大括号里为更新条件，第二个大括号为更新之后的内容
collection.update({Name:'Tom'},{Name:'Tom',age:18})

#删除集合collection中的所有数据
collection.remove()

#删除集合collection
collection.drop()

#关闭数据库
client.close()
client=None
'''





