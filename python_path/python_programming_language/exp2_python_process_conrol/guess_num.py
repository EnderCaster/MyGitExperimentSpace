#!/usr/bin/env python
#-*- utf-8 -*-


true_num =88
guess_num = int(raw_input("\nInput the number: "))
if guess_num > true_num:
	print('too high\n')
elif guess_num < true_num:
	print('too low')
else:
	print('success\n')
print('exiting')
