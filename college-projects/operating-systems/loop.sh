# Function returning points
func1(){
    return
}

# Read words
if [ $# -ge 1 ]
then
    words=("$@")
else
    read words
fi

# Write words
for word in "${words[@]}"
do
    echo $word
done

# Loop through all words and calculate score
for word in "${words[@]}"
do
    # ((i++))

    # echo $i

    # if [ $i -ge 10 ]
    # then
    #     break
    # fi
    
    in_dict=true

    if [ $in_dict = "true" ]
    then
        echo "Wow, can I call You Paul?"

        continue
    fi

    echo "HAHA, you noob XD"
    echo "Repeat until you are useful BRUH"

done