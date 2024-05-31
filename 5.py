import sys
import threading
import math

# Функция для вычисления части ряда Эйлера в заданном диапазоне
def calculate_partial_sum(start, end, result):
    partial_sum = 0
    for k in range(start, end):
        partial_sum += ((-1) ** k) / (2 * k + 1)
    result.append(partial_sum)

# Функция для вычисления числа π с использованием многопоточности
def calculate_pi(num_threads):
    chunk_size = int(math.ceil(1000000 / num_threads))
    threads = []
    partial_sums = []

    for i in range(num_threads):
        start = i * chunk_size
        end = min((i + 1) * chunk_size, 1000000)
        partial_sums.append(0)
        thread = threading.Thread(target=calculate_partial_sum, args=(start, end, partial_sums))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    pi = sum(partial_sums) * 4

    return pi

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python euler_series.py <num_threads>")
        sys.exit(1)

    num_threads = int(sys.argv[1])

    pi = calculate_pi(num_threads)
    print("Estimated value of pi:", pi)
