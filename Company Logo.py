if __name__ == '__main__':
    s = input()
    s= sorted(s)
    count = {n:0 for n in s}
    c = 0
    for v in s:
        count[v] += 1
    count = {k: v for k, v in sorted(count.items(), key=lambda item: item[1],reverse=True)}
    for key,value in count.items():
        print(key,value)
        c+=1
        if c == 3:
            break
