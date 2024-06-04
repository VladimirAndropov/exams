#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

dir=$1
find "$dir" -type f -mtime -2 -print0 | tar -czf archive.tar.gz --null -T -
