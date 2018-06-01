#!/usr/bin/env python3
# -*- utf-8 -*-
import sys
def Hours(minutes):
	hours,minutes=divmod(minutes,60)
	return hours,minutes

if __name__=="__main__":
	if len(sys.argv)>1:
		try:
			minutes=int(sys.argv[1])
			if minutes<0:
				raise ValueError("ValueError: Input number cannot be negative")
			print("{} H, {} M".format(*Hours(minutes)))
		except Exception as e:
			print(e)
	