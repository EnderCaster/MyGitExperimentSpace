#!/usr/bin/env python3
# -*- utf-8 -*-
class Solution:
    """remove the value from the array and return the length together result array
    """
    def remove_element(self,array,element):
        for i in array:
            if i==element:
                del i
            
        return len(array)