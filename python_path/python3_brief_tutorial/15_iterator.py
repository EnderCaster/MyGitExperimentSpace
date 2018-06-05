#!/usr/bin/env python3
# -*- utf-8 -*-
class Counter(object):
    """iterator can only use one time, once it throw StopIteration, the exception will be always thrown"""
    def __init__(self,low,high):
        self.current=low
        self.high=high
    def __iter__(self):
        return self
    def __next__(self):
        if self.current>self.high:
            raise StopIteration
        else:
            self.current+=1
            return self.current-1

a=Counter(5,10)
for i in a:
    print(i,end=" ")


# The iterator execute like that
# while True:
# try:
#   iter.__next__()
# except StopIteration:
#   break