# def __init__(self):
#     pass
# Xclass = type('x', (object,), {'a':100,'__init__':__init__})
# print(Xclass)
# print(type(Xclass))
# print(Xclass.__dict__)
# print(Xclass.mro())
# print(Xclass().__dict__)


# import pymysql
# conn = pymysql.Connect('192.168.1.231','python','python','python',3306)
#
# cur = conn.cursor()
# sqlclause = 'show processlist'
# cur.execute(sqlclause)
# for line in cur.fetchall():
#     print(line)
#
# mydic = {
#     '门派':('equip_type',10),
#     '等级':('equip_level',10),
#     '价格': ('price', 10),
#     '装评': ('equ_xiuwei', 10),
#     '炼护': ('lian_hu', 10),
#     '加护': ('jiahu', 10),
#     '大法': ('mattack_max', 10),
#     '小法': ('mattack_min', 10),
#     '大物': ('pattack_max', 10),
#     '小物': ('pattack_min', 10),
#     '疾语': ('castspeed', 10),
#     '追电': ('movespeed', 10),
#     '防御': ('pdef', 10),
#     '回避': ('avoid', 10),
#     '物防': ('mdef', 10),
#     '命中': ('hit', 10),
#     '会心': ('huixin', 10),
#     '万钧': ('wan_jun', 10),
#     '御心': ('yu_xin', 10),
#     '诛心': ('zhu_xin', 10),
#     '名称' : ('equip_name',20),
# }
# for line in mydic.values():
#     print("{} varchar({}),".format(line[0],line[1]))

# import time
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
# import pymysql
# conn = pymysql.Connect('192.168.1.231','python','python','python',3306)
# cur = conn.cursor()
# count = 1
# sqlclause = "insert into tx3result (yu_xin) values('%s' )"
# cur.execute(sqlclause,args=(count,))
# conn.commit()
# for line in cur.fetchall():
#     print(line)
# import random
# for i in range(10):
#     print(random.randrange(1,5))

import re
a = ['龙巫', '80', '8200.0', '92713', '195', '234', '792', '513', '2577', '1139', '0', '445', '5558', '548', '2143', '1596', '2581', '0', '117', '345', '阿燚丶', '2019-11-28 11:06:48']
for item in a:
    if re.fullmatch('\d+',item):
        print(item)

