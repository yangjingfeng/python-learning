import sys
def print_lol(the_list,indent=False,level=0,fn=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item,indent,level+1,fn)
        else:
            if indent:
                for tab_stop in range(level):
                    print ("\t",end="",file=fn),
            print (each_item,file=fn)

man=[]
other=[]
try:
    data=open('fun.txt')
    for each_line in data:
        try:
            (role,each_spoken)=each_line.split(':',1)
            each_spoken=each_spoken.strip()
            if role=="Man":
                man.append(each_spoken)
            else:
                other.append(each_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print ("the data file is missing!")
print (man)

try:
    with open("man.txt","w") as manfile,open("otherfile.txt","w") as otherfile:
        print_lol (man,fn=manfile)
        print_lol (other,fn=otherfile)
except IOError as err:
    print ("File error"+str(err))  
