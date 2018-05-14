#!/usr/bin/env python3
# -*- coding=utf-8 -*-


class Solution:
    def strStr(self, source, needle):
        if source is None or needle is None:
            return -1
        # the index arrange of the first character in needle
        for i in range(len(source)-len(needle)+1):
            # and the offset of each character in needle
            for j in range(len(needle)):
                if source[i+j] != needle[j]:
                    break
            # else for inner circle, execute if success
            else:
                return i
        return -1

testClass = Solution()
result = testClass.strStr("345346114567","123")
if result != -1:
    print("Success")
else:
    print("Failed")