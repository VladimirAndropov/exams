import sys
import math

def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root,
    else:
        return ()

def main():
    if len(sys.argv) != 4:
        print("Usage: python quadratic_solver.py A B C")
        return

    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])

        roots = solve_quadratic_equation(a, b, c)

        if roots:
            print("Корни уравнения:")
            for root in roots:
                print(root)
        else:
            print("Уравнение не имеет корней.")
    except ValueError:
        print("Ошибка: неверный формат входных данных.")

if __name__ == "__main__":
    main()