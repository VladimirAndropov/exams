# Напишите программу, которая создает нить. Родительская и вновь созданная нити должны распечатать десять строк текста.

import threading

def print_lines():
    for i in range(10):
        print(f"Дочерний поток {i+1}")

thread = threading.Thread(target=print_lines)
thread.start()

for i in range(10):
    print(f"Главный поток {i+1}")

thread.join()
