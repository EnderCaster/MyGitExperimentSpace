#!/usr/bin/env python3
#-*- utf-8 -*-
temperature_f = float(input("please input a F temperature:"))
temperature_c = float(temperature_f - 32) / 1.8
print("{:.2f}".format(temperature_c))
