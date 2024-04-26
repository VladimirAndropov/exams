import threading

# Функция, которую будет выполнять нить
def print_lines():
    for i in range(10):
        print("Это строка номер", i+1)

# Создание новой нити
new_thread = threading.Thread(target=print_lines)

# Запуск нити
new_thread.start()

# Теперь родительская нить также печатает десять строк текста
for i in range(10):
    print("Это строка номер", i+1)
