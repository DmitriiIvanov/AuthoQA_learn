word_1 = input()
word_2 = input()
if ('w' in word_1 or 't' in word_1) and ('w' in word_2 or 't' in word_2):
    print(word_1)
    print(word_2)
elif 'w' in word_1 or 't' in word_1:
    print(word_1)
elif 'w' in word_1 or 't' in word_2:
    print(word_2)
