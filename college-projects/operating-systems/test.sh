#!/bin/bash

if [ $# -ne 1 ]
then
    echo "BRUH"
    exit
fi

file=$1

echo "You have written \"$file\""

if [ -e $file ]
then
    echo "Haha"
else
    echo "NOOOO"
fi