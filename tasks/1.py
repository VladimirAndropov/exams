import threading

# Определяем функцию для выполнения в отдельной нити
def thread_task():
    for j in range(10):
        print(f"Thread line {j + 1}")

# Создаем объект нити
new_thread = threading.Thread(target=thread_task)

# Запускаем созданную нить
new_thread.start()

# Основной поток также выводит десять строк
for j in range(10):
    print(f"Main line {j + 1}")
