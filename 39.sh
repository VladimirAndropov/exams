#!/bin/bash
: '
Напишите скрипт, который считает кол-во уникальных записей из файла,
переданного как параметр и выводит на экран.
'

# Если кол-во переданных параметров не 1
if [[ $(($#)) -ne 1 ]] ; then
    echo "Ошибка: Некорректное кол-во переданных аргументов" >&2
    exit 1
fi

#Название файла
filename=$1

#Если файл существует
if [ -f "$filename" ]; then
    echo "Файл $filename существует."

#Если файл не существует
else 
    echo "Файл $filename не существует." >&2
    exit 1
fi

#Подсчет кол-ва уникальных строк в файле (с помощью wc)
lines_number=$(sort $filename | uniq -u | wc -l)

#Вывод на экран
echo "Количество уникальных строк в файле $filename = $lines_number"
