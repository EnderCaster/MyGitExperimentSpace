#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import collections
class Solution:
	def longest_common_substring(self, first, second):
		"""find the [length] of common substring, not the value
		so, just count++ when this circle have not break
		"""
		if first=='' or second=='':
			return 0

		lcs,lcs_temp=0,0
		for i in range(len(first)):
			for j in range(len(second)):
				lcs_temp=0
				while (i+lcs<len(first)) and (j+lcs_temp)<len(second) and (first[i+lcs_temp]==second[j+lcs_temp]):
					lcs_temp+=1
				if lcs_temp>lcs:
					lcs=lcs_temp

		return lcs


test_class=Solution()
result=test_class.longest_common_substring("asduifhwe","asdfhwe")
print(result)

