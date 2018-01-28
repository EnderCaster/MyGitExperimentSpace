#!/usr/bin/env python
#-*- utf-8 -*-
def f(x): return x%2 !=0 and x%3 !=0

filter(f,range(2,25)
# return the value in sequence that return true when use f
map(f,range(1,11))
# for each value in sequence ,call the f and return a sequence
def add(x,y): return x+y
reduce(add,range(1,11))
# x=add(1,2) y=list(range(1,11))[2] and cycle
a=range(0,50)
del a[position]
startPosition=0
stopPosition=3
del a[startPostion:stopPsition] # clear 0-2
del a[:] # clear all
del a # delete a

