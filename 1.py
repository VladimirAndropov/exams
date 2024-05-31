import concurrent.futures

# Функция, которую будет выполнять нить
def print_ten_lines():
    for i in range(10):
        print("This is line", i+1)

# Создание пула нитей
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Запуск первой нити
    executor.submit(print_ten_lines)
    
    # Главная нить также будет печатать десять строк текста
    for i in range(10):
        print("This is line", i+1)
