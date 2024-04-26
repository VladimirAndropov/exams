import sys

def print_numbers_divisible_by_12(start, end):
    try:
        start = int(start)
        end = int(end)
        if start > end:
            print("Ошибка: Первый параметр должен быть меньше второго.")
            return
        print("Числа, делящиеся на 12 в диапазоне от", start, "до", end, ":")
        for num in range(start, end + 1):
            if num % 12 == 0:
                print(num)
    except ValueError:
        print("Ошибка: Параметры должны быть целыми числами.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python script.py <начало_диапазона> <конец_диапазона>")
        sys.exit(1)

    start = sys.argv[1]
    end = sys.argv[2]

    print_numbers_divisible_by_12(start, end)
