from collections import namedtuple
ad = 0
stn = int(input())
st = namedtuple('st',input().split())
for _ in range(stn):    
    tmp = st(*input().split())
    ad += int(tmp.MARKS)
print(round((ad/stn),2))
