'''
Задание 9.
Дано предложение. В нем только два слова одинаковые. Найти эти слова.
'''

import string

txt = input()

for znp in string.punctuation:
    txt = txt.replace(znp, '')

words = set(txt.split(' '))

for word in words:
    if txt.count(word) == 2:
        print(word)
        break