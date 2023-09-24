'''
Задание 10.
Дано предложение. Выведите на экран те слова, которые отличны от первого слова,
и в которых нет повторяющихся букв.
'''

import string

txt = input()

for znp in string.punctuation:
    txt = txt.replace(znp, '')

words = txt.split(' ')

for word in words:
    if word != words[0] and len(set(list(word))) == len(word):
        print(word)