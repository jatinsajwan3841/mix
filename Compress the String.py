# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
s = input()
for key, value in groupby(s):
    print((len(list(value)), int(key)), end=' ')
