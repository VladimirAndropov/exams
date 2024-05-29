import random
import datetime

def generate_lottery_numbers():
    # Генерируем 5 случайных неповторяющихся чисел
    numbers = random.sample(range(1, 51), 5)
    return numbers

def main():
    # Генерируем номера лотереи
    lottery_numbers = generate_lottery_numbers()

    # Получаем текущую дату и время
    current_datetime = datetime.datetime.now()

    # Выводим на стандартный вывод
    print("Сгенерированные лотерейные номера:")
    for number in lottery_numbers:
        print(number)

    # Записываем в файл
    file_name = "lottery_numbers.txt"
    with open(file_name, "a") as file:
        file.write("Дата и время генерации: {}\n".format(current_datetime))
        file.write("Сгенерированные лотерейные номера:\n")
        for number in lottery_numbers:
            file.write(str(number) + "\n")

if __name__ == "__main__":
    main()
