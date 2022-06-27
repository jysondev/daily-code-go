from unittest import result


input_data = input()
row = int(input_data[1])
colum = int(ord(input_data[0])) - int(ord('a')) +1

# 나이트 이동가능 방향 8가지
steps = [(-2, 1), (-2, -1), (2, 1), (2, -1), (-1, 2), (1, 2), (-1, -2), (1, -2)]
result = 0

for step in steps:
    next_row = row+step[0]
    next_colum = colum+step[1]

    if next_row>=1 and next_row<=8 and next_colum>=1 and next_colum<=8:
        result+=1

print(result)