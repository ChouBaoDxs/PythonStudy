# -*- coding: UTF-8 -*-
def my_sum(*arg):
    if len(arg)==0:
        return 0
    for val in arg:
        if not isinstance(val,int):
            return 0
    return sum(arg)

def my_average(*arg):
    if len(arg)==0:
        return 0
    for val in arg:
        if not isinstance(val,int):
            return 0
    return sum(arg)/len(arg)

#闭包的方式
def my_sum1(*arg):
    print('in my_sum1')
    return sum(arg)

def my_average1(*arg):
    return sum(arg)/len(arg)

def dec(func):
    def in_dec(*arg):
        print('in dec arg=',arg)
        if len(arg) == 0:
            return 0
        for val in arg:
            if not isinstance(val, int):
                return 0
        return func(*arg)
    return in_dec

my_sum1=dec(my_sum1)    #my_sum1=in_dec(*arg)
print(my_sum1(1,2,3,4,5))
print(my_sum1(1,2,3,4,5,'6'))
my_average1=dec(my_average1)
print(my_average1(1,2,3,4,5))
print(my_average1())

# print(my_sum(1,2,3,4,5))
# print(my_sum(1,2,3,4,5,'6'))
# print(my_average(1,2,3,4,5))
# print(my_average())


















