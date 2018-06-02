#!/usr/bin/env python3
# -*- utf-8 -*-
class Solution:
    def reverse_words_in_string(self, origin):
        return self.my_solution(origin)

    def reverse_words_in_string_1(self, origin):
        """this function aims to trim string and reverse it by word
        exp: Hello world -> world Hello
        (not finished)
        """
        if len(origin)<=0:
            return origin

        s_ret,s_temp=list(),list()
        ix=len(origin)
        while(ix!=0):
            s_temp=list()
            print(ix)
            while origin[ix-1:ix]!=" " and origin[ix-1:ix]!="":
                s_temp.append(origin[ix-1:ix])
                if ix==0:
                    break
                print(origin[ix:ix+1])
                
            if len(s_temp)!=0:
                if len(s_ret)!=0:
                    s_ret.append(' ')

                s_temp.reverse()
                s_ret.append(s_temp)
            

        return s_ret
    def my_solution(self, origin):
        """time O(n),space O(n+2)
        """
        # don't think better just do it
        # we have anther string and two pointers
        index,index_t=len(origin)-1,len(origin)
        another_string=list()
        for i in range(len(origin)):
            # origin[index:index_t] 
            if origin[index:index_t]==" ":
                index_t=index
                index-=1
                continue

            if origin[index-1:index]==" " or index==0:
                another_string.append(origin[index:index_t])
                index_t=index
            print("index",index_t,":",origin[index:index_t])
            index-=1
        
        return " ".join(another_string)
            


test_class=Solution()
result=test_class.reverse_words_in_string("hello world this is a test")
print(result)