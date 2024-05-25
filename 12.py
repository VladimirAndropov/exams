import random
import datetime

def generate_lottery_numbers():
    numbers = random.sample(range(1, 51), 5)
    return sorted(numbers)

lottery_numbers = generate_lottery_numbers()

current_datetime = datetime.datetime.now()

print("Сгенерированные лотерейные числа:", lottery_numbers)
print("Дата и время генерации:", current_datetime)

with open("lottery_numbers.txt", "a") as file:
    file.write("Сгенерированные лотерейные числа: {}\n".format(lottery_numbers))
    file.write("Дата и время генерации: {}\n\n".format(current_datetime))