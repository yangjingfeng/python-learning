import paramiko
import time


ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.191', port=22, username='root', password='1')

channel = ssh.invoke_shell()
channel.settimeout(100)
channel.send('pwd\n')
channel.send('ls -lh\n')
buff = ''
while not buff.endswith('# '):
    resp = channel.recv(1024).decode()
    buff += resp
print(buff)
# 关闭连接
time.sleep(1)
channel.close()
