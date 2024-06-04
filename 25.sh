#!/bin/bash

user=$1
ps -u "$user" -o pid --sort pid | head -n 10
