import datetime
import logging
import sys

# Настройка логгера
logger = logging.getLogger(__name__)
handler = logging.FileHandler("/tmp/run.log")
handler.setFormatter(logging.Formatter("%(asctime)s: %(message)s"))
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def get_previous_run_count():
    try:
        with open("/tmp/previous_run_count.txt", "r") as file:
            return int(file.readline().strip())
    except FileNotFoundError:
        return 0

def store_previous_run_count(count):
    with open("/tmp/previous_run_count.txt", "w") as file:
        file.write(str(count))

def main():
    # Вывод "Hello" в стандартный вывод
    print("Hello")

    # Вывод количества предыдущих запусков в stderr
    previous_run_count = get_previous_run_count()
    logger.error(f"Предыдущих запусков: {previous_run_count}")
    new_run_count = previous_run_count + 1
    store_previous_run_count(new_run_count)

    # Запись строки с датой и временем запуска в журнал
    now = datetime.datetime.now()
    logger.info(f"Запуск скрипта в {now}")

if __name__ == "__main__":
    main()