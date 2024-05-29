import subprocess

def get_ports():
    try:
        process = subprocess.Popen(['netstat', '-tuln'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, _ = process.communicate()
        ports = []

        lines = out.decode().split('\n')
        for line in lines[2:]:
            if line.strip():
                _, port = line.split()[3].split(':')
                ports.append(int(port))

        return ports
    except FileNotFoundError:
        print("Error: 'netstat' command not found.")
        return []

if __name__ == "__main__":
    ports = get_ports()
    if ports:
        print("Open ports:")
        for port in ports:
            print(port)
    else:
        print("No open ports found.")
