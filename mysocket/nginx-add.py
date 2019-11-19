import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.1.226',22,'root','1')
res = client.exec_command('ls -l nginx-1.13.12.tar.gz')

class CCmd():
    def __init__(self,ip,port,username,password):
        self.ip = ip
        self.port = int(port)
        self.username = username
        self.password = password
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.ip, self.port, self.username, self.password)

    def exec(self,cmd):
        self.cmd = cmd
        stdin, stdout, stderr = self.client.exec_command(self.cmd)
        if stdout.channel.recv_exit_status() == 0:
            return (stdout.channel.recv_exit_status(),stdout.read().decode())
        else:
            return (stdout.channel.recv_exit_status(),stderr.read().decode())



mytest01 = CCmd('192.168.1.226','22','root','1')
if mytest01.exec('[ -f nginx-1.13.12.tar.gz ]')[0] == 0:
    res = mytest01.exec('tar -xf nginx-1.13.12.tar.gz')
    if res[0] == 0:
        mytest01.exec('cd /root/nginx-1.13.12 && ./configure --prefix=/usr/local/nginx --with-http_stub_status_module')
        mytest01.exec('cd /root/nginx-1.13.12 && make')
        mytest01.exec('cd /root/nginx-1.13.12 && make install')