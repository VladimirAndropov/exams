import psutil
import sys

def print_process_descendants(pid):
    try:
        parent_process = psutil.Process(pid)
    except psutil.NoSuchProcess:
        print("Процесс с PID", pid, "не найден.")
        return

    descendants = parent_process.children(recursive=True)
    if descendants:
        print("Потомки процесса с PID", pid, ":")
        for descendant in descendants:
            print("PID:", descendant.pid, "| Имя:", descendant.name())
    else:
        print("У процесса с PID", pid, "нет потомков.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python script.py <PID>")
        sys.exit(1)

    try:
        pid = int(sys.argv[1])
    except ValueError:
        print("PID должен быть целым числом.")
        sys.exit(1)

    print_process_descendants(pid)
