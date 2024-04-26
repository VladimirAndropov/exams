# Этот скрипт принимает PID в качестве аргумента командной строки и выводит всех его потомков, если они существуют. Для этого используется функция get_children_recursive, которая рекурсивно получает всех потомков процесса.

import psutil
import os
import sys

def get_children_recursive(pid):
    children = []
    try:
        parent = psutil.Process(pid)
        children = parent.children(recursive=True)
    except psutil.NoSuchProcess:
        pass
    return children

def main():
    if len(sys.argv) != 2:
        print("Usage: python process_tree.py <PID>")
        return

    try:
        pid = int(sys.argv[1])
    except ValueError:
        print("Error: PID must be an integer.")
        return

    print("Process Tree for PID", pid)
    print("----------------------------------")

    # Получаем список всех потомков процесса
    children = get_children_recursive(pid)

    if children:
        for child in children:
            print("PID:", child.pid, "| Name:", child.name())
    else:
        print("No children processes found.")

if __name__ == "__main__":
    main()
