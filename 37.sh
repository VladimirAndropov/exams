#!/bin/bash

for ext in "$@"; do
    mv data/*."$ext" tabs/
done
