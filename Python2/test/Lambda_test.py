# -*- coding: UTF-8 -*-

#使用Lambda
li=[{"age":20,"name":"def"},{"age":25,"name":"abc"},{"age":10,"name":"ghi"}]
li=sorted(li,key=lambda x:x["age"])
print(li)


#不使用Lambda
def comp(x):
    return x["age"]
li=[{"age":20,"name":"def"},{"age":25,"name":"abc"},{"age":10,"name":"ghi"}]
li=sorted(li,key=comp)
print(li)

#与其它语言不同，Python的Lambda表达式的函数体只能有唯一的一条语句，也就是返回值表达式语句。















