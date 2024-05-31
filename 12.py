import random
import datetime
import sys

def generate_lottery_numbers():
    numbers = random.sample(range(1, 51), 5)
    date_time = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    result = f"{date_time} -> {numbers}"
    return result

if __name__ == "__main__":
    result = generate_lottery_numbers()

    if len(sys.argv) == 2 and sys.argv[1] == "-f":
        if len(sys.argv) < 3:
            print("Ошибка: При использовании флага -f необходимо передать название файла!", file=sys.stderr)
            sys.exit(1)
        
        filename = sys.argv[2]
        with open(filename, 'a') as file:
            file.write(result + '\n')
    else:
        print(result)
