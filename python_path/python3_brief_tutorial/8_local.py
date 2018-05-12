#!/usr/bin/env python3
#-*- utf-8 -*-
def change():
	a = 90
	return a

a = 9
print("before:{}".format(a))
print("inside:{}".format(change()))
print("after:{}".format(a))
