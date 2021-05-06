m = 'baccbbbdabcdbca'
n = 'abc'
from itertools import permutations
tmp = list(permutations(n))
res = []
for v in tmp:
	v = ''.join(v)
	if v in m:
		res.append(m.index(v))
print(sorted(res))
