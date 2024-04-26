def check_hosts_file():
    try:
        with open("/etc/hosts", "r") as file:
            for line in file:
                if line.strip() and not line.strip().startswith("#"):
                    parts = line.split()
                    if len(parts) >= 2:
                        ip_address = parts[0]
                        if ip_address != "127.0.0.1":
                            return True
    except FileNotFoundError:
        print("Файл /etc/hosts не найден.")
    return False

if __name__ == "__main__":
    if check_hosts_file():
        print("Обнаружены записи в файле /etc/hosts, отличные от 127.0.0.1.")
    else:
        print("В файле /etc/hosts нет записей, отличных от 127.0.0.1.")
