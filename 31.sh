#!/bin/bash

for file in "$1"/*; do
    if [ -f "$file" ]; then
        size=$(du -h "$file" | awk '{print $1}' | sed 's/M//')
        if [ "$size" -gt 50 ]; then
            echo "$file"
        fi
    fi
done
