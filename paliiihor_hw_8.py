from datetime import datetime

"""1. С помощью рекурсии написать функцию которая будет подсчитывать сумму из списка чисел.
 ваша_функция([1, 2, 3, 4, 5, 6, 7, 8]) -> 36
 """
ls_1 = [1, 2, 3, 4, 5, 6, 7, 8]


def recurs(x: list) -> int:
    if len(x) == 1:
        return x[0]
    else:
        return x[0] + recurs(x[1:])


print(recurs(ls_1))

"""2. С помощью рекурсии написать функцию которая будет подсчитывать сумму из Вложенных списков чисел. 
ваша_функция([1, 2, [3, 4, [5, 6], 7], 8])->36"""

ls_2 = [1, 2, [3, 4, [5, 6], 7], 8]


def recurs2(x: list) -> list:
    lst = []
    for i in x:
        if isinstance(i, list):
            lst.extend(recurs2(i))
        else:
            lst.append(i)
    return lst  # Розпакував


new_list = recurs2(ls_2)  # Підрахунок сумми через пешру функцію
print(recurs(new_list))

"""3. Реализовать патерн декоратор в произвольной виде."""


def lower_text(function):
    def wrapper():
        answer = function().lower()
        return answer

    return wrapper


def counting_time(function):
    def wrapper():
        start = datetime.now()
        answer = function()
        print(datetime.now() - start)
        return answer

    return wrapper


def counting_letters(function):
    def wrapper():
        answer = (list(function()))
        for i in answer:
            if ' ' == i:
                answer.remove(i)
        return print(f'{len(answer)}\'elements for time')

    return wrapper


@counting_letters  # Кількість елементів надрукованих , без рахунку відступів
@lower_text  # Записує все в нижній регістр
@counting_time  # Пише час заякий було надруковано ім'я
def funk():
    a = input("Any text :  ")
    return a


funk()
