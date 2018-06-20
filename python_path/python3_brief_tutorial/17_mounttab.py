#!/usr/bin/env python3
# -*- utf-8 -*-
import os
def mount_details():
    """print the detail information of mount points"""
    with open("/proc/mounts") as fd:
        for line in fd:
            line=line.strip()
            words=line.split()
            print("{} on {} type {}".format(words[0],words[1],words[2]))
            if len(words)>5:
                print("({})".format(" ".join(words[3:-2])))
            else:
                print()

if __name__=="__main__":
    mount_details()