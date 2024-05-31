import threading
import time
import msvcrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_primes():
    num = 0
    while True:
        if is_prime(num):
            print(num)
        num += 1
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'q':
                break

# Замеряем время начала выполнения программы
start_time = time.time()

# Создаем и запускаем поток для проверки простых чисел
thread = threading.Thread(target=check_primes)
thread.start()

# Ожидаем завершения потока
thread.join()

# Замеряем время окончания выполнения программы и выводим время выполнения
end_time = time.time()
execution_time = end_time - start_time
print("Время выполнения программы:", execution_time, "секунд")

# Ожидаем завершения потока
thread.join()

