'''
Задание 12.
Как известно, имя в языке Python может содержать только латинские символы, цифры
и знак подчеркивания "_". При этом, имя не может начинаться с цифры и не может быть
ключевым словом. Напишите программу, которая проверяет введенную строку, может ли
она быть именем в языке Python.
'''

import string

def check(text):
    dct = string.ascii_letters + string.digits + '_'
    fnc = [
        'abs',
        'aiter',
        'all',
        'anext',
        'any',
        'ascii',
        'bin',
        'bool',
        'breakpoint',
        'bytearray',
        'bytes',
    ]

    if text[0] not in string.digits:
        if text not in fnc:
            for letter in text:
                if letter in dct:
                    pass
                else:
                    return False
        else:
            return False
    else:
        return False

    return True


t = input()
print(check(t))