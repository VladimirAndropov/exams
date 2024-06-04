#!/bin/bash

if [ -z "$1" ]; then
    echo "Ошибка: не указан каталог для проверки."
    echo "Использование: $0 путь_к_каталогу"
    exit 1
fi

directory=$1

changed_files=$(find "$directory" -type f -mtime -1)

if [ -z "$changed_files" ]; then
    echo "В каталоге '$directory' файлы не изменялись за последние сутки."
else
    echo "Список файлов, изменённых за последние сутки в каталоге '$directory':"
    echo "$changed_files"
fi

