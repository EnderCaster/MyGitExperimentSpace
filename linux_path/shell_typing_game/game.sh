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
			menu
			;;
		"2" )
			time = 5
			echo -e "\033[9;30H2) Dont you wanna be stronger?"
			menu
			;;
		"3" )
			time = 3
			echo -e "\033[10;30H3) Oh, I think you could be a good typist."
			menu
			;;
		* )
			echo -e "\033[22;2H Hey man. keep your mind, there is no choice like ${mode}"
			sleep 1
	esac
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
