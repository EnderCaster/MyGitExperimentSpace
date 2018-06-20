#!/usr/bin/env python3
# -*- utf-8 -*-
from 
class Solution:
    def subarray_closest_zero(self,nums):
        result=[]
        if(len(nums))==0:
            return result
        num_size=len(num)
        sum_index=[]
        # sum_index records a array like fibonacci (f3=f1+f2) as first , and the second is the index
        i=0
        while i<num_size:
            sum_index
