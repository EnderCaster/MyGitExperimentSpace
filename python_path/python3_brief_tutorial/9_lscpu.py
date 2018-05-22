#!/usr/bin/env python3
#-*- utf-8 -*-
info_dict=dict()
with open("/proc/cpuinfo") as cpuinfo:
    for index,line in enumerate(cpuinfo):
        sp_info=line.split(":")
        if len(sp_info)==2:
            info_dict.setdefault(line.split(":")[0].strip(),line.split(":")[1].strip())

for key,value in info_dict.items():
    print("{:10s}:{:10s}".format(key,value))