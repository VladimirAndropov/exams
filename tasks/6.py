import multiprocessing

# Функция, выполняющая вычисления
def calculate(x, y):
    return x ** y

# Функция, распределяющая задачи между процессами
def worker(task_segment, result_list):
    for idx, x in task_segment:
        result_list[idx] = calculate(x, 2)

if __name__ == "__main__":
    # Создание пула процессов с 5 воркерами
    with multiprocessing.Pool(5) as pool:
        # Список значений x от 0 до 1 с шагом 0.1
        x_values = [i * 0.1 for i in range(11)]
        results = [None] * len(x_values)

        # Определение размера каждого сегмента для процесса
        segment_size = len(x_values) // 5
        tasks = []

        for i in range(0, len(x_values), segment_size):
            end = min(i + segment_size, len(x_values))
            segment = list(enumerate(x_values[i:end], start=i))
            tasks.append((segment, results))

        # Асинхронное выполнение задач
        for task in tasks:
            pool.apply_async(worker, task)

        # Закрытие пула и ожидание завершения всех задач
        pool.close()
        pool.join()

    # Вывод результатов вычислений
    for x, result in zip(x_values, results):
        print(f"calculate({x}, 2) = {result}")
