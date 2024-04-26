import sys
import threading
import math

# Функция для вычисления суммы членов ряда Эйлера в заданном диапазоне
def compute_partial_sum(start, end):
    partial_sum = 0.0
    for k in range(start, end):
        partial_sum += ((-1) ** k) / (2 * k + 1)
    return partial_sum

# Функция для вычисления числа Пи с использованием ряда Эйлера и многопоточности
def compute_pi(num_threads):
    total_sum = 0.0
    threads = []

    # Разбиение диапазона на равные части для каждого потока
    interval = int(math.ceil(math.pi * 1000000 / num_threads))
    for i in range(num_threads):
        start = i * interval
        end = min((i + 1) * interval, int(math.pi * 1000000))
        thread = threading.Thread(target=lambda: compute_partial_sum(start, end))
        threads.append(thread)
        thread.start()

    # Ожидание завершения всех потоков и суммирование результатов
    for thread in threads:
        thread.join()

    for thread in threads:
        total_sum += thread.result

    # Итоговое значение числа Пи
    pi = 4 * total_sum
    return pi

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python pi_calculation.py <количество_потоков>")
        sys.exit(1)

    num_threads = int(sys.argv[1])
    pi = compute_pi(num_threads)
    print("Число Пи:", pi)
