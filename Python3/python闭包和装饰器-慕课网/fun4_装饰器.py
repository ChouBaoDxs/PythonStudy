# -*- coding: UTF-8 -*-
#闭包的方式

def dec(func):
    print('call dec')
    def in_dec(*arg):
        print('in dec arg=',arg)
        if len(arg) == 0:
            return 0
        for val in arg:
            if not isinstance(val, int):
                return 0
        return func(*arg)
    print('return in_dec')
    return in_dec

@dec    #等于my_sum=dec(my_sum)
def my_sum(*arg):   #my_sum=in_dec
    print('in my_sum')
    return sum(arg)

print(my_sum(1,2,3,4,5))

def my_average(*arg):
    return sum(arg)/len(arg)

# my_sum=dec(my_sum)    #my_sum1=in_dec(*arg)
# print(my_sum(1,2,3,4,5))
# print(my_sum(1,2,3,4,5,'6'))
# my_average=dec(my_average)
# print(my_average(1,2,3,4,5))
# print(my_average())


















