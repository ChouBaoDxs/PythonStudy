# -*- coding: UTF-8 -*-

import md5  #被废弃
src = 'this is a md5 test.'
m1 = md5.new()
m1.update(src)
print m1.hexdigest()        #这里输出的是32位小写

import hashlib
m2 = hashlib.md5()
m2.update(src)
print m2.hexdigest()        #这里输出的是32位小写














