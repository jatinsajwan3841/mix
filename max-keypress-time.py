'''kt = []
for _ in range(int(input())):
    t = list(map(int,input().split()))
    kt.append(t)'''
kt = [[0, 2], [1, 5], [0, 9], [2, 15]]
c = {}
for n in kt:
    c[n[0]] = 0
p = 0
for i in range(len(kt)):
    c[kt[i][0]] = max(kt[i][1] - p, c[kt[i][0]])
    p = kt[i][1]
print(chr(97+max(c,key=c.get)))
