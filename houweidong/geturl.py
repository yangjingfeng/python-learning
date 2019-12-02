import requests
import re
import time
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
    'Host':'www.audio699.com',
    'Connection': 'keep-alive',
}
s = requests.Session()
s.get('http://www.audio699.com/book/1054.html', headers=headers)
for i in range(1,2):
    res = s.get('http://www.audio699.com/book/1054/{}.html'.format(i),headers=headers)
    time.sleep(1)
    with open('restext.html','w') as f:
        f.writelines(res.content.decode())
    with open('restext.html') as f:
        for line in f.readlines():
            res = re.findall('\s*<source src="(\S*)"',line)
            if res:
                print(res[0])
                data = s.get(res[0],headers=headers).content
                with open('downloads\{}.m4a'.format(i),'wb') as mf:
                    mf.write(data)