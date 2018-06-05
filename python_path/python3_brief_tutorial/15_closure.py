#!/usr/bin/env python3
# -*- utf-8 -*-
def closure(param1):
    def add(param2):
        return param1+param2
    return add

c=closure(50)
for i in range(10):
    print(c(i))