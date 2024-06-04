#!/bin/bash

cmd=$1
shift
for user in "$@"; do
    sudo -u "$user" $cmd
done
