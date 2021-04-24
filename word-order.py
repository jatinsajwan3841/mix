# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
arr =[]
for i in range(n):
    arr.append(input())
count = {n:0 for n in arr}
for n in arr:
    count[n] += 1
print(len(count))
for key, value in count.items():
    print(value, end=' ')
