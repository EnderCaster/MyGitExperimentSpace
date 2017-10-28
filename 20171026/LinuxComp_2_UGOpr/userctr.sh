#!/bin/bash
operationMode=$1
teacherName=$2
studentNamePrefix=$3
studentCount=$4
#del
if [ $operationMode = "del" ] ; then
	counter=1
	while [ $counter -le $studentCount ]
	do
		echo $studentNamePrefix$counter 'deleted'
		counter=$(($counter + 1))
	done
fi
