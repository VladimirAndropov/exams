import argparse
import subprocess
import os

def install_package(package_name):
    try:
        subprocess.check_call(["sudo", "apt-get", "install", "-y", package_name])
        print(f"Установлен пакет: {package_name}")
    except subprocess.CalledProcessError:
        print(f"Ошибка установки пакета: {package_name}")

def read_packages_from_file(file_path):
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

parser = argparse.ArgumentParser(description="Устанавливает пакеты в текущую систему")

subparsers = parser.add_subparsers(dest="command")

install_parser = subparsers.add_parser("install", help="Устанавливает пакеты из аргументов или файла")
install_parser.add_argument("packages", type=str, nargs="+", help="Список пакетов для установки")
install_parser.add_argument("-f", "--file", help="Укажите путь к файлу с пакетами для установки")

args = parser.parse_args()

if args.command == "install":
    packages_to_install = args.packages
    if args.file:
        packages_to_install += read_packages_from_file(args.file)

    for package in packages_to_install:
        install_package(package)