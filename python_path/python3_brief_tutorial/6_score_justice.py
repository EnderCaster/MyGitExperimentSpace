#!/usr/bin/env python3
#-*- utf-8 -*-
n = int(input("how many students:"))
data = {}
Subjects = ("Physics","Maths","History")
for i in range(0,n):
	name = input("Name:")
	scores =[]
	for x in Subjects:
		scores.append(int(input("Enter scores of {}:".format(x))))

	data[name] = scores

for x, y in data.items():
	total = sum(y)
	print("{}'s total score {}".format(x, total))
	if total < 120:
		print(x, "failed")
	else:
		print(x, "passed")

