from itertools import combinations
def minimum_pluses(A):
	l1,l2 = A.split('=')
	c = 0
	s = list('+'.join(l1))
	l2 = int(l2)
	b = list(range(1,len(s),2))
	if int(l1) == l2:
		return 0
	for i in range(1,len(b)+1):
		tmp = list(combinations(b,i))
		#print(tmp)
		for v in tmp:	
			t1 = s[:]		
			for i in v:		
				t1[i] = ''
			#print(t1)
			if eval(''.join(t1)) == l2:
				for p in t1:
					if p == '+':
						c += 1
				return c
	return -1


def main():

    A = input()
    result = minimum_pluses(A)
    print(result)
if __name__ == "__main__":
    main()
