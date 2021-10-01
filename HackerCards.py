#HackerCards is a trendy new game. Each type of HackerCard has a distinct ID number greater than or equal to 1, and the cost of each HackerCard equal to its ID number.
inp = [1, 3, 4]
d = 7
h = 0
res = []
ls = 0
for i in range(1, d+1):
    if h < len(inp):
        if inp[h] == i:
            h += 1
            continue
    ls += i
    res.append(i)
    if ls == d:
        print(res)
        break
    elif ls > d:
        res.pop()
        print(res)
        break
