#!/bin/bash

# 0 - skip if the word does not exists in dictionary
# 1 - otherwise
skip=0

str="adsfasdasdfsadfasdfsa"

# arguments_array="$@"
letters_points=(1 3 3 2 1 4 2 4 1 8 5 1 3 1 1 3 10 1 1 1 1 4 4 8 4 10)

# A B C D E F G H I J K L M N O P  Q R S T U V W X Y  Z
# 1 3 3 2 1 4 2 4 1 8 5 1 3 1 1 3 10 1 1 1 1 4 4 8 4 10

# converting uppercase letters in string to lowercase letters

new_string=$(echo $str | tr '[:upper:]' '[:lower:]')

# default path

dictionary_path=${dictionary_path:-"/usr/share/dict/words"}

# 0 - word not in dictionary ; 1 word in dictionary

in_dictionary=0

# 0 - dictionary doesn't exist
dictionary_exist=0

# test if dictionary exist

if [ -f "$dictionary_path" ]; then

    # if exists 
        dictionary_exist=1

else

    echo "Uwaga: Słownik $dictionary_path nie istnieje."   
    # potential message if dictionary not present  

fi

if [ $dictionary_exist -eq 1 ] && grep -q "^$new_string$" "$dictionary_path" 2>/dev/null; then
    #if dictionary exist and word in dictionary
    in_dictionary=1
fi

# printing the result

if [ $in_dictionary -eq 1 ] && [ $dictionary_exist -eq 1 ]; then

    echo "Słowo \"$new_string\" znajduje się w słowniku."

elif [ $dictionary_exist -eq 1 ]; then 

    echo "Słowo \"$new_string\" nie znajduje się w słowniku."

    if [ $skip -eq 0 ];
    then
        echo "HAHA, NOOB"
    fi

    continue
fi

# echo $new_string

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