import sys
import threading
import math

# Функция для вычисления части ряда Эйлера в заданном диапазоне
def calculate_partial_sum(start, end):
    partial_sum = 0
    for k in range(start, end):
        partial_sum += ((-1) ** k) / (2 * k + 1)
    return partial_sum

# Функция для вычисления числа π с использованием многопоточности
def calculate_pi(num_threads):
    # Вычисление размера каждой части ряда для каждого потока
    chunk_size = int(math.ceil(1000000 / num_threads))
    threads = []
    partial_sums = [0] * num_threads

    # Создание и запуск потоков
    for i in range(num_threads):
        start = i * chunk_size
        end = min((i + 1) * chunk_size, 1000000)
        thread = threading.Thread(target=calculate_partial_sum, args=(start, end))
        threads.append(thread)
        thread.start()

    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()

    # Суммирование частичных сумм
    pi = sum(partial_sums) * 4

    return pi

if __name__ == "__main__":
    # Проверка наличия аргумента командной строки (количество потоков)
    if len(sys.argv) != 2:
        print("Usage: python euler_series.py <num_threads>")
        sys.exit(1)

    # Получение количества потоков из аргумента командной строки
    num_threads = int(sys.argv[1])

    # Вычисление числа π с использованием заданного количества потоков
    pi = calculate_pi(num_threads)
    print("Estimated value of pi:", pi)