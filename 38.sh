#!/bin/bash

log_file=$1
uniq -c "$log_file" | wc -l
