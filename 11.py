import sys

def find_divisible_by_12(start, end):
    try:
        start = int(start)
        end = int(end)
        for num in range(start, end + 1):
            if num % 12 == 0:
                print(num)
    except ValueError:
        print("Invalid input. Please enter integer values.")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        find_divisible_by_12(sys.argv[1], sys.argv[2])
    else:
        print("Please provide a start and end number as arguments.")
