#!/usr/bin/env python3
#-*- utf-8 -*-
i = 1
print ("-" * 120)
while i < 16:
	n = 1
	while n < 16:
		print("{:8X}".format(i * n),end = "")
		n += 1
	print()
	i += 1

print("-" * 120)
