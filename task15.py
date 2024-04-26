import os
import sys
import datetime

def count_modified_files(directory):
    # Определение текущей даты и даты, предшествующей 3 дням
    current_date = datetime.datetime.now()
    three_days_ago = current_date - datetime.timedelta(days=3)

    # Счетчик измененных файлов
    modified_files_count = 0

    # Обход всех файлов в указанной директории
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            # Получение времени последнего изменения файла
            modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(filepath))
            # Проверка, был ли файл изменен в течение последних 3 дней
            if modified_time > three_days_ago:
                modified_files_count += 1

    return modified_files_count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python script.py <директория>")
        sys.exit(1)

    directory = sys.argv[1]

    # Проверка существования директории
    if not os.path.isdir(directory):
        print("Указанная директория не существует.")
        sys.exit(1)

    # Получение количества измененных файлов и вывод на экран
    modified_files_count = count_modified_files(directory)
    print("Количество файлов, измененных за последние 3 дня:", modified_files_count)
