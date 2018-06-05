#!/usr/bin/env python3
# -*- utf-8 -*-
def my_decorator(function):
    """use the function under the 'at' as parameter"""
    def wrapper(*args,**kwargs):
        print("before")
        # we have to call the origin function 
        result=function(*args,**kwargs)
        print("after")
        # and return the result
        return result
    return wrapper

@my_decorator
def add(a,b):
    print("function called")
    return a+b

res=add(5,10)
print(res)