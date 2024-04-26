# Напишите сценарий, который находил бы корни "квадратного " уравнения, вида: Ax^2 + Bx + C = 0.
# Сценарий должен получать коэффициенты уравнения A, B и C, как аргументы командной строки, и выводить корни.
# Если корней нет, вывод должен быть пустым.
from sympy import solve

def quadratic(a, b, c):
	try:
		assert a != 0
		x = solve("x", a * x**2 + b * x + c)
		return x
	except AssertionError:
		return "Первый коэффициент не должен быть равен нулю"
	except UnboundLocalError:
		return "Нет действительных корней"

if __name__ == "__main__":
	a = float(input())
	b = float(input())
	c = float(input())
	print(quadratic(a, b, c))