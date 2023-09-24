'''
Задание 3.
Дан текст. Определить, сколько различных букв в нем.
'''

import string

text = input().lower()
res = set()

for symbol in text:
    if symbol not in string.ascii_letters:
        res.add(symbol)

print(len(res))
