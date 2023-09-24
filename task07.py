'''
Задание 7.
Дано предложение. Найти длину его самого короткого слова.
'''

import string

length = float('inf')
txt = input()

for znp in string.punctuation:
    txt = txt.replace(znp, '')

txt = txt.split(' ')

for word in txt:
    length = min(len(word), length)

print(length)