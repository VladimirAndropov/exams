import re
import os

hosts_file = "/etc/hosts"

# Проверяем существование файла /etc/hosts
if os.path.isfile(hosts_file):
    with open(hosts_file, 'r') as file:
        lines = file.readlines()
    
    # Ищем записи, отличные от 127.0.0.1
    invalid_lines = [line.strip() for line in lines if not re.match(r'^127\.0\.0\.1', line)]

    # Проверяем, были ли найдены записи отличные от 127.0.0.1
    if invalid_lines:
        print(f"В файле {hosts_file} найдены записи, отличные от 127.0.0.1:")
        for line in invalid_lines:
            print(line)
    else:
        print(f"В файле {hosts_file} отсутствуют записи, отличные от 127.0.0.1.")
else:
    print(f"Файл {hosts_file} не найден.")
