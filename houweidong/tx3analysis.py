import json
import time
import pymysql
createtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

conn = pymysql.Connect('192.168.1.231','python','python','python',3306)
cur = conn.cursor()
# print('门派 价格   装评   炼护 加护 大法 小法 大物 小物 疾语 追电 防御 回避 物防 命中 会心 万钧 御心 诛心')
mydic = {
    '门派':('equip_type',10),
    '等级':('equip_level',10),
    '价格': ('price', 10),
    '装评': ('equ_xiuwei', 10),
    '炼护': ('lian_hu', 10),
    '加护': ('jiahu', 10),
    '大法': ('mattack_max', 10),
    '小法': ('mattack_min', 10),
    '大物': ('pattack_max', 10),
    '小物': ('pattack_min', 10),
    '疾语': ('castspeed', 10),
    '追电': ('movespeed', 10),
    '防御': ('pdef', 10),
    '回避': ('avoid', 10),
    '物防': ('mdef', 10),
    '命中': ('hit', 10),
    '会心': ('huixin', 10),
    '万钧': ('wan_jun', 10),
    '御心': ('yu_xin', 10),
    '诛心': ('zhu_xin', 10),
    '名称' : ('equip_name',20),
}

mytype ={
    '1' : '荒火',
    '2' : '天机',
    '3' : '翎羽',
    '4' : '魍魉',
    '5' : '太虚',
    '6' :  '云麓',
    '7' :  '冰心',
    '8' : '弈剑',
    '9' : '鬼墨',
    '10' : '龙巫',
    '11' : '幽篁',
}


# for k,v in mydic.items():
#     print('{:<{}s}'.format(k,v[1]-2),end='')
# print()
# with open('tx3result.txt') as f:
#     res = json.loads(f.readlines()[0])
#     for line in res['msg']:
#         for value in mydic.values():
#             if value[0] == 'equip_type':
#                 # print(mytype.get(line[value[0]]))
#                 print('{:<{}s}'.format(mytype.get(line[value[0]]), value[1]-2), end='')
#             elif value[0] == 'price':
#                 print('{:<{}d}'.format(int(line[value[0]]/100), value[1]), end='')
#             else:
#                 print('{:<{}s}'.format(str(line[value[0]]), value[1]), end='')
#         print()

with open('tx3result.txt') as f:
    res = json.loads(f.readlines()[0])
    for line in res['msg']:
        lineitems = []
        for value in mydic.values():
            if value[0] == 'equip_type':
                # print(mytype.get(line[value[0]]))
                print('{:<{}s}'.format(mytype.get(line[value[0]]), value[1]-2), end='')
                lineitems.append(mytype.get(line[value[0]]))
            elif value[0] == 'price':
                print('{:<{}d}'.format(int(line[value[0]]/100), value[1]), end='')
                lineitems.append(str(line[value[0]]/100))
            else:
                print('{:<{}s}'.format(str(line[value[0]]), value[1]), end='')
                lineitems.append(str(line[value[0]]))
        lineitems.append(createtime)
        print()
        print(tuple(lineitems))
        sqlclause = "insert into tx3result2  (equip_type, equip_level, price, equ_xiuwei, lian_hu, jiahu, mattack_max, mattack_min, pattack_max, pattack_min, castspeed, movespeed, pdef, avoid, mdef, hit, huixin, wan_jun, yu_xin, zhu_xin, equip_name, createtime) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cur.execute(sqlclause, args=tuple(lineitems))

conn.commit()