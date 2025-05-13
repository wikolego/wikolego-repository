new_string="test"

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

fi