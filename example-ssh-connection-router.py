import paramiko
import getpass
import time

host = input('Please enter a host: ')
un = input('Please enter username: ')
pa = getpass.getpass('Please enter password: ')

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=host, username=un, password=pa)

print("Successfully connected")

remote_connection = ssh_client.invoke_shell()
remote_connection.send("show version | include uptime \n")

time.sleep(1)

output = remote_connection.recv(18999).decode("ascii")
print(output)
ssh_client.close
