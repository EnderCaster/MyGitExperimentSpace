#!/usr/bin/env python
#-*- utf-8 -*-
from __future__ import print_function
from collections import OrderedDict
import pprint
def CPUinfo():
	"""return CPU info in /proc/CPUinfo as a dict 
	CPU_info['procx']={...}
	"""
	CPU_info=OrderedDict()
	procinfo=OrderedDict()
	nprocs = 0
	with open('/proc/cpuinfo') as f:
		for line in f:
			if not line.strip():
				CPU_info['proc%s' % nprocs]=procinfo
				nprocs = nprocs + 1
				procinfo=OrderedDict()
			else:
				if len(line.split(':')) == 2 :
					procinfo[line.split(':')[0].strip()] = line.split(':')[1].strip()
				else:
					procinfo[line.split(':')[0].strip()] = ''
	return CPU_info

if __name__ =='__main__':
	CPUinfo=CPUinfo()
	for processor in CPUinfo.keys():
		print(CPUinfo[processor]['model name'])
