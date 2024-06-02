'''7. Напишите программу, которая проверяет все числа от 0 на простоту и выводит простые числа на экран по мере нахождения.
Числа должны проверяться в различных потоках (или процессах, по выбору студента).
Программа должна работать до тех пор, пока ее не остановит пользователь.'''

import threading
import time

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n ** 0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

class PrimeChecker(threading.Thread):
    def __init__(self):
        super().__init__()
        self.exit_event = threading.Event()

    def run(self):
        num = 0
        while not self.exit_event.is_set():
            if is_prime(num):
                print(num)
                time.sleep(0.3)
            num += 1

if __name__ == "__main__":
    prime_thread = PrimeChecker()
    prime_thread.start()

    print("Press Enter to stop...")
    input()

    prime_thread.exit_event.set()
    prime_thread.join()
