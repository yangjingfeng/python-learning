import paramiko

ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(hostname='192.168.1.191', port=22, username='root', password='1')
except ValueError:
    print("Can't connect to Router")
ssh.invoke_shell()
ssh_con=ssh.invoke_shell()
output=ssh_con.recv(500)
print(output.decode())
# 路由器参数初始化

ssh_con.send("pwd\n")
output = ssh_con.recv(500)
print(output.decode())
ssh_con.send("test\n")
output = ssh_con.recv(500)
print(output.decode())
ssh_con.send("sh run\n")
output = ssh_con.recv(500)
print(output.decode())
