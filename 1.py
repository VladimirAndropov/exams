import threading

# Функция, которую будет выполнять нить
def print_ten_lines(source):
    for i in range(10):
        print(f"{source}: This is line {i+1}")

# Создание новой нити
thread1 = threading.Thread(target=print_ten_lines, args=("Thread 1",))
thread2 = threading.Thread(target=print_ten_lines, args=("Thread 2",))

# Запуск нитей
thread1.start()
thread2.start()

# Ожидание завершения нитей
thread1.join()
thread2.join()

print("All threads completed")
