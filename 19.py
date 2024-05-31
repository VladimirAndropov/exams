def check_hosts_file():
    with open('/etc/hosts', 'r') as file:
        for line in file:
            if line.strip() and not line.startswith('#') and '127.0.0.1' not in line:
                print(f"Non-localhost entry found: {line.strip()}")

if __name__ == "__main__":
    check_hosts_file()
