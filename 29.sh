#!/bin/bash

dir=$1
if [ "$dir" != "*" ]; then
    rm -rf /home/"$dir"
fi
