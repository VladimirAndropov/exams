import sys
import math

def find_roots(a, b, c):
    roots = []
    discriminant = b**2 - 4*a*c

    if a == 0:
        print("Ошибка: Коэффициент a не может быть равен нулю.", file=sys.stderr)
        sys.exit(1)

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        roots.extend([root1, root2])
    elif discriminant == 0:
        root = -b / (2*a)
        roots.append(root)

    return roots

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Ошибка: Неверное количество параметров.", file=sys.stderr)
        print("Использование: python script.py <a> <b> <c>", file=sys.stderr)
        sys.exit(1)

    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
    except ValueError:
        print("Ошибка: Один из коэффициентов не является числом.", file=sys.stderr)
        sys.exit(1)

    roots = find_roots(a, b, c)

    print("Корни уравнения:")
    if roots:
        for root in roots:
            print(root)
    else:
        print("Уравнение не имеет действительных корней.")
