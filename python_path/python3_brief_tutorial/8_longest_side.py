#!/usr/bin/env python3
#-*- utf-8 -*-
import math
def longest_side(a, b):
	"""Function to find the length of the longest side of a right triangle.
	:arg a: side a of the triangle
	:arg b: side b of the triangle
	
	:return: Length of the longest side c as float
	"""
	return math.sqrt(a**2 + b**2)

if __name__ == '__main__':
	print(longest_side.__doc__)
	print(longest_side(4, 5))
