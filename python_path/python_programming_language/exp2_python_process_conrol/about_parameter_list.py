#!/usr/bin/env python
#-*- utf-8 -*-

def test(tep, *args):
	print args
# In this example, the parameters after the first will treat as a array. the array length can be 0 to n
# You can use a * operator to deconstract array/list and ** to deconstract dict
# lambda X: x+n -> function(x){x+n} // in this case 'n' is not defined
def make incrementor(n):
	return lambda X: x+n
f= make_incrementor(42)# lambda x:x+42
f(0) # return 0+42
