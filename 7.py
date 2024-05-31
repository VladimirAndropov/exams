import multiprocessing
import time

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
def check_prime_process(start, end):
    results = []
    for num in range(start, end):
        if is_prime(num):
            results.append(num)
    return results

if __name__ == "__main__":
    try:
        with multiprocessing.Pool() as pool:
            while True:
                # Запуск проверки чисел на простоту в нескольких процессах
                results = pool.imap_unordered(check_prime_process, [(i*10000, (i+1)*10000) for i in range(multiprocessing.cpu_count())])

                # Вывод результатов
                for result in results:
                    for prime_number in result:
                        print("Found prime number:", prime_number)

                time.sleep(0.1)  # Задержка для уменьшения нагрузки на процессор

    except KeyboardInterrupt:
        # Прерывание программы по нажатию Ctrl+C
        print("Program stopped by user.")
