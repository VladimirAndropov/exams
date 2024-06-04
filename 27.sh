#!/bin/bash

user=$1
shell=$(grep "$user" /etc/passwd | cut -d: -f7)
if [ -n "$shell" ]; then
    echo "$shell"
else
    echo "User not found"
fi
