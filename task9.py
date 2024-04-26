import subprocess

def get_open_ports():
    try:
        # Выполнение команды netstat для получения списка открытых портов
        result = subprocess.run(["netstat", "-an"], capture_output=True, text=True, check=True)
        netstat_output = result.stdout

        # Парсинг вывода команды netstat для получения открытых портов
        open_ports = set()
        for line in netstat_output.splitlines():
            if "LISTEN" in line:
                parts = line.split()
                if len(parts) >= 4:
                    port = parts[3].split(":")[-1]
                    if port.isdigit():
                        open_ports.add(int(port))

        return sorted(open_ports)
    except subprocess.CalledProcessError as e:
        print("Ошибка при выполнении команды netstat:", e)
        return []

if __name__ == "__main__":
    open_ports = get_open_ports()
    if open_ports:
        print("Открытые порты:", open_ports)
    else:
        print("На данной машине нет открытых портов.")
