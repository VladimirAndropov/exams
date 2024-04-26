# Этот скрипт принимает путь к каталогу в качестве аргумента командной строки. Он перебирает все файлы в этом каталоге и его подкаталогах, сравнивает время их последнего изменения с текущим временем, и увеличивает счетчик, если файл был изменен в течение последних трех дней. По завершении выводит количество измененных файлов.

import os
import sys
import time

def count_modified_files(directory):
    # Получаем текущее время в секундах
    current_time = time.time()

    # Вычисляем время, прошедшее за последние три дня (3 * 24 * 60 * 60 секунд)
    three_days_ago = current_time - (3 * 24 * 60 * 60)

    # Счетчик измененных файлов
    modified_files_count = 0

    # Перебираем все элементы в указанном каталоге
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Получаем путь к файлу
            file_path = os.path.join(root, file)
            # Получаем время последнего изменения файла
            modification_time = os.path.getmtime(file_path)
            # Проверяем, был ли файл изменен в течение последних трех дней
            if modification_time >= three_days_ago:
                modified_files_count += 1

    return modified_files_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python count_modified_files.py <directory>")
        return

    directory = sys.argv[1]

    if not os.path.isdir(directory):
        print("Error: '{}' is not a valid directory.".format(directory))
        return

    modified_files_count = count_modified_files(directory)
    print("Number of files modified in the last 3 days in '{}': {}".format(directory, modified_files_count))

if __name__ == "__main__":
    main()
