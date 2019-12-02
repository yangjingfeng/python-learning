import threading
import paramiko
import time

# sshconn.connect('192.168.1.206',22,'root','1')
# s = sshconn.exec_command('sleep 5;pwd')

def myconnect(ipaddr):
    sshconn = paramiko.SSHClient()
    sshconn.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    try:
        sshconn.connect(ipaddr,22,'root','1')
        s = sshconn.exec_command('sleep 5;pwd')
        print(ipaddr,s[1].read().decode())
    except:
        pass

for i in range(220):
    ipaddr = '192.168.1.{}'.format(i)
    t = threading.Thread(target=myconnect,args=(ipaddr,),name="thread--{}".format(i))
    t.start()
time.sleep(1)
print(threading.enumerate())




