import os

def read_hosts_file():
    with open("/etc/hosts", "r") as hosts_file:
        return hosts_file.readlines()

def is_ip_address(ip):
    return all(c.isdigit() or c == "." for c in ip)

def is_not_localhost(ip, line):
    return is_ip_address(ip) and ip != "127.0.0.1" and ip.strip() in line

def main():
    hosts_lines = read_hosts_file()

    non_localhost_ips = [ip.strip().split()[0] for ip, line in enumerate(hosts_lines) if is_not_localhost(ip, line)]

    if non_localhost_ips:
        print("Найдены записи в /etc/hosts, относящиеся к адресам отличным от 127.0.0.1:")
        for ip in non_localhost_ips:
            print(ip)
    else:
        print("В файле /etc/hosts не обнаружено записей, относящихся к адресам отличным от 127.0.0.1.")

if __name__ == "__main__":
    main()