import paramiko
import matplotlib as plt
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
client.connect('192.168.1.230',22,'root','1')
res = client.exec_command('netstat -an')[1].read().decode()

[ print (i) for i in res.split("\n") if i.startswith('tcp') ]

