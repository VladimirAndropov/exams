import psutil
import sys

def get_children_pids(parent_pid):
    children = []
    parent = psutil.Process(parent_pid)
    for child in parent.children(recursive=True):
        children.append(child.pid)
    return children

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Ошибка: Необходимо указать PID процесса", file=sys.stderr)
        sys.exit(1)

    parent_pid = int(sys.argv[1])
    try:
        parent = psutil.Process(parent_pid)
    except psutil.NoSuchProcess:
        print("Ошибка: Процесс с PID {} не найден".format(parent_pid), file=sys.stderr)
        sys.exit(1)

    children_pids = get_children_pids(parent_pid)
    if not children_pids:
        print("Процесс с PID {} не имеет потомков.".format(parent_pid))
    else:
        print("Потомки процесса {} с PID {}:".format(parent.name(), parent_pid))
        for pid in children_pids:
            try:
                child_process = psutil.Process(pid)
                print("{} {}".format(pid, child_process.name()))
            except psutil.NoSuchProcess:
                print("Ошибка: Потомок с PID {} не найден".format(pid), file=sys.stderr)
