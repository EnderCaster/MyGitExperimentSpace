#!/usr/bin/env python
#-*- utf-8 -*-
def fib(n):
	""" declare a function to calculate fibonacci until n """
	a,b=0,1
	while a<n:
		print a,
		a,b=b,a+b
	return True
print fib(int(raw_input('\npls ipt a no:')))
