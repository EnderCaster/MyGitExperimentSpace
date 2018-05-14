#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import collections


class Solution:
    def anagram(self, first, second):
        """anagram means the two words has same count of each alphabet"""
        if len(first) != len(second):
            return False

        return self.anagram1(first, second)

    def anagram1(self, first, second):
        """this solution means the two words has same count of each alphabet"""
        return collections.Counter(first) == collections.Counter(second)

    def anagram2(self, first, second):
        """ this solution means anagrams will be same after sorted """
        return sorted(first, second)


testClass = Solution()
result = testClass.anagram("123456789", "125436978")
if result:
    print("Success")
else:
    print("Failed")
