#!/usr/bin/env python3
# -*- utf-8 -*-
# a generator return only one value at once
def my_generator(low,high):
    """yield spawn a frozen break, when call again, start at there again"""
    while low <= high:
        yield low
        low+=1

for i in my_generator(5,10):
    print(i)