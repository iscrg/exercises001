'''
Задание 20.
Дано натуральное число не превосходящее 900 000 000. Напишите программу, которая
выводит на экран это число русскими словами.
'''

def skl(num, razr):
    if num == 1:
        if razr == 1:
            return ' тысяча '
        elif razr == 2:
            return ' миллион '
    elif num in [2, 3, 4]:
        if razr == 1:
            return ' тысячи '
        elif razr == 2:
            return ' миллиона '
    elif num in [5, 6, 7, 8, 9]:
        if razr == 1:
            return ' тысяч '
        elif razr == 2:
            return ' миллионов '

edin_for_thousand = [
    '',
    'одна',
    'две',
    'три',
    'четыре',
    'пять',
    'шесть',
    'семь',
    'восемь',
    'девять',
]

edin = [
    '',
    'один',
    'два',
    'три',
    'четыре',
    'пять',
    'шесть',
    'семь',
    'восемь',
    'девять',
]

teen = [
    'десять',
    'одиннадцать',
    'двенадцать',
    'тринадцать',
    'четырнадцать',
    'пятнадцать',
    'шестнадцать',
    'семнадцать',
    'восемнадцать',
    'девятнадцать',
]

tee = [
    '',
    '',
    'двадцать',
    'тридцать',
    'сорок',
    'пятьдесят',
    'шестьдесят',
    'семьдесят',
    'восемьдесят',
    'девяноста'
]

hundred = [
    '-',
    'сто',
    'двести',
    'триста',
    'четыреста',
    'пятьсот',
    'шестьсот',
    'семьсот',
    'восемьсот',
    'девятьсот',
]

num = int(input('Введите число:'))
num_list = list(str(num))
res = ''

#900 000 000
ln = len(num_list)
for i in range(ln):
    rsn = ln - i

    if rsn == 1:
        if len(num_list) > 1:
            if num_list[-2] != '1':
                res += edin[int(num_list[i])] + ' '
            elif num_list[-2] == '0':
                pass
            else:
                res += teen[int(num_list[i])] + ' '
        else:
            if num_list[-2] == '0':
                pass
            else:
                res += edin[int(num_list[i])-1] + ' '

    elif rsn in [2, 5, 8]:
        if num_list[-rsn] != '1':
            res += tee[int(num_list[i])] + ' '
        elif num_list[-rsn] != '0':
            pass

    elif rsn in [3, 6, 9]:
        if num_list[-rsn] != '0':
            res += hundred[int(num_list[i])] + ' '

    elif rsn == 4:
        if len(num_list) > 4:
            if num_list[-5] != '1':
                res += edin[int(num_list[i])] + skl(int(num_list[i]), 1)
            else:
                res += teen[int(num_list[i])] + skl(int(num_list[i]), 1)

        else:
            res += edin[int(num_list[i]) - 1] + skl(int(num_list[i]), 1)

    elif rsn == 7:
        if len(num_list) > 7:
            if num_list[-8] != '1':
                res += edin[int(num_list[i])] + skl(int(num_list[i]), 2)
            else:
                res += teen[int(num_list[i])] + skl(int(num_list[i]), 2)

        else:
            res += edin[int(num_list[i])] + skl(int(num_list[i]), 2)


print(res)