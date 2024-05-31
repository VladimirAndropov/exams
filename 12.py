import random
import datetime
import sys
import argparse

def generate_lottery_numbers(quantity=5, min_number=1, max_number=50):
    numbers = random.sample(range(min_number, max_number + 1), quantity)
    date_time = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    result = f"{date_time} -> {numbers}"
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate lottery numbers.')
    parser.add_argument('-f', '--file', metavar='filename', help='File to append results to')
    parser.add_argument('-q', '--quantity', type=int, default=5, help='Quantity of lottery numbers to generate (default: 5)')
    parser.add_argument('--min', type=int, default=1, help='Minimum number in the range (default: 1)')
    parser.add_argument('--max', type=int, default=50, help='Maximum number in the range (default: 50)')
    args = parser.parse_args()

    result = generate_lottery_numbers(args.quantity, args.min, args.max)

    if args.file:
        try:
            with open(args.file, 'a') as file:
                file.write(result + '\n')
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found.", file=sys.stderr)
            sys.exit(1)
        except PermissionError:
            print(f"Error: Permission denied for file '{args.file}'.", file=sys.stderr)
            sys.exit(1)
    else:
        print(result)
