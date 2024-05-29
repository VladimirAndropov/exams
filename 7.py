import multiprocessing
import time
import sys

# Функция для проверки, является ли число простым
def check_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    factor = 5
    while factor * factor <= number:
        if number % factor == 0 or number % (factor + 2) == 0:
            return False
        factor += 6
    return True

# Функция для поиска простых чисел в заданном диапазоне
def find_primes(start, step, output_queue):
    num = start
    while True:
        if check_prime(num):
            output_queue.put(num)
        num += step

if __name__ == "__main__":
    prime_output = multiprocessing.Queue()
    num_workers = multiprocessing.cpu_count()
    processes = []

    # Запуск нескольких процессов для параллельного поиска простых чисел
    for i in range(num_workers):
        process = multiprocessing.Process(target=find_primes, args=(i * 2 + 1, num_workers * 2, prime_output))
        processes.append(process)
        process.start()

    try:
        while True:
            # Печать найденных простых чисел по мере их нахождения
            while not prime_output.empty():
                prime = prime_output.get()
                print(f"Found prime number: {prime}")
            time.sleep(0.1)  # Небольшая задержка для снижения нагрузки на процессор
    except KeyboardInterrupt:
        print("Program stopped by user.")
        for process in processes:
            process.terminate()
        for process in processes:
            process.join()
