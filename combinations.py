from itertools import combinations
_ = input()
st = list(input().split())
comb = tuple(combinations(st,int(input())))
count = 0
for vals in comb:
	if 'a' in vals:
		count += 1
print(count/len(comb))
