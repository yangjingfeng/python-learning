import threading
import time

event=threading.Event()
def light():
    print('red')
    time.sleep(3)
    event.set()
def car(name):
    print('{}'.format(name))
    event.wait()
    print('{}'.format(name))

if __name__ == '__main__':
    t1 = threading.Thread(target=light)
    t1.start()
    for i in range(10):
        t = threading.Thread(target=car,args=(i,))
        t.start()