from itertools import groupby
inp = 'aaaabbbccccccccdaa'

# using inbuilt groupby
for v, c in groupby(inp):
    print(v, end='')
    print(len(list(c)), end='')
print()

# manually
prev, count = inp[0], 0
res = inp[0]
for v in inp:
    if prev == v:
        count += 1
    else:
        res += str(count) + v
        prev = v
        count = 1
res += str(count)
print(res)
