# 1й2ц3у
def a():
    print('Start of a()')
    b()  # Вызов b().


def b():
    print('Start of b()')
    c()  # Вызов c().


def c():
    print('Start of c()')
    42 / 0  # Порождает ошибку деления на нуль.

a()  # Вызов a()
