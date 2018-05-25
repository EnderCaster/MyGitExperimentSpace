#!/usr/bin/env python3
# -*- utf-8 -*-


class Solution:
    def longestPalindrome(self, origin):
        if not origin:
            return ""

        length = len(origin)
        longest, left, right = 0, 0, 0
        for i in range(0, length):
            for j in range(i+1, length+1):
                substr = origin[i:j]
                if self.isPalindrome(substr) and len(substr) > longest:
                    longest = len(substr)
                    left, right = i, j
        result = origin[left:right]
        return result

    def isPalindrome(self, origin):
        """validate if the origin string is a palindrome
        """
        if not origin:
            # of course empty string is a palindrome
            return True
        left_index, right_index = 0, len(origin)-1
        # jump off the special character
        while left_index < right_index:
            if not origin[left_index].isalnum():
                left_index += 1
                continue
            if not origin[right_index].isalnum():
                right_index -= 1
                continue
            if origin[right_index].lower() == origin[left_index].lower():
                left_index += 1
                right_index -= 1
                continue
            else:
                return False

        return True
    # O(n^2)
    def palindrome(self,origin,left,right):
        """the max length palindrome if when left and right is the center

        :return: 
        """
        while left>=0 and right<len(origin) and origin[left]==origin[right]:
            left-=1
            right+=1

        return origin[left+1:right-1]

    def longestPalindrome2(self,origin):
        if len(origin)==0:
            return origin
        res=""
        for i in range(len(origin)):
            target=self.palindrome(origin,i,i)
            if len(target)>len(res):
                res=target
            target=self.palindrome(origin,i,i+1)
            if len(target)>len(res):
                res=target
        return res
