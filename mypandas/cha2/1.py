import sentry_sdk
sentry_sdk.init("http://3278a90811e54fe8a5ef0c75000a6c02@192.168.1.202:9000/2")


try:
    1 / 0
except:
    print('not ok')