import os
import time


def list_recent_files():
    now = time.time()
    one_week_ago = now - 7 * 86400

    home_dir = os.path.expanduser('~')
    for root, dirs, files in os.walk(home_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getmtime(file_path) >= one_week_ago:
                print(file_path)


if __name__ == "__main__":
    list_recent_files()
