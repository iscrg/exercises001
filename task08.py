'''
Задание 8.
Дано предложение. Напечатать все его слова в порядке неубывания их длин.
'''

import string

txt = input()

for znp in string.punctuation:
    txt = txt.replace(znp, '')

txt = txt.split(' ')

txt.sort(key=len)
print(' '.join(txt))