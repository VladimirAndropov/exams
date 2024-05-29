import multiprocessing
import time
import sys

def is_prime(n):
    """Проверяет, является ли число простым."""
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

def find_primes(start, end, queue):
    """Ищет простые числа в заданном диапазоне и кладет их в очередь."""
    for num in range(start, end):
        if is_prime(num):
            queue.put(num)

if __name__ == "__main__":
    prime_queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=find_primes, args=(0, sys.maxsize, prime_queue))
    process.start()

    try:
        while True:
            while not prime_queue.empty():
                prime = prime_queue.get()
                print(f"Простое число найдено: {prime}")
            time.sleep(0.1)  # Небольшая задержка для снижения нагрузки на процессор
    except KeyboardInterrupt:
        print("Программа остановлена пользователем.")
        process.terminate()
