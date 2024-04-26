# Дана функция calculate(x, y).
# Напишите программу, которая создает пул из 5 процессов и распределяет в этом пуле
# вычисление функции на промежутке х от 0 до 1 с шагом 0,1. у равняется 2 всегда.

import multiprocessing


def calculate(x, y):
    return x**y


# Функция для распределения вычислений между процессами
def worker(x_values, results, start, end):
    for i in range(start, end):
        x = x_values[i]
        result = calculate(x, 2)
        results[i] = result


if __name__ == "__main__":
    # Создание пула из 5 процессов
    pool = multiprocessing.Pool(processes=5)

    # Создание списка значений x от 0 до 1 с шагом 0.1
    x_values = [i * 0.1 for i in range(11)]
    results = [None] * len(x_values)

    # Распределение вычислений между процессами
    chunk_size = len(x_values) // 5
    start = 0
    end = chunk_size
    for _ in range(5):
        pool.apply_async(worker, args=(x_values, results, start, end))
        start = end
        end = min(end + chunk_size, len(x_values))

    # Закрытие пула процессов и ожидание завершения всех процессов
    pool.close()
    pool.join()

    # Вывод результатов вычислений
    for x, result in zip(x_values, results):
        print(f"calculate({x}, 2) = {result}")
