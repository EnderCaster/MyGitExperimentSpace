#!/usr/bin/env python3
#-*- utf-8 -*-
rows = int(input("rows:"))
rows_counter = rows

while rows_counter > 0:
	space = rows - rows_counter
	space = " " * space
	star = rows_counter
	star = "*" * star
	print(space,star)
	rows_counter -= 1
