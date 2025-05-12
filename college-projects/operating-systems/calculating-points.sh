#!/bin/bash

path="/usr/share/dict/words"




# arguments_array="$@"
letters_points=(1 3 3 2 1 4 2 4 1 8 5 1 3 1 1 3 10 1 1 1 1 4 4 8 4 10)

# A B C D E F G H I J K L M N O P  Q R S T U V W X Y  Z
# 1 3 3 2 1 4 2 4 1 8 5 1 3 1 1 3 10 1 1 1 1 4 4 8 4 10

a_index=$(printf "%d" "'a")
big_a_index=$(printf "%d" "'A")

# converting uppercase letters in string to lowercase letters

str="abcdz"

new_string=$(echo $str | tr '[:upper:]' '[:lower:]')

echo $new_string

# walking through each of the letters in string

characters_array=()

for ((i=0; i<${#new_string}; i++))
{
    characters_array+=("${new_string:$i:1}")
}

# echo $characters_array

res=0

for c in "${characters_array[@]}"
{
    # echo "$c, "
    ascii_value=$(printf "%d" "'$c")
    # echo $ascii_value

    index=$((ascii_value-97))
    # echo $index

    val=${letters_points[$index]}
    # echo $val

    res=$((res+val))

    # letters_points
}

echo $res