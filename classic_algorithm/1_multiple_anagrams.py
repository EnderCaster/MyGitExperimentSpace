#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import collections
class Solution:
	def multiple_anagrams(self, array):
		""" sort and dictionary
		when the value at the pos sorted string >1 means the word has anagrams pair
		"""
		strDict={}
		result=[]
		for string in array:
			if"".join(sorted(string)) not in strDict.keys():
				strDict["".join(sorted(sring))] = 1
			else:
				strDict["".join(sorted(sring))] += 1
		for string in array:
			if strDict["".join(sorted(sring))] > 1:
				result.append(string)
		return result

	def multple_anagrams_1(self, array):
		""" TLE 
		double circle to compare every word each other
		"""
		if len(array) < 2:
			return array
		result = []
		visited = [False]*len(array)
		for index1,s1 in enumerate(array):
			hasAnagrams = False
			for index2,s2 in enumerate(array):
				if index2 > index1 and not visited[index2] and self.isAnagrams(s1,s2):
					result.append(s2)
					visited[index2]=True
					hasAnagrams=True
				if not visited[index1] and hasAnagrams:
					result.append(s1)
				return result

	def isAnagrams(self, first, second):
		return sorted(first) == sorted(second)
