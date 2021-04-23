l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))

s1 = sum(l1)
s2 = sum(l2)

pairs = []

for i in l1:
    for j in l2:
        if s1-i+j == s2-j+i:
            pairs.append((i,j))
if len(pairs) == 0:
    print('no pairs found')            
else:
    pairs = set(pairs)
    print(*pairs)
