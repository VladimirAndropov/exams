import os, sys


def search_files(target, size):
    for r, d, f in os.walk(target):
        for fi in f:
            fp = os.path.join(r, fi)
            try:
                fs = os.path.getsize(fp)
                if fs == size:
                    print(fp)
            except OSError:
                pass


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python search.py <dir> <size>")
        sys.exit(1)

    target = sys.argv[1]
    size = int(sys.argv[2])

    if not os.path.isdir(target):
        print("Error: Specified directory does not exist.")
        sys.exit(1)

    search_files(target, size)
