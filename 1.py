import threading

# Функция, которую будет выполнять нить
def print_ten_lines():
    for i in range(10):
        print("This is line", i+1)

# Создание новой нити
thread = threading.Thread(target=print_ten_lines)

# Запуск нити
thread.start()

# Главная нить также будет печатать десять строк текста
for i in range(10):
    print("This is line", i+1)