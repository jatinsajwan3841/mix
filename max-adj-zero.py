from itertools import groupby

num = int(input())
base = int(input())

def basec(num,base):
    if num < base:
        return [int(num%base)]
    res = []
    while True:        
        tmp = num % base
        res.append(tmp)
        num = int(num/base)
        if num < base:
            res.append(num)
            res.reverse()
            return res
result = basec(num,base)
print(result)
zeroes = []
for key, value in groupby(result):
    if key == 0:
        zeroes.append(len(list(value)))
if len(zeroes) == 0:
    print(-1)
else:
    print(max(zeroes))
