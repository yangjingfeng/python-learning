import re
mystr = '<cite>aaa</q>'

print(re.findall('<cite>(\S*)</[cite|q|p]>',mystr))
