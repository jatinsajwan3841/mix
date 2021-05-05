from itertools import product
km = input().split()
inp = []
for _ in range(int(km[0])):
    tmp = list(map(int,input().split()))[1:]
    inp.append(tmp)

def maximize(perm):
    mtp = 0
    for val in perm:
        tmp = 0        
        for v in val:
            tmp += v*v
        tmp = tmp%int(km[1])
        mtp = max(mtp,tmp)
    return mtp

perm = list(set(product(*inp)))
print(maximize(perm))
