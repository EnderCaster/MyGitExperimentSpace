#!/usr/bin/env python3
# -*- urf-8 -*-
class Counter(object):
    """This is not a iterator nor a generator
    reset the iter value to reuse
    """
    def __init__(self,low,high):
        print('i am the init function')
        self.low=low
        self.high=high
    def __iter__(self):
        print("i am the start of iter function")
        counter=self.low
        while self.high>=counter:
            yield counter
            counter+=1

obj=Counter(5,10)
for num in obj:
    print(num)
print("*"*10)
for num in obj:
    print(num)