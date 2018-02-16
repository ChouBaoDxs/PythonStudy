# -*- coding: UTF-8 -*-

import re

string='人脑.*计划'
string='H\dN\d'
string='[西藏|建设].*[建设|西藏]'
string='西藏.*建设'
string='(?:西藏|建设).*(?:建设|西藏)'
# string='(西藏|建设).*(建设|西藏)'
string='(?:西藏|建设|H7)'
temp='国家人脑研究计划实施   H7N9   建设美丽西藏   西藏好建设'

pattern=re.compile(string)

result=pattern.finditer(temp)
print type(result)
for each in result:
    print each.group()

result=pattern.findall(temp)
print type(result)
print len(result)
print type(result[0])
for each in result:
    print each















