import threading

def print_ten_lines():
    for _ in range(10):
        print("Hello from thread")

thread = threading.Thread(target=print_ten_lines)
thread.start()

for _ in range(10):
    print("Hello from parent thread")

thread.join()
