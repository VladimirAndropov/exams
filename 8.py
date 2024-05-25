import os
import sys

def find_files_by_size(directory, size):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_size = os.path.getsize(file_path)
                if file_size == size:
                    print(file_path)
            except OSError:
                pass

if len(sys.argv) != 3:
    print("Usage: python find_files.py <directory> <size>")
    sys.exit(1)

directory = sys.argv[1]
size = int(sys.argv[2])

if not os.path.isdir(directory):
    print("Ошибка: директория не существует.")
    sys.exit(1)

find_files_by_size(directory, size)
