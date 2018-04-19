#!/usr/bin/env python
# -*- utf-8 -*-
from __future__ import print_function
from collections import OrderedDict
def memory_info():
	"""return memory info in /proc/meminfo as a dict 
	"""
	memory_info=OrderedDict()
	with open('/proc/meminfo') as f:
		for line in f:
			memory_info[line.split(':')[0]]=line.split(':')[1].strip()
	return memory_info

if __name__ =='__main__':
	memory_info=memory_info()
	print('Total memory: {0}'.format(memory_info['MemTotal']))
	print('Free memory: {0}'.format(memory_info['MemFree']))

