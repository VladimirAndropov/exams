#!/bin/bash

if [ -z "$1" ]; then
    echo "Ошибка: не указан файл для анализа."
    echo "Использование: $0 имя_файла"
    exit 1
fi

file=$1

if [ ! -f "$file" ]; then
    echo "Файл '$file' не найден."
    exit 1
fi

unique_count=$(sort "$file" | uniq | wc -l)

echo "Количество уникальных записей в файле '$file': $unique_count"

