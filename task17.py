import os
import datetime

def get_files_modified_last_week(directory):
    # Определение текущей даты и даты, предшествующей 7 дням
    current_date = datetime.datetime.now()
    week_ago = current_date - datetime.timedelta(days=7)

    # Список для хранения файлов, измененных за последнюю неделю
    modified_files = []

    # Обход всех файлов в указанной директории
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            # Получение времени последнего изменения файла
            modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(filepath))
            # Проверка, был ли файл изменен за последнюю неделю
            if modified_time > week_ago:
                modified_files.append(filepath)

    return modified_files

if __name__ == "__main__":
    home_directory = os.path.expanduser("~")
    modified_files = get_files_modified_last_week(home_directory)

    if modified_files:
        print("Файлы, измененные за последнюю неделю в домашней директории:")
        for file in modified_files:
            print(file)
    else:
        print("В домашней директории нет файлов, измененных за последнюю неделю.")
