from pytube import YouTube
import re
import requests
import os
import paramiko

def copyFile(filename):
    trans = paramiko.Transport(sock=("", 22))
    trans.connect(
        username="",
        password=""
    )
    sftp = paramiko.SFTPClient.from_transport(trans)
    sftp.put(filename, "/usr/local/nginx/html/movies/{}".format(filename))

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
    'Connection': 'keep-alive',
}
url = 'https://www.youtube.com/watch?v=fa7cJjKJ_lk&list=PLAPUFB0EKWq-tqpdLoa-dVbFSJucbwt6D'

response = requests.get(url,headers=headers)

for item in re.findall('data-video-id="(.*?)".*?data-video-title="(.*?)"',response.text):
    print(item)
    fileList = os.listdir('/opt')
    k,v = item
    v = '{}.mp4'.format(v)
    if v in fileList:
        pass
    else:
        YouTube('https://www.youtube.com/{}'.format(k)).streams.get_highest_resolution().download()
    copyFile(v)
    os.remove(v)

