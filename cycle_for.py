numbers_1 = list(map(int, input().split()))
numbers_2 = list(map(int, input().split()))

summ_numbers_1 = 0
summ_numbers_2 = 0

for i in numbers_1:
    summ_numbers_1 = summ_numbers_1 + i

for i in numbers_2:
    summ_numbers_2 = summ_numbers_2 + i

if summ_numbers_1 > summ_numbers_2:
    print(1)
elif summ_numbers_2 > summ_numbers_1:
    print(2)
