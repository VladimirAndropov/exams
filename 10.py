# используя scp
# scp 127.0.0.1/windows 1.0.0.0/vasya


# второй вариант на питоне

# В этом коде мы подключаемся к удаленному хосту по SSH, используя библиотеку Paramiko, и копируем файл с удаленного хоста в текущую папку
import sys
import paramiko

def scp_copy_file(remote_host, remote_file):
    try:
        # Установка SSH-соединения
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(remote_host)

        # Копирование файла с удаленного хоста
        sftp_client = ssh_client.open_sftp()
        sftp_client.get(remote_file, remote_file.split('/')[-1])  # Копирование файла в текущую папку
        sftp_client.close()

        print("File copied successfully.")
    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your credentials.")
    except paramiko.SSHException as e:
        print("SSH error:", e)
    except FileNotFoundError:
        print("File not found on remote host.")
    finally:
        ssh_client.close()

if __name__ == "__main__":
    # Проверка количества аргументов командной строки
    if len(sys.argv) != 3:
        print("Usage: python scp_copy.py <remote_host> <remote_file>")
        sys.exit(1)

    # Получение имени хоста и имени файла из аргументов командной строки
    remote_host = sys.argv[1]
    remote_file = sys.argv[2]

    # Вызов функции копирования файла по SSH
    scp_copy_file(remote_host, remote_file)
