
# n, m, k를 공백으로 구분하여 받기
n, m, k = map(int, input().split())

# n개의 수를 공백으로 구분하여 받기
data = list(map(int, input().split()))

data.sort() # 정렬
first, second = data[n-1], data[n-2]
result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)
