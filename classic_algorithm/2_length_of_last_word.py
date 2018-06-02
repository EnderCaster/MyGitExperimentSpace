#!/usr/bin/env python3
# -*- utf-8 -*-
class Solution:
    def length_of_last(self,origin):
        if len(origin)==0:
            return 0
        index=0
        while origin[len(origin)-index-1:len(origin)-index]==' ':
            index+=1
            if index==len(origin):
                return 0
        for i in range(len(origin)):
            if origin[len(origin)-index-i-1:len(origin)-index-i]=='' or origin[len(origin)-index-i-1:len(origin)-index-i]==' ':
                return i
