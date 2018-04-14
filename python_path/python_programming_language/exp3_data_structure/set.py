#!/usr/bin/env python
#-*- utf-8 -*-
basket=['f1','f2','f3','f4','f2']
test=set(basket)

# each value is unique

a=set('asdhfiaw')
b=set('asdfjiwen')
# a,b => char[]

a-b #sub
a | b # or
a & b # and
a^b #xor

# for
testSet={x for x in 'afilwuehuwy' if x not in 'abc}
