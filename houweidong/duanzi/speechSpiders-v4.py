import tkinter
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
            return resHmtml
myspeech = speechOne()
speech = myspeech.get()

def mycontent(text):
    canv.delete(0.0, 'end')
    columnWeight = 30
    while True:
        mysite = [50,columnWeight]
        print(text)
        mycontext = text[:10]
        text = text[10:]
        if mycontext:
            canv.insert(mysite,text=mycontext,anchor=tkinter.W, font = columnFont)
        else:
            break
        columnWeight += 30
    canv.after(1000, mycontent, myspeech.get())

root = tkinter.Tk()
root.title('生活调剂')
canv = tkinter.Canvas(background='#e3f9ed')
canv.pack()
columnFont = ('微软雅黑', 18)
mycontent(myspeech.get())

root.mainloop()
