# Сценарий должен имитировать работу лототрона -- извлекать 5 случайных неповторяющихся чисел в диапазоне 1 - 50. Сценарий должен предусматривать как вывод на stdout, так и запись чисел в файл, кроме того, вместе с числами должны выводиться дата и время генерации данного набора.

import random
import datetime

def generate_lottery_numbers():
    # Генерируем 5 случайных неповторяющихся чисел в диапазоне 1 - 50
    numbers = random.sample(range(1, 51), 5)
    return sorted(numbers)

def main():
    # Генерируем номера
    lottery_numbers = generate_lottery_numbers()

    # Получаем текущую дату и время
    current_datetime = datetime.datetime.now()

    # Выводим на stdout
    print("Сгенерированные лотерейные числа:", lottery_numbers)
    print("Дата и время генерации:", current_datetime)

    # Записываем числа в файл
    with open("lottery_numbers.txt", "a") as file:
        file.write("Сгенерированные лотерейные числа: {}\n".format(lottery_numbers))
        file.write("Дата и время генерации: {}\n\n".format(current_datetime))

if __name__ == "__main__":
    main()