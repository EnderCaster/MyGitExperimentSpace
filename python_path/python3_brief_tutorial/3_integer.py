#!/usr/bin/env python3
#-*- utf-8 -*-
days = int(input("How many Days:"))
months = days // 30
days = days % 30
print("Month:{},Day:{}".format(months,days))
