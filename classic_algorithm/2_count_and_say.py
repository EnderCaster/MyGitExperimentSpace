#!/usr/bin/env python3
# -*- utf-8 -*-


class Solution:
    def count_and_say(self, index):
        if index <= 0:
            return ""
        res = "1"

        index -= 1
        while index:
            # because the first element defined outside, so we circle index-1 times
            pointer = ""
            i=0
            while i < len(res):
                # for i =0 ; i<len(res); i++
                # this circle generate next string
                count = 1
                while (i+1 < len(res)) and (res[i] == res[i+1]):
                    # for consequence char count +1 and index(i) move next
                    count += 1
                    i += 1
                pointer += (str(count)+res[i])
                i+=1
            res = pointer
            index -= 1
        return res


cl = Solution()
result=cl.count_and_say(5)
print(result)