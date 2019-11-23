# import requests
# import threading
#
# def getnginx():
#     print(requests.get('http://192.168.1.226/status').content.decode())
#
# for i in range(10):
#     t = threading.Thread(target=getnginx)
#     t.run()

class Context(dict):
    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise ArithmeticError('Attribute {} not exist'.format(item))

    def __setattr__(self, key, value):
        self[key]=value

# mydic = {'a':'aaa','b':'bbb'}
# print(Context(mydic).a)
con = Context()
con.a = 'aaa'
print(con.a)