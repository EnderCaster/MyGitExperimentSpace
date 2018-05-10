#!/usr/bin/env python3
#-*- utf-8 -*-
x = float(input("x:"))
n = term = num = 1
result = 1.0
while n <= 100:
	term *= x / n
	result += term
	n += 1
	if term < 0.0000001:
		break

print("Times:{},Sum:{}".format(n, result))
print("direct calc:{}".format(e^^x))
