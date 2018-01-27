#!/usr/bin/env python
#-*- utf-8 -*-
a = ['cat','window','defenestrate']
for x in a:
	print(x,len(x))
print('------')
# in python2.7 sysout with () treat multi param as a calculated string include () and ,
print range(5,10)
print('------')
print range(0,10,3)
print('------')
print range(-10,-100,-30)
print('------')
for i in range(len(a)):
	print i,a[i]
