rubles = int(input())
dollars = int(input())
euro = int(input())

print(
    f'У пользователя в наличии {rubles} рублей, за них он может получить {rubles // dollars} долларов или {rubles // euro} евро')
