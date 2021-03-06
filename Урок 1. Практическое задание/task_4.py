"""
Задание 4. Написать программу, которая генерирует в указанных пользователем границах:
    случайное целое число;
    случайное вещественное число;
    случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

Подсказка:
Нужно обойтись без ф-ций randint() и uniform()
Использование этих ф-ций = задание не засчитывается

Функцию random() использовать можно
Опирайтесь на пример к уроку
"""
from random import random

left_int = int(input('введите минимальное целое число: '))
right_int = int(input('введите максимальное целое число'))
if left_int != right_int:
    rand_int = int(random() * (right_int - left_int + 1)) + left_int
    print(f'случайное целое число в заданном диапазоне {rand_int}')
else:
    print('Вы ввели одинаковые числа!')

left = float(input('введите минимальное вещественное число: '))
right = float(input('введите максимальное вещественное число: '))
if left != right:
    rand = random() * (right - left) + left
    print(f'случайное вещественное число в заданном диапазоне {rand}')
else:
    print('Вы ввели одинаковые числа!')
