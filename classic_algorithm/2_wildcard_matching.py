#!/usr/bin/env python3
#-*- utf-8 -*-
class Solution:
    def is_match(self,origin,regex):
        return self.is_match2(origin,regex)
    def is_match2(self,origin,regex):
        if origin=='' or regex=='':
            return False
        return self.dfs(origin,0,regex,0)
    def dfs(self,origin,origin_index,regex,regex_index):
        if origin_index==len(origin) or regex_index==len(regex):
            if origin_index==len(origin) and regex_index==len(regex):
                return True
            else:
                return False
        if regex[regex_index]=='*':
            while regex[regex_index]=='*':
                regex_index+=1
                if regex_index==len(regex):
                    # that means regex is all *
                    return True
            while origin_index<len(origin) and not self.dfs(origin,origin_index,regex,regex_index):
                origin_index+=1

            return origin_index!=len(origin)
        elif origin[origin_index] or regex[regex_index]=='?':
            return self.dfs(origin,origin_index+1,regex,regex_index+1)
        else:
            return False
    
    def is_match3(self,origin,regex):
        i,j=0,0
        star,ss=0,0
        while origin[i]:
            if regex[j]=='?' or regex[j]==origin[j]:
                i+=1
                j+=1
                continue
            if regex[j=="*"]:
                j+=1
                star=j
                ss=i
                continue
            if star :
                j=star
                ss+=1
                i=ss
                continue
            return False
        while regex[j]=='*':
            j+=1
        return not regex[j]