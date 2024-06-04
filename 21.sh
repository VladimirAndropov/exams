#!/bin/bash

for file in /var/log/*; do
    if [ -f "$file" ]; then
        size=$(du -h "$file" | awk '{print $1}' | sed 's/M//')
        if [ "$size" -gt 50 ]; then
            echo "$file"
        fi
    fi
done
