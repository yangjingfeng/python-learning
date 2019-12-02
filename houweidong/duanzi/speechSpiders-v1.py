import requests
import re
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
    'Connection': 'keep-alive',
}

res = requests.get('https://www.nihaowua.com/home.html',headers=headers)
resHmtml = res.content.decode()
# print(resHmtml)

def main():
    content = re.findall('<section>(.*)</section>',resHmtml)
    try:
        speech = re.findall('>(\S*)<', content[0])
        with open('result.txt', 'a+', encoding='utf8') as f:
            f.write(speech[0]+'\n')
        print(speech)
    except:
        print(resHmtml)
if __name__ == '__main__':
    main()