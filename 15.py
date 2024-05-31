import os
import sys
from datetime import datetime, timedelta

def count_modified_files(directory):
    # Проверяем, существует ли указанный каталог
    if not os.path.exists(directory) or not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a directory.")
        sys.exit(1)

    # Получаем текущую дату
    current_date = datetime.now()

    # Вычисляем дату, которая была 3 дня назад
    three_days_ago = current_date - timedelta(days=3)

    # Счетчик измененных файлов
    modified_files_count = 0

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            if file_modified_time > three_days_ago:
                modified_files_count += 1

    return modified_files_count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <directory>".format(sys.argv[0]))
        sys.exit(1)

    directory = sys.argv[1]
    modified_files_count = count_modified_files(directory)
    print("Number of files modified in the last 3 days in '{}': {}".format(directory, modified_files_count))
