#!/bin/bash

log_file="/tmp/run.log"

current_datetime=$(date +"%Y-%m-%d %H:%M:%S")

echo "Script run at: $current_datetime" >> "$log_file"

echo "Hello"

previous_runs=$(wc -l < "$log_file")

echo "Number of previous runs: $previous_runs" >&2