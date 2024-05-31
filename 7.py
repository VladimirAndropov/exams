import multiprocessing
import time
import sys

# Функция для проверки числа на простоту
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

# Функция для проверки чисел на простоту в отдельном процессе
def check_prime_process(start, end, results):
    for num in range(start, end):
        if is_prime(num):
            results.put(num)

if __name__ == "__main__":
    # Создание очереди для результатов
    results = multiprocessing.Queue()

    # Создание пула процессов
    pool = multiprocessing.Pool()

    try:
        while True:
            # Запуск проверки чисел на простоту в нескольких процессах
            pool.starmap(check_prime_process, [(i*10000, (i+1)*10000, results) for i in range(multiprocessing.cpu_count())])
            
            # Вывод результатов
            while not results.empty():
                prime_number = results.get()
                print("Found prime number:", prime_number)
            
            time.sleep(0.1)  # Задержка для уменьшения нагрузки на процессор

    except KeyboardInterrupt:
        # Прерывание программы по нажатию Ctrl+C
        print("Program stopped by user.")
        pool.terminate()
