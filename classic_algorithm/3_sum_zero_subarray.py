#!/usr/bin/env python3
# -*- utf-8 -*-
class Solution:
    def sum_zero_summary(self,array):
        return self.hash_set(array)
    # def tle(self,array):
    #     tle is a starter version of hash, 
    #     result=[]
    #     current_sum=0
    #     sum_i=[]
    #     for i in range(len(array)):
    #         current_sum+=array[i]
    #         if 0==current_sum:
    #             result.append(0)
    #             result.append(i)
    #             return result
    #     if sum_i.count(current_sum):
    #         result.append()
    def hash_set(self,nums):
        result=[]
        hash={}
        hash.setdefault(0,0)
        curr_sum=0
        for i in range(len(nums)):
            curr_sum+=nums[i]
            if hash.get(curr_sum) != None:
                # we find curr sum in hash set ,means that we added a serial of number that sum is 0, from the first time we calc the sum
                result.append(hash.get(curr_sum))
                result.append(i)
                return result
            else:
                # record currsum
                hash.setdefault(curr_sum,i+1)
        return result