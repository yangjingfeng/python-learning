import requests
import re

class speechOne:
    speech = ''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
        'Connection': 'keep-alive',
    }
    def get(self):
        res = requests.get('https://www.nihaowua.com/home.html',headers=self.headers)
        resHmtml = res.content.decode()
        content = re.findall('<section>.*</section>',resHmtml)
        try:
            speech = content[0].split('>')[3].split('<')[0]
            return speech
        except:
            pass

