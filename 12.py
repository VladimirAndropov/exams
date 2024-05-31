import random
import datetime


def generate_lotto_numbers():
    numbers = random.sample(range(1, 51), 5)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result = f"{timestamp}: {numbers}"

    print(result)

    with open("lotto_numbers.txt", "a") as file:
        file.write(result + "\n")


if __name__ == "__main__":
    generate_lotto_numbers()
