from posixpath import split
from unittest import result

# n * m 
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    if min_value > result:
        result = min_value

print(result)