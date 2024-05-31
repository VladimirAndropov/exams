import threading
import time
import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_prime(n):
    if is_prime(n):
        print(f"{n} is prime")

def main():
    n = 0
    while True:
        thread = threading.Thread(target=check_prime, args=(n,))
        thread.start()
        n += 1
        time.sleep(0.01)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Stopped by user")
