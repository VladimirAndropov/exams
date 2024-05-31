import multiprocessing
import time
import sys

# Функция для поиска всех чисел, кратных 12, в указанном диапазоне
def find_divisible_by_12(start, end, results):
    start = start + (12 - (start % 12))  # Находим первое число, кратное 12, в диапазоне
    for num in range(start, end, 12):  # Итерируем через каждое 12-е число в диапазоне
        results.put(num)

if __name__ == "__main__":
    # Проверка корректности введенных параметров
    if len(sys.argv) != 3:
        print("Usage: python script.py <start_number> <end_number>")
        sys.exit(1)

    try:
        start_num = int(sys.argv[1])
        end_num = int(sys.argv[2])
    except ValueError:
        print("Параметры должны быть целыми числами.")
        sys.exit(1)

    if start_num >= end_num:
        print("Начальное число должно быть меньше конечного числа.")
        sys.exit(1)

    # Замеряем время начала выполнения программы
    start_time = time.time()

    # Создание очереди для результатов
    results = multiprocessing.Queue()

    # Создание и запуск процесса для поиска чисел, кратных 12
    process = multiprocessing.Process(target=find_divisible_by_12, args=(start_num, end_num + 1, results))
    process.start()

    try:
        # Ожидание и вывод результатов
        while True:
            if not results.empty():
                divisible_number = results.get()
                print("Число, которое делится на 12:", divisible_number)
            time.sleep(0.1)  # Задержка для уменьшения нагрузки на процессор
    except KeyboardInterrupt:
        # Прерывание программы по нажатию Ctrl+C
        print("Программа остановлена пользователем.")
        process.terminate()

    # Замеряем время окончания выполнения программы и выводим время выполнения
    end_time = time.time()
    execution_time = end_time - start_time
    print("Время выполнения программы:", execution_time, "секунд")
