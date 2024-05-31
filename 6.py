import multiprocessing

# Функция для вычисления значения функции calculate(x, y)
def calculate(x, y):
    return x ** y

if __name__ == "__main__":
    # Создание пула из 5 процессов
    pool = multiprocessing.Pool(processes=5)

    # Создание списка значений x от 0 до 1 с шагом 0.1
    x_values = [i * 0.1 for i in range(11)]

    # Распределение вычислений между процессами
    results = pool.starmap(calculate, [(x, 2) for x in x_values])

    # Закрытие пула процессов
    pool.close()
    pool.join()

    # Вывод результатов вычислений
    for x, result in zip(x_values, results):
        print(f"calculate({x}, 2) = {result}")
