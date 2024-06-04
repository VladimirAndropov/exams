#!/bin/bash

while true; do
    if ! pgrep -f script13 > /dev/null; then
        ./script13 &
    fi
    sleep 13
done
