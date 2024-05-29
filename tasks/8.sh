if [ $# -ne 2 ]; then
    echo "Usage: $0 <directory> <size>"
    exit 1
fi

if [ ! -d "$1" ]; then
    echo "Error: '$1' is not a directory."
    exit 1
fi

directory=$(realpath "$1")

size=$2

find "$directory" -type f -size "${size}c" | while IFS= read -r file; do
    echo "$file"
done