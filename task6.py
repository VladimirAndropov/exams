import multiprocessing

# Функция calculate
def calculate(x, y):
    return x * y

if __name__ == "__main__":
    # Создание пула процессов
    pool = multiprocessing.Pool(processes=5)

    # Генерация значений x от 0 до 1 с шагом 0.1
    x_values = [i * 0.1 for i in range(11)]

    # Установка y как 2
    y_value = 2

    # Вычисление функции для каждого значения x в пуле процессов
    results = []
    for x in x_values:
        result = pool.apply_async(calculate, (x, y_value))
        results.append(result)

    # Получение результатов из пула и вывод на экран
    for result in results:
        print("Результат:", result.get())

    # Закрытие пула процессов
    pool.close()
    pool.join()
