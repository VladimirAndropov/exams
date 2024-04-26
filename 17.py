import os
import datetime

# Функция для получения списка файлов в директории
def get_files_in_dir(dir_path):
    return [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]

# Функция для получения даты за последнюю неделю
def get_last_week_date():
    now = datetime.datetime.now()
    return now - datetime.timedelta(days=7)

# Главная функция
def main():
    home_dir = os.path.expanduser("~")
    last_week_date = get_last_week_date()

    files_in_home_dir = get_files_in_dir(home_dir)
    modified_files = [f for f in files_in_home_dir if os.path.getmtime(os.path.join(home_dir, f)) >= last_week_date.timestamp()]

    if modified_files:
        print("Файлы в домашней директории, измененные за последнюю неделю:")
        for file in modified_files:
            print(file)
    else:
        print("В домашней директории за последнюю неделю никто ничего не изменил.")

if __name__ == "__main__":
    main()