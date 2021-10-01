#for each group of contiguous computers of a certain length determine min amount of disk space available on a computer.
def segment(x, space):
    s = 0
    e = x
    res = []
    while e <= len(space):
        res.append(min(space[s:e]))
        s += 1
        e += 1
    return max(res)
