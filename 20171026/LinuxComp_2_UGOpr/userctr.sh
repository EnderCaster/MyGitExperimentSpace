#!/bin/bash
operationMode=$1
teacherName=$2
studentNamePrefix=$3
studentCount=$4
if [ $studentCount -lt 1 ] ; then
	echo 'parameter error'
	exit 0
elif [ $studentCount -gt 10 ] ; then
	echo 'parameter error'
	exit 0
elif [[ $studentNamePrefix =~ ^[0-9\|A-Z]+$ ]]
	echo 'parameter error'
	exit 0
fi
	
#add
if [ $operationMode = "add" ] ; then
#generate random password
	randompassword=$(openssl rand -base64 8 | cksum | cut -c1-6)
#add teacher
	adduser -g sudo -s zsh $teacherName --stdin $randompassword
	echo $teacherName':'$randompassword
	counter=1
	while [ $counter -le $studentCount ]
	do
		#judge if the user exist
		if [ id $studentNamePrefix$counter &> /dev/null ] ; then
			echo $studentNamePrefix$counter':******'
		else
			randompassword=$(openssl rand -base64 8 | cksum | cut -c1-6)
			adduser -s zsh $studentNamePrefix$counter --stdin $randompassword
			echo $studentNamePrefix$counter':'$randompassword
		fi
	done
#del
elif [ $operationMode = "del" ] ; then
	deluser -q $teacherName
	counter=1
	while [ $counter -le $studentCount ]
	do
		deluser -q $studentNamePrefix$counter
		echo $studentNamePrefix$counter 'deleted'
		counter=$(($counter + 1))
	done
fi
