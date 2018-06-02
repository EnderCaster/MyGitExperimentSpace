#!/usr/bin/env python3
# -*- utf-8 -*-
import collections
class Solution:
    def compare_strings(self, first, second):
        """all character in first is in second"""
        letters=collections.defaultdict(int)
        for a in first:
            letters[a]+=1

        for b in second:
            if b not in letters:
                return False
            elif letters[b]<=0:
                return False
            else:
                letters[b]-=1

        return True