#!/bin/bash
function welcome()
{
	declare -r welcome_banner='0000000010000000000000000000000000000010000100000000000000100000
0000000010000000001000001000000000100001000100000000000000101000
1111110010000000000100110011110000010001000100000000000000100100
0000010011111100000100100010010000010111101111100111111000100100
0000010100000100000000100010010010000010001000000000001000100000
0100100100001000000000100010010001000010010000000000001000111110
0010101001000000111100100010010001000011101111000010010111100000
0001010001000000000100100010010000010010100001000001010000100100
0001000001000000000100100010010000010010100010000000100000100100
0010100010100000000100101011010000100010100010000000100000101000
0010010010100000000100110010100011100010101111100001010000101000
0100010100010000000100100010000000100010100010000001001000010000
1000000100010000000100000010000000100100100010000010001000110010
0000001000001000001010000010000000100100100010000100000001001010
0000010000000100010001111111111000101001101010000000000010000110
0000100000000010000000000000000000010000000100000000000100000010'
	declare -i row=5
	declare -ir line_char_count=65
	echo -ne "\033[37;40\033[5;3H"
	for ((i=0; i<${#welcome_banner};i++))
	do
		if [ "$[i%line_char_count]" == "0" ] && [ "${i}" != "0" ]
		then
			row=${row}+1
			echo -ne "\033["${row}";3H"
		fi
		# here is to sub welcome_banner at i and length=1
		if [ "${welcome_banner:${i}:1}" == "0" ]
		then
			# fg color : 30 black 31 red 32 green 33 brown 34 blue 35 purple 36 cyan 37 white 38 default+underline 39 default-underline
			# bg color : 40 black 41 red 42 green 43 brown 44 blue 45 purple 46 cyan 47 white 49 default black
			echo -ne "\033[37;40m "
		elif [ "${welcome_banner:${i}:1}" == "1" ]
		then
			echo -ne "\033[31;40m#"
		fi
	done
	row=${row}+1
	echo -ne "\033["${row}";15H"
}
function choose_mode()
{
	echo -e "\033[8;30H1) easy"
	echo -e "\033[9;30H2) normal"
	echo -e "\033[10;30H3) difficult"
	echo -ne "\033[22;2HMake your choice now:"
	read mode
	case ${mode} in
		"1" )
			time = 10
			echo -e "\033[8;30H1) Hey, you choose this?"
			sleep 1
			menu
			;;
		"2" )
			time = 5
			echo -e "\033[9;30H2) Dont you wanna be stronger?"
			sleep 1
			menu
			;;
		"3" )
			time = 3
			echo -e "\033[10;30H3) Oh, I think you could be a good typist."
			sleep 1
			menu
			;;
		* )
			echo -e "\033[22;2H Hey man. keep your mind, there is no choice like ${mode}"
			sleep 1
	esac
}
function menu()
{
	while [ 1 ]
	do
		draw_border
		echo -e "\033[8;30H1) number"
		echo -e "\033[9;30H2) alpha"
		echo -e "\033[10;30H3) alpha+num"
		echo -e "\033[11;30H4) word"
		echo -e "\033[12;30H5) exit"
		echo -ne "\033[22;2HHey man, choose one now:"
		read choice
		case ${choice} in
		"1" ) 
			draw_border
			game_main digit
			echo -e "\033[39;49m"
			;;
		"2" ) 
			draw_border
			game_main char
			echo -e "\033[39;49m"
			;;
		"3" ) 
			draw_border
			game_main mix
			echo -e "\033[39;49m"
			;;
		"4" ) 
			draw_border
			echo -ne "\033[22;2H"
			read -p "What file you wanna to use :" file
			if [ ! -f "${file}" ]
			then
				menu
			else
				exec 4<${file}
				game_main word
				echo -e "\033[39;49m"
			fi
			;;
		"5"|"q"|"Q" ) 
			draw_border
			echo -e "\033[10;25HExiting"
			echo -e "\033[39;49m"
			sleep 1
			clear
			exit 1
			;;
		* ) 
			draw_border
			echo -e "\033[22;2H Out of range, R U OK?"
			sleep 1
			;;
		esac
	done
}
function draw_border()
{
	declare -i width=79
	declare -i height=23

	clear

	echo -e "\033[37;40m"
	for (( i=1;i<=${width};i++ ))
	do
		for (( j=1; j<=${height};j++ ))
		do
			echo -e "\033[${j};${i}H "
		done
	done
	# display + at corner
	echo -ne "\033[1;1H+\033[${height};1H+\033[1;${width}H+\033[${height};${width}H+"
	for (( i=2; i<=${width}-1; i++ ))
	do
		echo -ne "\033[1;${i}H-"
		echo -ne "\033[${height};${i}H-"
	done
	for (( i=2; i<=${height}-1; i++ ))
	do
		echo -ne "\033[${i};1H|"
		echo -ne "\033[${i};${width}H|"
	done
}
function clear_text_area()
{
	for (( i=5; i<=21; i++ ))
	do
		for (( j=3; j<=77; j++ ))
		do
			echo -e "\033[44m\033[${i};${j}H "
		done
	done
	echo -e "\033[37;40m"

}
function put_array()
{
	case ${i} in
	digit )
		chars="123567890"
		for (( i=0; i<10; i++ ))
		do
			array[${i}]=${chars:${i}:1}
		done
		;;
	char )
		chars="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
		for (( i=0; i<52; i++ ))
		do
			array[${i}]=${chars:${i}:1}
		done
		;;
	mix )
		chars="123567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
		for (( i=0; i<62; i++ ))
		do
			array[${i}]=${chars:${i}:1}
		done
		;;
	* )
		;;
	esac
}
function get_random_char()
{
	declare -i typenum=0
	case ${i} in
	digit )
		typenum=$((${RANDOM}%10))
		;;
	char )
		typenum=$((${RANDOM}%52))
		;;
	mix )
		typenum=$((${RANDOM}%62))
		;;
	* )
		;;
	esac
	random_char=${array[${typenum}]}

}
function game_main()
{
	declare -i game_start_time=`date +%s`
	declare -i game_done_time=0

	declare -i start_time
	declare -i dead_time
	declare -i current_time
	declare -i done_time

	declare -i number_right=0
	declare -i number_total=0
	declare -i accuracy=0
	put_array ${i}
	while [ 1 ]
	do
		echo -e "\033[2;2H type the word as fast as you can!"
		echo -e "\033[3;2H time now:"
		current_time=`date +%s`
		game_done_time=${current_time}-${game_start_time}
		echo -e "\033[31;40m\033[3;15H${game_done_time}\033[37;40m"
		echo -e "\033[3;60H total:\033[31;26m${number_total}\033[37;40m"
		echo -e "\033[3;30H accuray:\033[31;40m${accuracy}\033[37;40m"
		echo -ne "\033[22;2H your input is:"
		clear_text_area
		for (( line=20; line<=60; line=line+10 ))
		do
			if [ "${ifchar[${line}]}" == "" ] || [ "${done_time[${line}]}" -gt "${time}" ]
			then
				clear_line ${line}
				if [ "${1}" == "word" ]
				then
					read -u 4 word
					if [ "${word}" == "" ]
					then
						exec 4<${file}
					fi
				else
					get_random_char ${1}
					putchar[${line}]=${random_char}
				fi
				number_total=${number_total}+1
				ifchar[${line}]=1
				start_time[${line}]=`date +%s`
				current_time[${line}]=${start_time[${line}]}
				done_time[${line}]=${time}
				column[${line}]=0
				if [ "${1}" == "word" ]
				then
					move 0 ${line} ${putchar[${line}]}
				fi
			else
				current_time[${line}]=`date +%s`
				done_time[${line}]=${current_time[${line}]}-${start_time[${line}]}
				move ${done_time[${line}]} ${line} ${putchar[${line}]}
			fi
		done
		if [ "${1}" != "word" ]
		then
			echo -ne "\033[22;14H"
			if read -n 1 -t 0.5 input_char
			then
				for (( line=20; line<=60; line=line+10 ))
				do
					if [ "${input_char}" == "$putchar[$line]}" ]
					then
						clear_line ${line}
						ifchar[${line}]=""
						echo -e "\007\033[32;40m\033[4;62H  do well\033[37;40m"
						number_right=${number_right}+1
						break
					else
						echo -e "\033[31;40m\033[4;62H cheer up!bro!\033[37;40m"
					fi
				done
			fi
		else
			echo -ne "\033[22;14H"
			if read input_word
			then
				for (( line=20; line<=60; line=line+10 ))
				do
					if [ "${input_word}" == "$putchar[$line]}" ]
					then
						clear_line ${line}
						ifchar[${line}]=""
						echo -e "\007\033[32;40m\033[4;62H  do well\033[37;40m"
						number_right=${number_right}+1
						break
					else
						echo -e "\033[31;40m\033[4;62H cheer up!bro!\033[37;40m"
					fi
				done
			fi
		fi
		trap " do_exit " 2
		accuracy=${number_right}*100/${number_total}
	done
}
function clear_line()
{
	for (( i=1; i<${width}; i++ ))
	do
		echo -ne "\033[44m\033[${1};${i}H "
	done
}
function do_exit()
{
	draw_border
	echo -e "\033[10;30H Exiting"
	echo -e "\033[0m"
	sleep 2
	clear
	exit 1
}
function main()
{
	draw_border
	welcome
	echo -ne "Start your challange?[y/N]"
	read start_choice
	if [[ ${start_choice} == "Y" || ${start_choice} == "y" ]]
	then 
		draw_border
		choose_mode
	else
		clear
		exit 1
	fi
	exit 1
}
main
