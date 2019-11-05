import re
pattern = re.compile('/({[^{}:]+:?[^{}:]*})')
s = '/student/{name:str}/xxx/{id:int}'
s1 = '/student/xxx/{id:int}/yyy'

TYPEPATTERNS = {
    'str': r'[^/]+',
    'word': r'\w+',
    'int': r'[+-]?\d+',
    'float': r'[+-]?\d+\.\d+',
    'any': r'.+'
}
TYPECAST = {
    'str': str,
    'word': str,
    'int': int,
    'float': float,
    'any': str
}

print(pattern.search(s).end())