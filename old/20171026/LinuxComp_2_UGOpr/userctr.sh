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
elif [[ $studentNamePrefix =~ ^[0-9\|A-Z]+$ ]] ; then
	echo 'parameter error'
	exit 0
fi
	
#add
if [ $operationMode = "add" ] ; then
#generate random password
	randompassword=$(openssl rand -base64 8 | cksum | cut -c1-6)
#add teacher
	useradd -g sudo -s "/bin/zsh" $teacherName
	echo $teacherName':'$randompassword | sudo chpasswd
	echo $teacherName':'$randompassword
	counter=1
	while [ $counter -le $studentCount ]
	do
		#judge if the user exist
		if [ id $studentNamePrefix$counter &> /dev/null ] ; then
			echo $studentNamePrefix$counter':******'
		else
			randompassword=$(openssl rand -base64 8 | cksum | cut -c1-6)
			useradd -s "/bin/zsh" $studentNamePrefix$counter
			echo $studentNamePrefix$counter':'$randompassword | sudo chpasswd
			echo $studentNamePrefix$counter':'$randompassword
		fi
		counter=$(($counter + 1))
	done
#del
elif [ $operationMode = "del" ] ; then
	sudo deluser -q $teacherName
	counter=1
	while [ $counter -le $studentCount ]
	do
		sudo deluser -q $studentNamePrefix$counter
		counter=$(($counter + 1))
	done
fi
