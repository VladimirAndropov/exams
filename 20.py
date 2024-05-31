import datetime
import sys

log_file = "/tmp/run.log"

# Получаем текущую дату и время
current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Записываем дату и время запуска в файл журнала
with open(log_file, 'a') as file:
    file.write(f"Script run at: {current_datetime}\n")

# Выводим "Hello" в стандартный вывод
print("Hello")

# Считаем количество предыдущих запусков программы из файла журнала
with open(log_file, 'r') as file:
    previous_runs = sum(1 for line in file)

# Выводим количество предыдущих запусков в stderr
print(f"Number of previous runs: {previous_runs}", file=sys.stderr)
