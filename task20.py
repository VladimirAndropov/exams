import sys
import os
import datetime

def log_run():
    # Открытие файла журнала в режиме дополнения
    log_file = "/tmp/run.log"
    with open(log_file, "a") as file:
        # Запись даты и времени запуска в файл журнала
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"Запуск скрипта: {current_time}\n")

    # Вывод "Hello" в стандартный вывод
    print("Hello")

    # Подсчет количества предыдущих запусков программы
    try:
        with open(log_file, "r") as file:
            lines = file.readlines()
            previous_runs = len([line for line in lines if "Запуск скрипта" in line])
        # Вывод количества предыдущих запусков в stderr
        print(previous_runs, file=sys.stderr)
    except FileNotFoundError:
        print("Ошибка: Файл журнала не найден.", file=sys.stderr)

if __name__ == "__main__":
    log_run()
