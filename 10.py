#!/bin/bash

# Проверяем, переданы ли аргументы - имя файла и адрес хоста
if [ $# -ne 2 ]; then
    echo "Usage: $0 <filename> <remote_host>"
    exit 1
fi

# Получаем имя файла и адрес хоста из аргументов
filename=$1
remote_host=$2

# Копируем файл с удаленного хоста в текущую папку
scp -q "$remote_host:$filename" .

# Проверяем статус выполнения команды scp
if [ $? -eq 0 ]; then
    echo "File '$filename' copied successfully from $remote_host."
else
    echo "Error: Failed to copy file '$filename' from $remote_host."
fi
