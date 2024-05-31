#!/bin/bash

# Записываем результат выполнения команды netstat в переменную
netstat_output=$(netstat -tuln 2>/dev/null)

# Проверяем успешность выполнения команды netstat
if [ $? -ne 0 ]; then
    echo "Ошибка: Невозможно получить информацию о сетевых соединениях."
    exit 1
fi

# Используем awk для фильтрации вывода netstat и вывода списка открытых портов
open_ports=$(echo "$netstat_output" | awk '/LISTEN/ {split($4, a, ":"); print a[length(a)]}')

# Выводим список открытых портов на данной машине
echo "Список открытых портов на данной машине:"
echo "$open_ports"
