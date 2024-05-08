
# Этот скрипт использует команду find для поиска файлов в указанном каталоге, которые были изменены в течение последних трех дней. Затем он считает количество найденных файлов и выводит это количество на экран.

#!/bin/bash

# Проверяем, передан ли аргумент - каталог
if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

# Проверяем, существует ли указанный каталог
if [ ! -d "$1" ]; then
    echo "Error: '$1' is not a directory."
    exit 1
fi

# Получаем текущую дату в формате YYYY-MM-DD
current_date=$(date +%Y-%m-%d)

# Получаем временную метку для текущей даты минус 3 дня в секундах
three_days_ago=$(date -d "3 days ago" +%s)

# Счетчик измененных файлов
modified_files_count=0

# Используем команду find для поиска файлов в указанном каталоге,
# которые были изменены в течение последних трех дней, и увеличиваем
# счетчик для каждого найденного файла
find "$1" -type f -newermt "$current_date - 3 days" -print0 | while IFS= read -r -d '' file; do
    modified_files_count=$((modified_files_count + 1))
done

# Выводим количество измененных файлов на экран
echo "Number of files modified in the last 3 days in '$1': $modified_files_count"
