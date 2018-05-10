#!/usr/bin/env python3
#-*- utf-8 -*-
basic_salary = 1500
bonus_rate = 200
commision_rate = 0.02
number_of_camera = int(input("camera number:"))
price = float(input("total price:"))
bonus = (bonus_rate * number_of_camera)
commision = (commision_rate * number_of_camera * price)
print("{:15s}={:10.2f}".format("Bonus",bonus))
print("{:15s}={:10.2f}".format("Commision",commision))
print("{:15s}={:10.2f}".format("Gross salary",basic_salary + bonus + commision))

