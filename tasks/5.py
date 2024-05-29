import sys
import threading
import math

# Функция для вычисления части ряда Эйлера в заданном диапазоне
def compute_segment_sum(start, end):
    segment_sum = 0
    for k in range(start, end):
        segment_sum += ((-1) ** k) / (2 * k + 1)
    return segment_sum

# Функция для вычисления числа π с использованием многопоточности
def compute_pi_with_threads(thread_count):
    segment_length = math.ceil(1000000 / thread_count)
    threads = []
    results = [0] * thread_count

    def worker(thread_index, start, end):
        results[thread_index] = compute_segment_sum(start, end)

    # Создание и запуск потоков
    for i in range(thread_count):
        start_index = i * segment_length
        end_index = min((i + 1) * segment_length, 1000000)
        thread = threading.Thread(target=worker, args=(i, start_index, end_index))
        threads.append(thread)
        thread.start()

    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()

    # Суммирование частичных сумм
    pi_estimate = sum(results) * 4

    return pi_estimate

if __name__ == "__main__":
    # Проверка наличия аргумента командной строки (количество потоков)
    if len(sys.argv) != 2:
        print("Usage: python euler_series.py <num_threads>")
        sys.exit(1)

    # Получение количества потоков из аргумента командной строки
    num_threads = int(sys.argv[1])

    # Вычисление числа π с использованием заданного количества потоков
    pi_value = compute_pi_with_threads(num_threads)
    print("Estimated value of pi:", pi_value)
