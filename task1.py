# Напишите программу, которая создает нить.
# Родительская и вновь созданная нити должны распечатать десять строк текста.

import threading


def new_thread_func():
    for i in range(10):
        print("New Thread: " + str(i))


if __name__ == "__main__":
    new_thread = threading.Thread(target=new_thread_func)
    new_thread.start()

    for i in range(10):
        print("Main Thread: " + str(i))
