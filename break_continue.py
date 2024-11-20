numbers = list(map(int, input().split()))
result = 0
for i in numbers:
    if i <= 0:
        continue
    else:
        result = result + i

print(result)

