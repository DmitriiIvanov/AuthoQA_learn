numbers = [1, 2.5, 5, 7, 8, 3.9]
list_int = []
list_float = []
for i in numbers:
    if type(i) == float:
        list_float.append(i)
    else:
        list_int.append(i)

print(list_int)
print(list_float)
