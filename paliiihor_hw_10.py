"""Задача 1. 50 баллов
Видосик по Замыканиям просмотреть
и повторить за автором.
мне скинуть файлик с повтором или своим примером"""


def one():
    x = ['one', 'two']

    def inner():
        print(x)
        print(id(x))

    return inner


a = one()
o = a.__closure__[0].cell_contents
o.append('three')
a()
"""Задача 1. 50 баллов
Написать функцию которая будет добавлять код страны
к номеру телефона с помощью замыкания
внешний вид вызова функции.
my_number = user_telephone('+044')
my_number('838372893')
+044838372893 результат."""


def add_num(x):
    def user_num(y):
        return x + y

    return user_num


my_number = add_num('+044')
print(my_number('838372893'))
