import requests
import json

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
    'Connection': 'keep-alive',
}
data = {
    'act':'overall_search_role',
    'order_by':'',
    'page':'1',
    'other_arg':'',
    'price_max':'1000000',
    'price_min':'100000',
    'equip_jia_hu_min':'234',
    'equip_level_min':'80',
    # 'mattack_max':'4000',
}
tx3url = 'https://tx3.cbg.163.com/cgi-bin/search.py'
res = requests.post(tx3url,data=data,headers=headers)
with open('tx3result.txt','w') as f:
    for line in res.content.decode():
        f.write(line)


