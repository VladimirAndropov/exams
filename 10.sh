#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Usage: $0 <filename> <remote_host>"
    exit 1
fi

filename=$1
remote_host=$2

scp "$remote_host:$filename" .

if [ $? -eq 0 ]; then
    echo "Файл '$filename' успешно скопирован из $remote_host."
else
    echo "Ошибка: не удалось скопировать файл '$filename' из $remote_host."
fi