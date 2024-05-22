#!/bin/bash

# Функция для генерации случайных чисел
generate_random_numbers() {
  local range=50
  local count=5
  local numbers=()
  
  while [ "${#numbers[@]}" -lt "$count" ]; do
    num=$((RANDOM % range + 1))
    if [[ ! " ${numbers[@]} " =~ " $num " ]]; then
      numbers+=("$num")
    fi
  done

  echo "${numbers[@]}"
}

# Генерация случайных чисел
random_numbers=$(generate_random_numbers)

# Текущая дата и время
current_datetime=$(date "+%Y-%m-%d %H:%M:%S")

# Вывод на stdout
echo "Случайные числа: $random_numbers"
echo "Дата и время генерации: $current_datetime"

# Запись в файл
output_file="lototron_output.txt"
{
  echo "Случайные числа: $random_numbers"
  echo "Дата и время генерации: $current_datetime"
} > "$output_file"

