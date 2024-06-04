#!/bin/bash

for file in ~/$(find ~ -type f -mtime -30 -mtime -7); do
    sed -i 's/test/tset/g' "$file"
done
