'''
Задание 16.
Дан текст. Проверить, правильно ли в нем расставлены круглые скобки (т. е.
находится ли справа от каждой открывающей скобки соответствующая ей закрывающая
скобка, а слева от каждой закрывающей — соответствующаяей закрывающая).
'''

'''
def analyser(txt):
    txt_modified = ''

    for x in txt:
        if x in ['(', ')']:
            txt_modified += x

    if txt_modified.count('(') == txt_modified.count(')'):
        for x in txt_modified:
            

txt = input()
'''


def check_brackets(txt):
    brackets = []

    for l in txt:
        if l == '(':
            brackets.append(l)

        elif l == ')':
            if not brackets:
                return False
            else:
                brackets.pop()

    return len(brackets) == 0


txt = input()

if check_brackets(txt):
    print("Верно")
else:
    print("Неверно")
