#!/usr/bin/env python
# -*- utf-8 -*-
import os
def load_stat():
	load_avg={}
	f=open('/proc/loadavg')
	con=f.read().split()
	f.close()
	load_avg['lavg_1']=con[0]
	load_avg['lavg_5']=con[1]
	load_avg['lavg_15']=con[2]
	load_avg['nr']=con[3]
	load_avg['last_pid']=con[4]
	return load_avg

print("loadavg(1):",load_stat()['lavg_1'])

