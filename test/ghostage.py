def verify_anagrams(first:str,second:str):
    first = set(first.split(','))
    second = set(second.split(','))
    a = sorted(list(first.intersection(second)))
    return ','.join(a)

print(verify_anagrams("hello,world", "hello,earth"))
