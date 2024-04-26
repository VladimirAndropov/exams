import multiprocessing
import math

# Функция для проверки числа на простоту
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, max_divisor + 1, 2):
        if n % d == 0:
            return False
    return True

# Функция для проверки чисел на простоту в различных потоках
def check_prime_numbers():
    number = 0
    while True:
        if is_prime(number):
            print("Простое число:", number)
        number += 1

if __name__ == "__main__":
    # Создание пула процессов
    pool = multiprocessing.Pool()

    # Запуск функции проверки чисел на простоту в каждом процессе
    for _ in range(multiprocessing.cpu_count()):
        pool.apply_async(check_prime_numbers)

    # Ожидание команды от пользователя для завершения программы
    input("Нажмите Enter для остановки программы...\n")

    # Закрытие пула процессов
    pool.terminate()
