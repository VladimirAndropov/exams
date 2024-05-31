import os
import sys
import time


def count_recent_files(dir_path):
    now = time.time()
    three_days_ago = now - 3 * 86400
    count = 0

    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getmtime(file_path) >= three_days_ago:
                count += 1

    print(f"Number of files modified in the last 3 days: {count}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        directory = sys.argv[1]
        count_recent_files(directory)
    else:
        print("Please provide a directory as argument.")
