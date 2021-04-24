n = int(input())
def f(n):
	count = 0
	dupl = []
	while True:
		dupl.append(n)
		n += 1
		n = int(str(n).rstrip('0'))
		count += 1
		if n in dupl:
			return count
print(f(n))
