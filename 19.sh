# Этот скрипт проверяет, существует ли файл /etc/hosts. Если файл существует, он использует grep для поиска всех строк, которые не начинаются с 127.0.0.1. Если такие строки найдены, скрипт выводит сообщение о наличии записей, отличных от 127.0.0.1. Если таких записей нет, скрипт сообщает об их отсутствии. Если файл /etc/hosts не существует, выводится сообщение об этом.

#!/bin/bash

# Путь к файлу /etc/hosts
hosts_file="/etc/hosts"

# Проверяем существование файла /etc/hosts
if [ -f "$hosts_file" ]; then
    # Используем grep для поиска записей, отличных от 127.0.0.1
    result=$(grep -v '^127\.0\.0\.1' "$hosts_file")

    # Проверяем, были ли найдены записи отличные от 127.0.0.1
    if [ -n "$result" ]; then
        echo "В файле $hosts_file найдены записи, отличные от 127.0.0.1:"
        echo "$result"
    else
        echo "В файле $hosts_file отсутствуют записи, отличные от 127.0.0.1."
    fi
else
    echo "Файл $hosts_file не найден."
fi
