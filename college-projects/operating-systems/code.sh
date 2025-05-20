#!/bin/bash
    
# Function returning points
func1(){

    # input string
    str=$1

    # 0 - skip if the word does not exists in dictionary, 1 - otherwise
    skip=$2
    
    # input dictionary
    dictionary_path=$3

    # arguments_array="$@"
    letters_points=(1 3 3 2 1 4 2 4 1 8 5 1 3 1 1 3 10 1 1 1 1 4 4 8 4 10)
    letters_points+=("A" "B" "C" "D" "E" "F" "G" "H" "I" "J" "K" "L" "M" "N" "O" "P" "Q" "R" "S" "T" "U" "V" "W" "X" "Y" "Z")

    # test=(1 2 3)
    # test+=("a" "b" "c")

    # echo ${test[4]}

    # letters_points_2=((1 "A") (3 "B") (3 "C") (2 "D") (1 "E") (4 "F") (2 "G") (4 "H") (1 "I") (8 "J") (5 "K") (1 "L") (3 "M") (1 "N") (1 "O") (3 "P") (10 "Q") (1 "R") (1 "S") (1 "T") (1 "U") (4 "V") (4 "W") (8 "X") (4 "Y") (10 "Z"))

    # A B C D E F G H I J K L M N O P  Q R S T U V W X Y  Z
    # 1 3 3 2 1 4 2 4 1 8 5 1 3 1 1 3 10 1 1 1 1 4 4 8 4 10

    # converting uppercase letters in string to lowercase letters
    new_string=$(echo $str | tr '[:upper:]' '[:lower:]')

    # 0 - word not in dictionary, 1 - otherwise
    in_dictionary=0

    # Check if word exists in dictionary
    if grep -i -q "^$new_string$" "$dictionary_path"; then
        echo "Słowo \"$new_string\" jest poprawne."
    else 
        echo "Słowo \"$new_string\" nie jest poprawne."

        if [ $skip -eq 0 ]; then
            return
        fi
    fi

    # walk through each of the letters in string and add to characters_array
    characters_array=()

    for ((i=0; i<${#new_string}; i++))
    {
        characters_array+=("${new_string:$i:1}")
    }

    # calculate result
    res=0

    for c in "${characters_array[@]}"
    {
        ascii_value=$(printf "%d" "'$c")

        index=$((ascii_value-97))
        
        val=${letters_points[$index]}

        res=$((res+val))
        
        index2=$((index+26))
        x=${letters_points[$index2]}
        echo $x
    }

    echo $res
}

# path to dictionary
dictionary_path="/usr/share/dict/words"

# 0 - show help, 1 - otherwise
h_opt=1

# 0 - skip words not in dictionary, 1 - otherwise
d_opt=1

# 0 - dictionary exists, 1 - otherwise
dict_exists=0

words=()

i=0
while [ $i -lt $# ]; do
    i=$((i+1))
    arg="${!i}"
    case "$arg" in
        -h)
            h_opt=0
            ;;
        -d)
            d_opt=0
            ;;
        -f)

            # Check if next argument is a path
            if [ $i -lt $# ]; then
                i=$((i+1))
                dictionary_path="${!i}"
            else
                echo "Błąd: Brak ścieżki do słownika po fladze -f"
                exit 1
            fi

            dict_exists=1

            ;;
        -*)
            echo "Błąd: Nieznana flaga: $arg"
            echo "Użyj -h aby uzyskać pomoc"
            exit 1
            ;;
        *)
            # If not a flag
            words+=("$arg")
            ;;
    esac
done

# Test if dictionary exist
if [ ! -f "$dictionary_path" ]; then
    echo "Błąd: Słownik $dictionary_path nie istnieje." 
    exit 1
fi

# Display only help, if added -h
if [ $h_opt -eq 0 ]; then
    cat ./help.txt
    exit 0
fi

# Read word, if input does not contain any words
if [ ${#words[@]} -eq 0 ]; then
    read -a words
fi

# Loop through all words and calculate score
for word in "${words[@]}"; do
    func1 $word $d_opt $dictionary_path
done
