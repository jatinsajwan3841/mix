n = int(input())
arr = map(int, input().split())
s = list(set(arr))
s.sort()
print(s[-2])