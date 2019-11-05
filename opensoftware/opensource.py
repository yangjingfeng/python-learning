import xlrd
import re
import xlwt
from pathlib import Path


xls_file_all = xlrd.open_workbook('./sourcefile/jumpserver.xls')
xls_sheet_all = xls_file_all.sheets()[0]
xls_content_all = xls_sheet_all.col_values(0)
def getIndex(hostname):
    for index in range(len(xls_content_all)-1):
        if xls_content_all[index].strip().lower() == hostname.strip().lower():
            return index

def opensource(file):
    p = Path(file)
    rowcount = 0
    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet('software')
    xls_file = xlrd.open_workbook(file)
    xls_sheet = xls_file.sheets()[0]
    xls_content_ip =  xls_sheet.col_values(0)
    xls_content_result =  xls_sheet.col_values(8)
    hostcontent = []
    for i in range(len(xls_content_ip)):
        if xls_content_result[i]=="" or xls_content_result[i]=="@ ok":
            hostcontent.append(xls_content_ip[i])
            continue
        for line in xls_content_result[i].split('\n'):
            eachline = line.split("@")
            if eachline[0] != '' and len(eachline) >= 5:
                if eachline[1].strip() == "postgres" and re.findall('\s-D\s',eachline[4]):
                    index = getIndex(eachline[0])
                    if index:
                        worksheet.write(rowcount, 0, label=xls_sheet_all.col_values(4)[index])
                        worksheet.write(rowcount, 1, label=xls_sheet_all.col_values(1)[index])
                    for group in range(5):
                        worksheet.write(rowcount, group+2, label=eachline[group].strip())
                    rowcount += 1
                if eachline[1].strip() != "postgres":
                    alllength = re.findall(eachline[1].strip(),eachline[4])
                    reglength = re.findall('lib\w*/'+eachline[1].strip(),eachline[4])
                    if len(alllength) != len(reglength):
                        index = getIndex(eachline[0])
                        if index:
                            worksheet.write(rowcount, 0, label=xls_sheet_all.col_values(4)[index])
                            worksheet.write(rowcount, 1, label=xls_sheet_all.col_values(1)[index])
                        for group in range(5):
                            worksheet.write(rowcount, group+2, label=eachline[group].strip())
                        rowcount += 1
    workbook.save('resultfile/{}'.format(p.name))
    return hostcontent
opensource('./sourcefile/20190322.xls')
opensource('./sourcefile/20181117.xls')