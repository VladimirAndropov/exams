import threading
import sys


def calculate_pi_segment(start, end, result, index):
    pi_segment = sum(1.0 / k ** 2 for k in range(start, end))
    result[index] = pi_segment


def main(threads_count):
    n = 1000000  # Number of terms in the series
    segment_size = n // threads_count
    threads = []
    result = [0] * threads_count

    for i in range(threads_count):
        start = i * segment_size + 1
        end = (i + 1) * segment_size + 1
        thread = threading.Thread(target=calculate_pi_segment, args=(start, end, result, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    pi_approx = (sum(result) * 6) ** 0.5
    print(f"Approximated value of Pi: {pi_approx}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        threads_count = int(sys.argv[1])
        main(threads_count)
    else:
        print("Please provide the number of threads as argument.")
