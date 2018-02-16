# -*- coding: UTF-8 -*-
import json
import requests

#Secret Key：83b2ed796fa2ed87        python_test：云逻辑方法名
#name=2333: 传入一个参数，名称是name，值是2333
#print '测试'
# url='http://cloud.bmob.cn/83b2ed796fa2ed87/python_test?name=2333'
# response=requests.get(url)
# print response
# print response.text
# ob_json=json.loads(response.text)
# print ob_json
#
# print "\n*************************\n"
# #
# print 'post方式插入一条数据信息'
# url='http://cloud.bmob.cn/83b2ed796fa2ed87/insert_data?name=insert'
# data={
#     'temperature':455,
#     'ph':1.0,
#     'ammonia_nitrogen':80,
#     'dissolved_oxygen':75,
# }
# response=requests.post(url=url,data=data)
# print response
# print response.text
#
# print 'get方式插入一条数据信息'
# url='http://cloud.bmob.cn/83b2ed796fa2ed87/insert_data?temperature=1000&ph=2.5&ammonia_nitrogen=88&dissolved_oxygen=23'
# response=requests.get(url)
# print response
# print response.text
#
# print "\n*************************\n"

print '查询最新的数据信息'
url='http://cloud.bmob.cn/83b2ed796fa2ed87/find_data?name=find'
response=requests.get(url)
# print response
print response.text

#解析返回的数据
ob_json=json.loads(response.text)
# print ob_json
result=ob_json['results']
# print result
# print type(result)
data=result[0]
# print data
temperature=data.get('temperature')
print "温度:"+str(temperature)
ph=data.get('ph')
print "ph值:"+str(ph)
ammonia_nitrogen=data.get('ammonia_nitrogen')
print "氨氮值:"+str(ammonia_nitrogen)
dissolved_oxygen=data.get('dissolved_oxygen')
print "溶解氧:"+str(dissolved_oxygen)
createdAt=data.get('createdAt')
print "数据采集时间:"+str(createdAt)




