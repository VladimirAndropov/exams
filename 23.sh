#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Usage: $0 <minutes> <directory>"
    exit 1
fi

minutes=$1
dir=$2
find "$dir" -type f -mmin +$minutes -delete
