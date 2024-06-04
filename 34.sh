#!/bin/bash

df -h | awk '{if ($4 < 100) print $1"|"$4}'
