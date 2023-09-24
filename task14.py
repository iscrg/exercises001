'''
Задание 14.
В телевизионной игре "Поле чудес", игрок отгадывает слово. Напишите программу, которая спрашивает
у ведущего подсказку и загаданное слово. Далее, программа удаляет информацию с экрана, выполняя
вывод 25 пустых строк. После этого, выводится подсказка и слово, где вместо букв, выводятся
символы "*". Игрок должен с десяти попыток отгадать слово по буквам. После каждого хода выводится
слово, где неназванные буквы закрыты символом "*".  Отгаданные буквы выводятся на тех местах, где
они расположены. Каждый ход сопровождается вопросом "Буква или слово (0 - буква, 1 - слово)?".
В случае если слово отгадано верно, выводится сообщение "Победа!". Если слово названо неверно,
или закончились попытки, выводится сообщение "Проигрыш!".

Пример работы программы:
Ведущий вводит две строки: подсказку и загаданное слово.
Дикое животное.
тигр
Программа выводит 25 пустых строк и таким образом "скрывает" то, что написал ведущий.
Игрок пытается отгадать слово:
Дикое животное.
****
Буква или слово (0 - буква, 1 - слово)?0
a
****
Буква или слово (0 - буква, 1 - слово)?0
р
***р
Буква или слово (0 - буква, 1 - слово)?0
и
*и*р
Буква или слово (0 - буква, 1 - слово)?1
тигр
Победа!
'''


def game(prompt, word):
    encrypted_word = ['*'] * len(word)

    print('\n' * 25)
    print(f'Подсказка: {prompt}')

    for i in range(10):
        print(''.join(encrypted_word))

        choice = input('Буква или слово (0 - буква, 1 - слово)?')
        answer = input()
        if choice == '1':
            if answer == word:
                return True
            else:
                return False

        elif choice == '0':
            if answer in word:
                encrypted_word[word.index(answer)] = answer
            else:
                pass

        if ''.join(encrypted_word) == word:
            return True

    return False


prompt = input('Введите подсказку: ')
word = input('Введите слово: ')

print('\n' * 25)

g = game(prompt, word)
if g:
    print('Победа!')
else:
    print('Проигрыш!')