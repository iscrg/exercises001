'''
Задание 5.
Даны три строки. Выведите на экран только те символы, которые есть лишь в одной из этих трёх строк.
'''

strs = [input(), input(), input()]
symb_str = [set(), set(), set()]
res = []

for i in range(3):
    for symbol in strs[i]:
        symb_str[i].add(symbol)

for i in range(3):
    a = [0, 1, 2]
    a.remove(i)
    for symbol in symb_str[i]:
        if (symbol not in symb_str[a[0]] and
                symbol not in symb_str[a[1]]):
            res.append(symbol)

print(res)
