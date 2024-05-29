import sys

def find_divisible_by_12(start, end):
    try:
        start = int(start)
        end = int(end)
        if start > end:
            print("Error: Start value should be less than end value.")
            return

        print("Numbers divisible by 12 in range {} to {}:".format(start, end))
        for num in range(start, end + 1):
            if num % 12 == 0:
                print(num)
    except ValueError:
        print("Error: Invalid input. Please enter integer values for start and end.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <start> <end>")
    else:
        start = sys.argv[1]
        end = sys.argv[2]
        find_divisible_by_12(start, end)
