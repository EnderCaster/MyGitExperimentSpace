#!/usr/bin/env python
#-*- utf-8 -*-
def ask_ok(prompt,retries=4,complaint='y/n?pls'):
	while True:
		ok=raw_input(prompt)
		if ok in ('y','ye','yes'):
			return True
		if ok in ('n'm'no','nop','nope'):
			return False
		retries=retries-1
		if retries < 0:
			raise IOError('refusenik user')
		print complaint
# This example show a function that has requirable and optional parameters	
# This function can also called like ask_ok(prompt=xxx,complaint=xxx)
# or ask_ok('',complaint=xxx) to special the parameter you wanna to assign/modify the default value
