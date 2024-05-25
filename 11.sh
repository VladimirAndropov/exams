#!/bin/bash

is_number() {
  [[ "$1" =~ ^-?[0-9]+$ ]]
}

if [ "$#" -ne 2 ] || ! is_number "$1" || ! is_number "$2"; then
  echo "Ошибка: Скрипт требует два числовых аргумента."
  echo "Использование: $0 <начало диапазона> <конец диапазона>"
  exit 1
fi

start=$1
end=$2

if [ "$start" -gt "$end" ]; then
  echo "Ошибка: Начало диапазона должно быть меньше или равно концу диапазона."
  exit 1
fi

for ((i = start; i <= end; i++)); do
  if (( i % 12 == 0 )); then
    echo "$i"
  fi
done