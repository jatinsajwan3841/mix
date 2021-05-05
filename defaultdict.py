from collections import defaultdict
A = defaultdict(list)
B = []
nm = input().split()
for ind in range(1,int(nm[0])+1):
    A[input()].append(ind)
for _ in range(int(nm[1])):
    B.append(input())
for val in B:
    if val in A:
        print(*A[val])
    else:
        print(-1)
