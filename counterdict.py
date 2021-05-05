from collections import Counter
input()
shoestore = input().split()
count = Counter(shoestore)
amount = 0
for _ in range(int(input())):
    tmp = input().split()
    if tmp[0] in count and count[tmp[0]] != 0:
        amount += int(tmp[1])
        count[tmp[0]] -= 1
print(amount)
