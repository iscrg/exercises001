'''
Задание 4.
Определите какой символ встречается ровно три раза в тексте. Гарантируется, что символ
с такой частотой встречаемости только один.
'''

text = input()
letters = {}

for symbol in text:
    if symbol not in letters.keys():
        letters[symbol] = 1
    else:
        letters[symbol] += 1

idx = list(letters.values()).index(3)
print(list(letters.keys())[idx])
