from itertools import count


n = int(input())

sec, min = 60, 60
count = 0

for i in range(n+1):
    for s in range(sec):
        for m in range(min):
            if '3' in str(s) + str(m) + str(i):
                count+=1
print(count)