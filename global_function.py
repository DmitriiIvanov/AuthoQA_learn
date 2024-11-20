var_1 = 10  # globak variable
var_2 = 20
print(var_1, var_2)


def sum_var():
    var_1 = 20  # lockale variable
    var_2 = 30
    result = var_1 + var_2
    print(result)

def sub_var():
    # var_1 = 20  # lockale variable
    # var_2 = 30
    result = var_1 - var_2
    print(result)

sum_var()
sub_var()