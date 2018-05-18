#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import string
class Solution:
	def rotate_string(self, string, length):
		"""RCR for string
		if length = 5 and string.len=20
		from 20 to 5 exchange i and i-5
		"""
		if length<=0:
			return string
		
		if length > len(string):
			length=length%len(string)

		string=list(string)
		while length>0:
			for index in range(len(string)):
				exchange=string[0]
				string[0]=string[(index +1 ) % len(string)]
				string[(index +1 ) % len(string)]=exchange

			length-=1
		return "".join(string)

test_class=Solution()
origin=string.ascii_uppercase
result=test_class.rotate_string(origin,5)
print(origin)
print(result)

