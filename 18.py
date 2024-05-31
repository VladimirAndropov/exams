import subprocess
import sys

# Функция для установки программы
def install_program(program):
    print(f"Установка программы: {program}")
    # Добавьте здесь команду установки программы
    # Например, для apt-get:
    # subprocess.run(["sudo", "apt-get", "install", "-y", program])

# Проверяем, передан ли аргумент с текстовым файлом
if len(sys.argv) == 2 and sys.argv[1].endswith('.txt'):
    with open(sys.argv[1], 'r') as file:
        programs = file.read().splitlines()
else:
    programs = sys.argv[1:]

# Проверяем, есть ли программы для установки
if not programs:
    print("Не указан список программ для установки.")
    sys.exit(1)

# Перебираем каждую программу из списка и устанавливаем её
for program in programs:
    install_program(program)
