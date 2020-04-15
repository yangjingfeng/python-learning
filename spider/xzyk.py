from urllib.parse import urlencode
from pytube import YouTube
import re

import requests
search_query = {
    'search_query' : '笑逐言开201906',
    'pbj' : 1,
}

data = urlencode(search_query)
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
    'Connection': 'keep-alive',
}
url = 'https://www.youtube.com/results' + '?' + data

response = requests.get(url=url,headers=headers)
for item in re.findall('yt-lockup-content.*?href="(.*?)".*?title="(.*?)"',response.text):
    k,v = item
    print(k,v)


exit(3)

yt = YouTube('https://www.youtube.com/fxB5UzLHPcs')

YouTube('https://www.youtube.com/fxB5UzLHPcs').streams.get_highest_resolution().download()

yt = YouTube('https://www.youtube.com/watch?v=fxB5UzLHPcs')

yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()