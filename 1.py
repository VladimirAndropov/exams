'''1. Напишите программу, которая создает нить. Родительская и вновь созданная нити должны распечатать десять строк текста.'''

import threading

# Создание блокировки
print_lock = threading.Lock()

# Функция, которую будет выполнять нить
def print_ten_lines(thread_name):
    for i in range(10):
        with print_lock:  # Захват блокировки
            print(f"{thread_name}: This is line {i+1}")

# Создание новой нити
new_thread = threading.Thread(target=print_ten_lines, args=("New Thread",))

# Запуск нити
new_thread.start()

# Главная нить также будет печатать десять строк текста
print_ten_lines("Main Thread")

# Ожидание завершения новой нити
new_thread.join()
