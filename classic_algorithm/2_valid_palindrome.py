#!/usr/bin/env python3
#-*- utf-8 -*-
class Solution:
    def isPalindrome(self, origin):
        """validate if the origin string is a palindrome
        """
        if not origin:
            # of course empty string is a palindrome
            return True
        left_index, right_index=0,len(origin)-1
        # jump off the special character
        while left_index<right_index:
            if not origin[left_index].isalnum():
                left_index+=1
                continue
            if not origin[right_index].isalnum():
                right_index-=1
                continue
            if origin[right_index].lower()==origin[left_index].lower():
                left_index+=1
                right_index-=1
                continue
            else:
                return False

        return True
        
    def betterSolution(self,origin):
        """this function aims at O(n) time difficult and 0 extra space
        """
        return True
test_class=Solution()
print(test_class.isPalindrome("a file elif"))