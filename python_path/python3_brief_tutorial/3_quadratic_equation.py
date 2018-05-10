#!/usr/bin/env python3
#-*- utf-8 -*-
from math import sqrt
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
d = b * b - 4 * a * c
if d < 0:
	print("ROOTS are imaginary")
else:
	root1 = ( - b + sqrt(d)) / (2 * a)
	root2 = ( - b - sqrt(d)) / (2 * a)
	print("root 1 = {}".format(root1))
	print("root 2 = {}".format(root2))
