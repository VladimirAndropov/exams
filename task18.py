import subprocess
import sys

def install_programs(programs):
    for program in programs:
        try:
            subprocess.run(["pip", "install", program], check=True)
            print(f"Программа '{program}' успешно установлена.")
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при установке программы '{program}':", e)

def read_programs_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            programs = [line.strip() for line in file.readlines() if line.strip()]
        return programs
    except FileNotFoundError:
        print("Файл не найден.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        programs = read_programs_from_file(sys.argv[1])
    elif len(sys.argv) > 2:
        programs = sys.argv[1:]
    else:
        print("Использование: python script.py <программа1> <программа2> ... или")
        print("python script.py <путь_к_файлу>")
        sys.exit(1)

    install_programs(programs)
