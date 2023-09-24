'''
Задание 17.
Строка содержит арифметическое выражение, в котором используются круглые скобки,
в том числе вложенные. Напишите программу, которая вычисляет значение этого выражения.
Функцию eval() не использовать.
'''


class Calc:
    def __init__(self, exp):
        self.__expension = exp

    def __putout(self, exp):
        open = exp.rindex('(')+1
        close = exp[open:].index(')') + open
        po_exp = exp[open:close]
        return po_exp

    def __small_calculate(self, exp):
        if exp[0] == '-':
            exp = f'0{exp}'

        exp_num = exp
        exp_symbols = ''
        symbols = ['^', '*', '/', '+', '-']

        for symbol in symbols:
            exp_num = " ".join(exp_num.split(symbol))

        exp_num = exp_num.split()

        for e in exp:
            if e in symbols:
                exp_symbols += e
        exp_symbols = list(exp_symbols)

        for symbol in symbols:
            while symbol in exp_symbols:
                indx = exp_symbols.index(symbol)

                if symbol == '^':
                    res = float(exp_num[indx]) ** float(exp_num[indx + 1])
                elif symbol == '*':
                    res = float(exp_num[indx]) * float(exp_num[indx + 1])
                elif symbol == '/':
                    res = float(exp_num[indx]) / float(exp_num[indx + 1])
                elif symbol == '+':
                    res = float(exp_num[indx]) + float(exp_num[indx + 1])
                elif symbol == '-':
                    res = float(exp_num[indx]) - float(exp_num[indx + 1])

                del exp_symbols[indx]
                del exp_num[indx+1]
                exp_num[indx] = res

        return exp_num[0]

    def __calculate(self, exp):
        pass

    def calc(self):
        while '(' in self.__expension:
            exp = self.__putout(self.__expension)
            res = self.__small_calculate(exp)
            exp = f'({exp})'
            self.__expension = self.__expension.replace(str(exp), str(res))

        return self.__small_calculate(self.__expension)


m = Calc(input('Введите выражение без пробелов:'))
print(m.calc())
