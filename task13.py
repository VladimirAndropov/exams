import sys
import math

def solve_quadratic_equation(A, B, C):
    # Вычисление дискриминанта
    discriminant = B**2 - 4*A*C

    # Проверка наличия корней
    if discriminant < 0:
        return []
    elif discriminant == 0:
        x = -B / (2*A)
        return [x]
    else:
        x1 = (-B + math.sqrt(discriminant)) / (2*A)
        x2 = (-B - math.sqrt(discriminant)) / (2*A)
        return [x1, x2]

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Использование: python script.py <A> <B> <C>")
        sys.exit(1)

    try:
        A = float(sys.argv[1])
        B = float(sys.argv[2])
        C = float(sys.argv[3])
    except ValueError:
        print("Коэффициенты должны быть числами.")
        sys.exit(1)

    roots = solve_quadratic_equation(A, B, C)
    if roots:
        print("Корни уравнения:", roots)
    else:
        print("У уравнения нет корней.")
