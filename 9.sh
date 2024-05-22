#!/bin/bash


echo "Список открытых портов:"
netstat -tulpn | awk '/LISTEN/ {print $4}' | sed -E 's/.*:([0-9]+)/\1/'

