import time
import paramiko

def copyFile(filename):
    trans = paramiko.Transport(("", 22022))
    trans.connect(
        username="root",
        password=""
    )
    sftp = paramiko.SFTPClient.from_transport(trans)
    sftp.put(filename, "/tmp/{}".format(filename))
    sftp.close()

for i in range(10):
    copyFile('a.txt')
    time.sleep(1)
