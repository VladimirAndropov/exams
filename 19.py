import re

hosts_file = "/etc/hosts"

# Проверяем существование файла /etc/hosts
if os.path.isfile(hosts_file):
    with open(hosts_file, 'r') as file:
        # Читаем файл построчно и проверяем каждую строку
        for line in file:
            if not line.startswith('127.0.0.1'):
                print(f"В файле {hosts_file} найдены записи, отличные от 127.0.0.1:")
                print(line.strip())
                break
        else:
            print(f"В файле {hosts_file} отсутствуют записи, отличные от 127.0.0.1.")
else:
    print(f"Файл {hosts_file} не найден.")
