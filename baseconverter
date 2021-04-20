def basec(num,base):
    if num < base:
        return [int(num%base)]
    res = []
    while True:        
        tmp = num % base
        res.append(tmp)
        num = int(num/base)
        if num < base:
            res.append(num)
            res.reverse()
            return res
def fullbasec():
    num = int(input("num : "))
    base = int(input("base : "))
    result = basec(num,base)
    for index,val in enumerate(result):
        if val > 9:
            result[index] = chr(val+55)  
    return result            

print(*fullbasec())
