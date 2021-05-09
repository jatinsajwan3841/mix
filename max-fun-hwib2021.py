from itertools import combinations
'''n = int(input())
k = int(input())
ni = [int(input()) for _ in range(n)]'''
n = 6
k = 3
ni = [2,3,4,1,2,3]

def score(l):
    s = 0
    for i,v in enumerate(l):
        s += v * (i+1)
    return str(s)

def gencom(n,k):
    for val in list(combinations(range(1,n),k-1)):
        yield val

if n == k:
    r = []
    for v in ni:
        r.append(str(v))
    print(eval('&'.join(r)))       

else:
    c = -1
    for v in gencom(n,k):
        tmp = [ni[0:v[0]]]
        for i in range(1,len(v)):
            tmp.append(ni[v[i-1]:v[i]])
        tmp.append(ni[v[len(v)-1]:])
        tc = []
        for i in tmp:
            tc.append(score(i))
        tc = eval('&'.join(tc))
        if tc >= c:
            c = tc
            #print(tmp)
    print(c)
