import os
def format_time(time_string):
    if '-' in time_string:
        splitter='-'
    elif ':' in time_string:
        splitter=':'
    else:
        return (time_string)
    (mins,secs)=time_string.split(splitter)
    return (mins+'.'+secs)
b=[]
for my_file in os.listdir(os.getcwd()):
    if my_file.find("txt") != -1:
        with open(my_file,'r') as read_file:
            a=read_file.readline().split(",")
            for i in a:
                b.append(format_time(i))
            print (sorted(b))
            b=[]

