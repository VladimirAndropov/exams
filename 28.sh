#!/bin/bash

home_dir=$(grep www-data /etc/passwd | cut -d: -f6)
if [ -n "$home_dir" ]; then
    echo "$home_dir"
else
    echo "User www-data not found"
fi
