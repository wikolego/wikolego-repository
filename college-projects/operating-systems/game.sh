#!/bin/bash

# arguments_array="$@"
letters_points=(1 3 3 2 1 4 2 4 1 8 5 1 3 1 1 3 10 1 1 1 1 4 4 8 4 10)

# A B C D E F G H I J K L M N O P  Q R S T U V W X Y  Z
# 1 3 3 2 1 4 2 4 1 8 5 1 3 1 1 3 10 1 1 1 1 4 4 8 4 10

a_index=$(printf "%d" "'a")
big_a_index=$(printf "%d" "'A")


# letter='a'

# int_letter=$(printf "%d" "'$letter")
# echo $int_letter

# if [ $int_letter -ge $a_index ]
# then
#     echo "small letter"
# else
#     echo "big letter"
# fi


# converting uppercase letters in string to lowercase letters

str="fdASFd"

echo $str | tr '[:upper:]' '[:lower:]'


# walking through each of the letters in string

# $characters_array=($(echo "smth" | grep -o .))

for c in $characters_array
{
    echo $c
}