import sys
import os
import paramiko

def scp_copy_file(remote_host, remote_file):
    try:
        # Подключение к удаленному хосту по SSH
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(remote_host)

        # Открытие сессии SCP для копирования файла
        with ssh_client.open_sftp() as sftp:
            # Копирование файла с удаленного хоста в текущую директорию
            sftp.get(remote_file, os.path.basename(remote_file))

        print("Файл успешно скопирован.")
    except paramiko.AuthenticationException:
        print("Ошибка аутентификации. Проверьте логин и пароль.")
    except paramiko.SSHException as e:
        print("Ошибка SSH:", e)
    except FileNotFoundError:
        print("Файл не найден.")
    finally:
        # Закрытие SSH-соединения
        if ssh_client:
            ssh_client.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python scp_copy_file.py <удаленный_хост> <удаленный_файл>")
        sys.exit(1)

    remote_host = sys.argv[1]
    remote_file = sys.argv[2]

    # Вызов функции для копирования файла по SSH
    scp_copy_file(remote_host, remote_file)
