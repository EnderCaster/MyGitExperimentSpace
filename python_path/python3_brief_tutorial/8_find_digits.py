#!/usr/bin/env python3
#-*- utf-8 -*-
"""This program relate a string file change it below
"""
file_path = "/home/shiyanlou/Code/String.txt"
string_file = open(file_path)
source_string = string_file.readline()
string_file.close()
new_string = ""
for ch in source_string:
	if ch.isdigit():
		new_string += ch

print(new_string)

