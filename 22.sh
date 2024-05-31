#!/bin/bash
: '
Написать скрипт на Bash, который должен принимать в качестве
аргумента любую строку и удалять из /home/
каталог с именем, соответствующим переданной строке
без необходимости отвечать утвердительно на вопросы системы.
'

# Если кол-во переданных параметров не 1
if [[ $(($#)) -ne 1 ]] ; then
    echo "Ошибка: Необходимо передать параметр в виде названия файла в /home" >&2
    exit 1
fi

#Переменная с названием файла, который передали через параметр
file_name=$1
#Текущая директория, чтоб вернуться в нее потом
current_path=$(pwd)
#Переход в домашний каталог /home
cd

#Если файл существует
if [ -f "$file_name" ]; then
    echo "Файл $file_name существует"
    #Удаляем файл
    rm -f $file_name
    echo "Удалили файл $file_name"
else 
    echo "Файла $file_name не существует!"
fi

#Переход туда, откуда запускался скрипт
cd $current_path
echo "Завершили работу скрипта"
