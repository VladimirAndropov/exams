import multiprocessing

def calculate(x, y):
    return x * y  # Placeholder function

def worker(x, y):
    result = calculate(x, y)
    print(f"calculate({x}, {y}) = {result}")

def main():
    with multiprocessing.Pool(5) as pool:
        args = [(x/10, 2) for x in range(11)]
        pool.starmap(worker, args)

if __name__ == "__main__":
    main()
