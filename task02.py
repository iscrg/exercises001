'''
Задание 2.
Дан текст. Необходимо определить максимальное количество последовательных одинаковых символов в нём.
'''

text = input()
res = -1
m_res = 1

for i in range(1, len(text)):
    if text[i-1] == text[i]:
        m_res += 1

    elif text[i-1] != text[i] and m_res != 1:
        res = max(res, m_res)
        m_res = 1

print(res)
