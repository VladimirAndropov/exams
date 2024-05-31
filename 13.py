import sys
import cmath

def find_roots(a, b, c):
    d = cmath.sqrt(b**2 - 4*a*c)
    root1 = (-b + d) / (2*a)
    root2 = (-b - d) / (2*a)
    return root1, root2

if __name__ == "__main__":
    if len(sys.argv) == 4:
        a, b, c = map(float, sys.argv[1:4])
        root1, root2 = find_roots(a, b, c)
        print(f"Roots: {root1}, {root2}")
    else:
        print("Please provide coefficients A, B, and C as arguments.")
