# -*- coding: UTF-8 -*-

def deco(func):
    def in_deco(x,y):
        print('in deco')
        func(x,y)
    print('call deco')
    return in_deco()

#deco(bar)->in_deco
#bar=in_deco
#bar() in_deco() bar()
@deco
def bar(x,y):
    print('in bar',x+y)

print(type(bar))
bar(1,2)













