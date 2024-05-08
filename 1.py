import threading

# Функция, которую будет выполнять нить
def print_ten_lines():
    for i in range(10):
        print("This is line", i+1)

# Создание новой нити
thread1 = threading.Thread(target=print_ten_lines)

# Создание главной нити
main_thread = threading.Thread(target=print_ten_lines)

# Запуск нитей
thread1.start()
main_thread.start()

# Ждем завершения нитей
thread1.join()
main_thread.join()
