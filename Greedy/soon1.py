from itertools import count


n, k = map(int, input().split())
count = 0
while n > 1:
    a = n%k
    if a == 0:
        n=n/k
    else:
        n-=1
    count+=1

print(count)