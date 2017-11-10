#!/bin/bash
counter=0
read compNo
if [ compNo -ge 100000 ] ; then
	echo 'no more than 10^5'
	exit 1
elif [ compNo =~ [A-Za-z] ] ; then
	echo 'number is number'
	exit 2
else
	i=0
	while [ i -lt compNo ]
	do
	echo 'input school number and score:'
	read inputStr
	echo (schoolNo[i]=$(echo $inputStr | cut -d ' ' -f 1))'\n' >> /tmp/schoolNo.tmp
	schoolScore[i]=$(echo $inputStr | cut -d ' ' -f 2)
	i=$(($i + 1))
	done
	echo $(cat /tmp/schoolNo.tmp | sort -u) > /tmp/schoolNo.uniq
	rm /tmp/schoolNo.tmp
	counter=$(cat /tmp/schoolNo.uniq | uniq -c)
	i=0
	j=0
	while [ i -lt counter ]
	do
		school=$(schoolNo[i])
		score=0
		while [ j -lt $(schoolScore[*]) ]
		do
			if [ school == schoolNo[j] ] ; then
			score=$(($score + $schoolScore[j]))
			fi
			j=$(($j + 1))
		done
		echo $school ' ' $score >> /tmp/result.unsort
		i=$(($i + 1))
	done
	cat /tmp/result.unsort | sort -t ' ' -k 2 | head -n 1
fi
