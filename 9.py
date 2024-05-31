import subprocess

def list_open_ports():
    result = subprocess.run(['netstat', '-tuln'], stdout=subprocess.PIPE)
    print(result.stdout.decode('utf-8'))

if __name__ == "__main__":
    list_open_ports()
