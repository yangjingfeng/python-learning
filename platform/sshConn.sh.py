import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.1.226',22,'root','1')
res = client.exec_command('netstat -anp | grep ^tcp')
print(res[1].read().decode())
