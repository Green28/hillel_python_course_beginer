"""1) написать функцию которая в качестве аргумента принимает размер стороны квадрата, а возвращает кортеж в котором лежат три значения:
    a)периметр квадрата
    b)диагональ квадрата
    c)площадь квадрата
"""


# x: int = int(input("x= "))


def funk_value(x_value: int) -> tuple:
    perimeter = x_value * 4
    diagonal = x_value * (2 ** 0.5)
    area = x_value * x_value
    return perimeter, diagonal, area


print(funk_value(7))

"""2) написать функцию которая принимает в качестве аргумента номер месяца, в возвращает строку - время года, этого
месяца
"""


def seasons(x: int) -> str:
    seasons_true = ""
    if x in [12, 1, 2]:
        seasons_true = 'winter'
    elif x in [3, 4, 5]:
        seasons_true = 'spring'
    elif x in [6, 7, 8]:
        seasons_true = 'summer'
    else:
        seasons_true = 'autumn'
    return seasons_true


print(seasons(9))

"""3) написать функцию, которая принимает в качестве аргументов два списка, а возвращает список, состоящий из элементов
этих двух списков, при чем первый элемент списка - первый элемент первого аргумента, второй элемент списка - первый 
элемент второго списка, третий элемент - второй элемент первого списка, четвертый - второй элемент второго аргумента
 и т.д.
т.е для аргументов [1, 2, 3] и [11, 22, 33] функция должна вернуть [1, 11, 2, 22, 3, 33].
Будет плюсом использование генераторов последовательностей для решения этой задачи."""

list1 = [1, 2, 3]
list2 = [11, 22, 33]


def spiski2v1(list1: list, list2: list) -> list:
    list3 = [[list1[i], list2[i]] for i in range(len(list1))]
    list3 = [j for i in list3 for j in i]
    return list3


print(spiski2v1(list1, list2))

"""
4) Написать функцию которая принимает в качестве аргумента строку, и возвращает object True, если строка является полиндромом и object False если нет."""


def polidrom(x: str) -> str:
    if x.lower() == x.lower()[::-1]:
        return "Object True"
    return "Object False"


print(polidrom('anna'))
