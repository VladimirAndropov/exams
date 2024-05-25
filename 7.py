import multiprocessing
import time
import sys


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def check_prime_process(start, end, results):
    for num in range(start, end):
        if is_prime(num):
            results.put(num)


results = multiprocessing.Queue()

process = multiprocessing.Process(target=check_prime_process, args=(0, sys.maxsize, results))
process.start()

try:
    while True:
        if not results.empty():
            prime_number = results.get()
            print("Найдено простое число:", prime_number)
except KeyboardInterrupt:
    print("Программа остановлена пользователем")
    process.terminate()
