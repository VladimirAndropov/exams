import multiprocessing
from functools import partial

# Функция для вычисления значения функции calculate(x, y)
def calculate(x, y):
    return x ** y

if __name__ == "__main__":
    # Создание пула из 5 процессов с помощью менеджера контекста
    with multiprocessing.Pool(processes=5) as pool:
        # Создание списка значений x от 0 до 1 с шагом 0.1
        x_values = [i * 0.1 for i in range(11)]

        # Распределение вычислений между процессами с помощью map
        chunk_size = len(x_values) // 5
        results = pool.map(partial(calculate, y=2), x_values)

        # Вывод результатов вычислений
        for x, result in zip(x_values, results):
            print(f"calculate({x}, 2) = {result}")
