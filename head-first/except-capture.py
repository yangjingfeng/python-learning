man=[]
other=[]
try:
    data=open('fun.txt')
    for each_line in data:
        try:
            (role,each_spoken)=each_line.split(':',1)
#             print (a[0],"said:",a[1],end="")
            each_spoken=each_spoken.strip()
            if role=="Man":
                man.append(each_spoken)
            else:
                other.append(each_spoken)
        except ValueError:
            pass
    print (man)
    print (other)
    data.close()
except IOError:
    print ("the data file is missing!")


