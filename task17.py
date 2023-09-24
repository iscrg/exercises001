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
        close = exp.index(')')
        rev_exp = exp[:close]
        po_exp = ''

        for l in rev_exp[::-1]:
            if l != '(':
                po_exp += l
            else:
                break

        return po_exp[::-1]

    def __small_calculate(self, exp):
        exp = exp.split

    def __calculate(self, exp):

        exp = exp.split(['+', '-', '*', '/'])
        print(exp)\

    def calc(self):
        exp = self.__putout(self.__expension)
        self.__calculate(exp)

    def test(self):
        string = "GeeksForGeeks, | is an-awesome! website"
        delimiters = [",", "|", ";"]

        for delimiter in delimiters:
            string = " ".join(string.split(delimiter))

        result = string.split()

        print(result)

m = Calc('2+(10+10*12)')
m.test()
#m.calc()