#!/bin/bash
local_ip=$(ifconfig|grep inet |awk -F: '{print $2 }'|awk -F " " '{print $1 }' | head -n 1)
softwarenum=$(dpkg -l | wc -l)
processtotalcount=$(ps -ef | wc -l)
echo 'cpu num: '$(cat /proc/cpuinfo| grep "cpu cores"| uniq | cut  -d ':' -f 2)
echo 'memory total: '$(cat /proc/meminfo |grep 'MemTotal' |awk -F : '{print $2}' |sed 's/^[ \t]*//g')
echo 'memory free: '$(free -m |grep - |awk -F : '{print $2}' |awk '{print $2}') 'M'
echo 'disk size: '$(df -h | head -n 2 | tail -n 1 | cut -d " " -f 4)
echo 'system bit: '$(getconf LONG_BIT)
echo 'process: '$processtotalcount
echo 'software num: '$softwarenum
echo 'ip: '$local_ip
