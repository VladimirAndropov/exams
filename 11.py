#Задача 11. Сценарий должен вывести (на stdout) все числа, делящиеся на 12,
# в диапазоне от первого параметра до последнего.
# Если параметры заданы некорректно, скрипт должен вывести сообщение.
import sys
if len(sys.argv) != 3:
    print("Введено неверное кол-во аргументов")
    sys.exit(1)
try:
    start_num = int(sys.argv[1])
    end_num = int(sys.argv[2])
except ValueError:
    print("Аргументы должны быть целыми")
    sys.exit(1)

if start_num > end_num:
    print("Ошибка: начальное число больше, чем финальное")
    sys.exit(1)

for num in range(start_num, end_num + 1):
    if num % 12 == 0:
        print(num)