import threading

# Определяем функцию для выполнения в отдельной нити
def print_from_thread():
    output = [f"Secondary thread output {i + 1}" for i in range(10)]
    print('\n'.join(output))

# Создаем объект нити
secondary_thread = threading.Thread(target=print_from_thread)

# Запускаем созданную нить
secondary_thread.start()

# Основной поток также выводит десять строк
main_output = [f"Primary thread output {i + 1}" for i in range(10)]
print('\n'.join(main_output))

# Ждем завершения вторичной нити
secondary_thread.join()
