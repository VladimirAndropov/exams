'''
10. Напишите программу, которая копирует файл с удаленного хоста в текущую папку по SSH. Имя файла и адрес хоста принимать как параметры.
'''

import sys
import paramiko

def copy_file_via_ssh(remote_host, username, password, remote_file):
    """
    Копирует файл с удаленного хоста по SSH.
    """
    try:
        # Установка SSH-соединения
        with paramiko.SSHClient() as ssh_client:
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(remote_host, username=username, password=password)

            # Копирование файла с удаленного хоста в текущую папку
            with ssh_client.open_sftp() as sftp_client:
                sftp_client.get(remote_file, remote_file.split("/")[-1])

            print(f"File '{remote_file}' copied successfully.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python 10.py <remote_host> <username> <password> <remote_file>")
        sys.exit(1)

    remote_host, username, password, remote_file = sys.argv[1:]

    copy_file_via_ssh(remote_host, username, password, remote_file)
