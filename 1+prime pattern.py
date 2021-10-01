inp = int(input())


def isPrime(v):
    if v == 1:
        return True
    elif v == 2:
        return True
    else:
        for i in range(2, v):
            if v % i == 0:
                return False
            else:
                pass
        return True


def nPrime(n):
    temp = []
    start = 1
    while True:
        if isPrime(start):
            temp.append(start)
            if len(temp) == n:
                return temp
        start += 1


for i in range(1, inp+1):
    print(*nPrime(i))
