import os
import time

def find_recently_modified_files(directory, threshold):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_modified_time = os.path.getmtime(file_path)
            except OSError as e:
                print(f"Ошибка при доступе к файлу {file_path}: {e}")
                continue
            if file_modified_time > threshold:
                print(file_path)

if __name__ == "__main__":
    home_dir = os.path.expanduser("~")  # Получаем путь к домашней директории пользователя
    one_week_ago = time.time() - 7 * 24 * 60 * 60  # Вычисляем временную метку, представляющую текущее время минус 7 дней
    find_recently_modified_files(home_dir, one_week_ago)
