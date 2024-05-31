import os
import sys

def find_files_by_size(directory, size):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getsize(file_path) == size:
                print(file_path)

if __name__ == "__main__":
    # Проверяем передачу двух аргументов командной строки
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory> <size>")
        sys.exit(1)

    directory = sys.argv[1]
    size = int(sys.argv[2])

    # Проверяем, является ли переданная директория действительно директорией
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a directory.")
        sys.exit(1)

    find_files_by_size(directory, size)
