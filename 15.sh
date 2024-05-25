#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

if [ ! -d "$1" ]; then
    echo "Error: '$1' is not a directory."
    exit 1
fi

current_date=$(date +%Y-%m-%d)

three_days_ago=$(date -d "3 days ago" +%s)

modified_files_count=0

find "$1" -type f -newermt "$current_date - 3 days" -print0 | while IFS= read -r -d '' file; do
    modified_files_count=$((modified_files_count + 1))
done

echo "Number of files modified in the last 3 days in '$1': $modified_files_count"