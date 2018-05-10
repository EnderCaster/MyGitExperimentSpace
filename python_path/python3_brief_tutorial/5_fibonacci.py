#!/usr/bin/env python3
#-*- utf-8 -*-
a, b = 0, 1
while b < 100:
	print(b)
	a, b = b, b + a

a, b = 0, 1
while b < 100:
	print(b, end = ' ')
	a, b = b, b + a
