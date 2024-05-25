#!/bin/bash

install_program() {
    echo "Установка программы: $1"
    # Добавьте здесь команду установки программы
    # Например, для apt-get:
    # sudo apt-get install -y "$1"
}

if [ $# -eq 1 ] && [ -f "$1" ]; then
    programs=$(cat "$1")
else
    programs="$@"
fi

if [ -z "$programs" ]; then
    echo "Не указан список программ для установки."
    exit 1
fi

for program in $programs; do
    install_program "$program"
done