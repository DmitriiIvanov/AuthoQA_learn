# 1 2 3 4
# 3 4 5 6
# 4 5

numbers_1 = set(map(int, input().split()))
numbers_2 = set(map(int, input().split()))
numbers_3 = set(map(int, input().split()))
result = numbers_1 & numbers_2
for i in result:
    if i in numbers_3:
        continue
    else:
        print(i)

