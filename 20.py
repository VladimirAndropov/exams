import os
import sys
import datetime

log_file = '/tmp/run.log'


def log_run():
    if os.path.exists(log_file):
        with open(log_file, 'r') as file:
            count = sum(1 for line in file)
    else:
        count = 0

    with open(log_file, 'a') as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"Run at: {timestamp}\n")

    print("Hello")
    print(f"Number of previous runs: {count}", file=sys.stderr)


if __name__ == "__main__":
    log_run()
