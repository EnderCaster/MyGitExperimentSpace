#!/usr/bin/env python3
#-*- utf-8 -*-
"""There are 21 sticks, you can take 1-4 number of sticks as a time.
Whoever will take the last stick till loose
"""
sticks = 21

while True:
	print("sticks left:{:3d}".format(sticks))
	sticks_taken = int(input("take stick(1-4):"))
	if sticks ==1:
		print("you loose")
		break
	
	if sticks_taken >= 5 or sticks_taken <= 0:
		print("input wrong")
		continue

	print("computer took:{:3d}".format(5 -sticks_taken))
	sticks -= 5
