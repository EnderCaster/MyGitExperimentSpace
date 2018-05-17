#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import string
class Solution:
	def rotate_string(self, string, length):
		"""RCR for string
		if length = 5 and string.len=20
		from 20 to 5 exchange i and i-5
		"""
		string=list(string)
		for index in range(len(string)):
			if length > len(string):
				length=length%len(string)
			exchange=string[len(string)-1-index-length]
			string[len(string)-1-index-length]=string[len(string)-1-index]
			string[len(string)-1-index]=exchange
			if length == len(string) - 1 - index:
				break
		return string

test_class=Solution()
origin=string.ascii_uppercase
result=test_class.rotate_string(origin,5)
print(origin)
print(result)

