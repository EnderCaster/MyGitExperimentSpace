#!/usr/bin/env python3
#-*- utf-8 -*-
a=[1,2,3,4,5,6,7,8,9,125,345,45,456,1,13]
sum_a = 0
for i in a:
	sum_a = sum_a + i

length = len(a)
result = float(sum_a / length)
print("{:.2f}".format(result))
