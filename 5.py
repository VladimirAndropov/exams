'''5. Напишите программу, которая вычисляет число Пи при помощи ряда Эйлера.
Количество потоков программы должно определяться параметром командной строки.'''

import sys
import threading


def compute_pi(start, end):
    partial_sum = 0.0
    for i in range(start, end):
        partial_sum += (-1) ** i / (2 * i + 1)
    return partial_sum


def main(num_threads):
    num_terms = 1000000  # Количество членов ряда Эйлера
    thread_list = []
    partial_sums = [0.0] * num_threads

    # Функция для запуска вычислений в каждом потоке
    def thread_worker(thread_id):
        start = thread_id * (num_terms // num_threads)
        end = (thread_id + 1) * (num_terms // num_threads)
        partial_sums[thread_id] = compute_pi(start, end)

    # Создание и запуск потоков
    for i in range(num_threads):
        thread = threading.Thread(target=thread_worker, args=(i,))
        thread.start()
        thread_list.append(thread)

    # Ожидание завершения всех потоков
    for thread in thread_list:
        thread.join()

    # Вычисление общей суммы
    total_sum = sum(partial_sums)

    # Вычисление значения числа Пи
    pi_estimate = 4 * total_sum
    print(f"Estimated value of Pi: {pi_estimate}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: 5.py <num_threads>")
        sys.exit(1)

    num_threads = int(sys.argv[1])
    main(num_threads)

'''
juliamekhtieva@MacBook-Pro-73 exam_net_sys % python 5.py 4
Estimated value of Pi: 3.141591653589781
'''