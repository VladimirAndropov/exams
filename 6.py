import multiprocessing
import math

# Основная вычислительная функция
def power_function(base, exponent):
    return base ** exponent

# Функция, выполняющая задачи для каждого процесса
def execute_tasks(task_range, result_array):
    for index, value in task_range:
        result_array[index] = power_function(value, 2)

if __name__ == "__main__":
    # Создаем пул процессов с 5 рабочими процессами
    process_count = 5
    with multiprocessing.Pool(process_count) as pool:
        # Генерация списка значений от 0 до 1 с шагом 0.1
        values = [i * 0.1 for i in range(11)]
        results = multiprocessing.Manager().list([None] * len(values))

        # Определение размера сегмента для задач каждого процесса
        segment_length = math.ceil(len(values) / process_count)
        tasks = []

        for i in range(0, len(values), segment_length):
            end_index = min(i + segment_length, len(values))
            task_segment = list(enumerate(values[i:end_index], start=i))
            tasks.append((task_segment, results))

        # Асинхронное распределение задач между процессами
        async_results = [pool.apply_async(execute_tasks, task) for task in tasks]

        # Ожидание завершения всех задач
        for async_result in async_results:
            async_result.wait()

    # Вывод результатов
    for value, result in zip(values, results):
        print(f"power_function({value}, 2) = {result}")
