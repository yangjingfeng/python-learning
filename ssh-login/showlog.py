import paramiko


ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.100', port=22, username='test', password='test')

channel = ssh.invoke_shell()
channel.settimeout(100)
channel.send('en\n')
channel.send('test\n')
channel.send('sh log\n')
buff = ''
while not buff.endswith('# '):
    channel.send(' ')
    resp = channel.recv(9999).decode()
    buff += resp
print(buff)
# 关闭连接
channel.close()
