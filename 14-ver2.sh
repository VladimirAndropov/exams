# Этот скрипт принимает PID процесса в качестве аргумента. Затем он использует команду pstree с опцией -p, чтобы вывести дерево процессов для указанного PID, включая все его потомки.
# ps --forest -o pid,tty,stat,time,cmd -g 2795

#!/bin/bash

# Проверяем, передан ли аргумент - PID процесса
if [ $# -ne 1 ]; then
    echo "Usage: $0 <PID>"
    exit 1
fi

# Получаем PID процесса из аргумента
pid=$1

# Проверяем существует ли процесс с указанным PID
if ! ps -p "$pid" > /dev/null; then
    echo "Error: Process with PID $pid does not exist."
    exit 1
fi

# Используем команду pstree для вывода всех потомков процесса по его PID
pstree -p "$pid"
