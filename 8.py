import os
import sys

def find_files_by_size(dir_path, size):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getsize(file_path) == size:
                print(file_path)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        directory = sys.argv[1]
        file_size = int(sys.argv[2])
        find_files_by_size(directory, file_size)
    else:
        print("Please provide a directory and a file size as arguments.")
