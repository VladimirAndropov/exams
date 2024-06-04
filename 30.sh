#!/bin/bash

file=$1
if [ "$file" != "*" ]; then
    rm -f /home/"$file"
fi
