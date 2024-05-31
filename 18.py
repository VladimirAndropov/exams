import subprocess
import sys

def install_programs(programs):
    for program in programs:
        subprocess.run(['sudo', 'apt-get', 'install', '-y', program])

if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            programs = file.read().splitlines()
            install_programs(programs)
    elif len(sys.argv) > 1:
        install_programs(sys.argv[1:])
    else:
        print("Please provide a list of programs as arguments or a text file containing the list of programs.")
