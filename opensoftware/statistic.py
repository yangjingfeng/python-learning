import xlrd

def softwarecount(file):
    result = 0
    for (k,v) in hostnamecount(file):
        result += v
    return result

def systemHostname(file):
    xls_file = xlrd.open_workbook(file)
    xls_sheet = xls_file.sheets()[0]
    xls_content = xls_sheet.col_values(0)
    xls_content_ip = xls_sheet.col_values(1)
    hostdic= {}
    iplist=[]
    for k,v in zip(xls_content,xls_content_ip):
        if v not in iplist:
            iplist.append(v)
            hostdic.setdefault(k,0)
            hostdic[k] += 1
    return sorted(hostdic.items(),key= lambda x:x[1],reverse=True)


def systemSoftware(file):
    xls_file = xlrd.open_workbook(file)
    xls_sheet = xls_file.sheets()[0]
    xls_content = xls_sheet.col_values(0)
    systemdic = {}
    for item in xls_content:
        systemdic.setdefault(item,0)
        systemdic[item] += 1
    newipcount = sorted(systemdic.items(),key = lambda x:x[1],reverse=True)
    return newipcount



def hostnamecount(file):
    xls_file = xlrd.open_workbook(file)
    xls_sheet = xls_file.sheets()[0]
    xls_content = xls_sheet.col_values(2)
    ipcount = {}
    for item in xls_content:
        ipcount.setdefault(item,0)
        ipcount[item] += 1
    newipcount = sorted(ipcount.items(),key = lambda x:x[1],reverse=True)
    return newipcount

def softwareClassCount(file):
    xls_file = xlrd.open_workbook(file)
    xls_sheet = xls_file.sheets()[0]
    xls_content = xls_sheet.col_values(3)
    software = {}
    for item in xls_content:
        software.setdefault(item,0)
        software[item] += 1
    newipcount = sorted(software.items(),key = lambda x:x[1],reverse=True)
    return newipcount

print("software count:--------------")
print(softwarecount('./resultfile/20181117.xls'))
print(softwarecount('./resultfile/20190322.xls'))
print("system contain software:--------------")
for k,v in systemHostname('./resultfile/20181117.xls'):
    print(k,v,end='; ')
print()
for k,v in systemHostname('./resultfile/20190322.xls'):
    print(k,v,end='; ')
print()
print("system contain host:--------------")
for k,v in systemSoftware('./resultfile/20181117.xls'):
    print(k,v,end='; ')
print()
for k,v in systemSoftware('./resultfile/20190322.xls'):
    print(k,v,end='; ')
print()
print("host contain software:--------------")
for k,v in hostnamecount('./resultfile/20181117.xls'):
    print(k,v,end='; ')
print()
for k,v in hostnamecount('./resultfile/20190322.xls'):
    print(k,v,end='; ')
print()

print("software class count:--------------")
for k,v in softwareClassCount('./resultfile/20181117.xls'):
    print(k,v,end='; ')
print()
for k,v in softwareClassCount('./resultfile/20190322.xls'):
    print(k,v,end='; ')
print()



