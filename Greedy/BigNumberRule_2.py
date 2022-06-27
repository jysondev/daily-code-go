
# n, m, k를 공백으로 구분하여 받기
from itertools import count

# n array 갯수
# m 더하는 갯수
# k 한 숫자가 더할수있는 최대갯수
n, m, k = map(int, input().split())

# n개의 수를 공백으로 구분하여 받기
data = list(map(int, input().split()))

data.sort() # 정렬
first, second = data[n-1], data[n-2]
result = first*k*(int(m/k)) + (m%k)*second

print(m/k)
print(m%k)
print(result)
