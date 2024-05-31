import os
import time

home_dir = os.path.expanduser("~")  # Получаем путь к домашней директории пользователя
one_week_ago = time.time() - 7 * 24 * 60 * 60  # Вычисляем временную метку, представляющую текущее время минус 7 дней

for root, dirs, files in os.walk(home_dir):
    for file in files:
        file_path = os.path.join(root, file)
        stat = os.stat(file_path)
        if stat.st_mtime > one_week_ago:
            print(file_path)
