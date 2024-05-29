import sys
import threading
import math

# Функция для вычисления части ряда в заданном диапазоне
def calculate_partial_sum(start, end):
    partial_sum = 0
    for i in range(start, end):
        partial_sum += ((-1) ** i) / (2 * i + 1)
    return partial_sum

# Функция для вычисления числа π с использованием многопоточности
def estimate_pi(num_threads):
    segment_size = math.ceil(1000000 / num_threads)
    threads = []
    partial_results = [0] * num_threads

    def worker(thread_index, start, end):
        partial_results[thread_index] = calculate_partial_sum(start, end)

    # Создаем и запускаем потоки
    for i in range(num_threads):
        start_idx = i * segment_size
        end_idx = min((i + 1) * segment_size, 1000000)
        thread = threading.Thread(target=worker, args=(i, start_idx, end_idx))
        threads.append(thread)
        thread.start()

    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()

    # Суммируем частичные результаты
    pi_estimate = sum(partial_results) * 4
    return pi_estimate

if __name__ == "__main__":
    # Проверка наличия аргумента командной строки (количество потоков)
    if len(sys.argv) != 2:
        print("Usage: python 5.py <num_threads>")
        sys.exit(1)

    # Получаем количество потоков из аргумента командной строки
    num_threads = int(sys.argv[1])

    # Вычисляем значение π с использованием заданного количества потоков
    pi_value = estimate_pi(num_threads)
    print("Estimated value of pi:", pi_value)
