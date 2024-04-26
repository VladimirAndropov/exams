import random
import datetime

def generate_lottery_numbers():
    # Генерация 5 случайных неповторяющихся чисел
    numbers = random.sample(range(1, 51), 5)
    return numbers

def print_and_write_to_file(numbers):
    # Вывод чисел на stdout
    print("Сгенерированные числа:", numbers)

    # Запись чисел в файл
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    filename = "lottery_numbers_" + now.strftime("%Y%m%d_%H%M%S") + ".txt"
    with open(filename, "w") as file:
        file.write("Дата и время генерации: {}\n".format(timestamp))
        file.write("Сгенерированные числа:\n")
        for number in numbers:
            file.write(str(number) + "\n")

if __name__ == "__main__":
    # Генерация чисел лототрона
    numbers = generate_lottery_numbers()

    # Вывод чисел на stdout и запись в файл
    print_and_write_to_file(numbers)
