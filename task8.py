import os
import sys

def list_files_by_size(directory, size):
    # Рекурсивный обход всех файлов в директории
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            # Получение размера файла
            file_size = os.path.getsize(filepath)
            # Проверка соответствия размера заданному значению
            if file_size == size:
                print("Файл:", filepath)

if __name__ == "__main__":
    # Проверка наличия двух аргументов командной строки
    if len(sys.argv) != 3:
        print("Использование: python list_files_by_size.py <директория> <размер>")
        sys.exit(1)

    directory = sys.argv[1]
    size = int(sys.argv[2])

    # Проверка существования директории
    if not os.path.isdir(directory):
        print("Указанная директория не существует.")
        sys.exit(1)

    # Вызов функции для вывода файлов с заданным размером
    list_files_by_size(directory, size)
