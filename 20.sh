#!/bin/bash

# Определяем путь к файлу журнала
log_file="/tmp/run.log"

# Получаем текущую дату и время
current_datetime=$(date +"%Y-%m-%d %H:%M:%S")

# Записываем дату и время запуска в файл журнала
echo "Script run at: $current_datetime" >> "$log_file"

# Выводим "Hello" в стандартный вывод
echo "Hello"

# Считаем количество предыдущих запусков программы из файла журнала
previous_runs=$(wc -l < "$log_file")

# Выводим количество предыдущих запусков в stderr
echo "Number of previous runs: $previous_runs" >&2
