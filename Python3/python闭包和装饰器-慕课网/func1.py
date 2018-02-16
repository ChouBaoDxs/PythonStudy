# -*- coding: UTF-8 -*-

passline=60

def func(val):
    passline=90
    print('%x'%id(val))
    if val>=passline:
        print('pass')
    else:
        print('failed')

    def in_func():#(val,)
         print(val)
    in_func()
    return in_func()

def Max(val1,val2):
    return max(val1,val2)
print(Max(90,100))

func(89)
print("*****************")
f=func(89)
f()
print(f.__closure__)




