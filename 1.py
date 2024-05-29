import threading

def print_ten_lines():
    for i in range(10):
        print("This is line", i+1)

thread = threading.Thread(target=print_ten_lines)

thread.start()

for i in range(10):
    print("This is line", i+1)