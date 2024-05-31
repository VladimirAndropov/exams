import paramiko
import sys


def copy_file(remote_host, remote_path, local_path):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(remote_host, username='your_username', password='your_password')

    sftp = ssh.open_sftp()
    sftp.get(remote_path, local_path)
    sftp.close()
    ssh.close()


if __name__ == "__main__":
    if len(sys.argv) == 3:
        remote_host = sys.argv[1]
        remote_path = sys.argv[2]
        local_path = './' + remote_path.split('/')[-1]
        copy_file(remote_host, remote_path, local_path)
    else:
        print("Please provide the remote host and file path as arguments.")
