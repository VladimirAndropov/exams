# python find_files.py /path/to/directory 1024

# Эта программа будет искать файлы в указанной директории и ее поддиректориях, выводя имена файлов, размер которых соответствует заданному размеру (в байтах).

import os
import sys

def find_files_by_size(directory, size):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # Получение размера файла
                file_size = os.path.getsize(file_path)
                # Проверка соответствия размера заданному
                if file_size == size:
                    print(file_path)
            except OSError:
                # Обработка ошибок доступа к файлу
                pass

if __name__ == "__main__":
    # Проверка количества аргументов командной строки
    if len(sys.argv) != 3:
        print("Usage: python find_files.py <directory> <size>")
        sys.exit(1)

    # Получение директории и размера из аргументов командной строки
    directory = sys.argv[1]
    size = int(sys.argv[2])

    # Проверка существования указанной директории
    if not os.path.isdir(directory):
        print("Error: Specified directory does not exist.")
        sys.exit(1)

    # Обход файлов в указанной директории и ее поддиректориях
    find_files_by_size(directory, size)
