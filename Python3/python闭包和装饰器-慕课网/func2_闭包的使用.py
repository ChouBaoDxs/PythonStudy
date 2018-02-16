# -*- coding: UTF-8 -*-

def func_150(val):
    passline=90
    if val>=passline:
        print('pass')
    else:
        print('failed')

def func_100(val):
    passline=60
    if val>=passline:
        print('pass')
    else:
        print('failed')

def set_passline(passline):     #闭包的使用
    def cmp(val):
        if val>passline:
            print('pass')
        else:
            print('failed')
    return cmp

func_150(89)
func_100(59)
print('********************************')
f_100=set_passline(60)
# print(type(f_100))
# print(f_100.__closure__)
f_100(89)
f_100(59)

f_150=set_passline(90)
f_150(89)
f_150(59)
