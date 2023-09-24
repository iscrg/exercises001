'''
Задание 1.
Дан текст. Необходимо определить максимальное количество последовательных пробельных символов  в нём.
'''

import string

m_res = 0
res = -1
text = input()

for symbol in text:
    if symbol in string.whitespace:
        m_res += 1
    elif symbol not in string.whitespace and m_res != 0:
        res = max(m_res, res)
        m_res = 0

print(res)
