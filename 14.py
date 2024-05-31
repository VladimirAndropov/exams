import psutil
import sys

def list_descendants(pid):
    try:
        parent = psutil.Process(pid)
        children = parent.children(recursive=True)
        for child in children:
            print(f"PID: {child.pid}, Name: {child.name()}")
    except psutil.NoSuchProcess:
        print(f"No such process with PID {pid}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        pid = int(sys.argv[1])
        list_descendants(pid)
    else:
        print("Please provide a PID as argument.")
