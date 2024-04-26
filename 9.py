# Эта программа использует модуль subprocess для выполнения команды netstat -tuln, которая выводит список открытых портов на машине. Затем программа обрабатывает вывод команды, извлекая номера портов, и выводит их на экран.
import subprocess

def get_open_ports():
    try:
        # Запуск команды netstat для получения списка открытых портов
        result = subprocess.run(['netstat', '-tuln'], capture_output=True, text=True)
        output_lines = result.stdout.split('\n')
        open_ports = []

        # Обработка вывода команды netstat
        for line in output_lines[2:]:  # Пропускаем первые две строки, содержащие заголовки
            if line.strip():  # Пропускаем пустые строки
                parts = line.split()
                if len(parts) >= 4:
                    address, port = parts[3].split(':')
                    open_ports.append(int(port))

        return open_ports
    except FileNotFoundError:
        print("Error: 'netstat' command not found.")
        return []

if __name__ == "__main__":
    open_ports = get_open_ports()
    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(port)
    else:
        print("No open ports found.")