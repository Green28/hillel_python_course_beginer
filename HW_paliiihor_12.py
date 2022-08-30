import string


"""Задача 1 10 баллов:
Написать 3 примера генераторных функций с различными последовательностями."""


def generator1():
    print("HW 2,3")
    yield "Monday"
    print("HW 4,7")
    yield "Tuesday"
    print("HW  exercises 123,7")
    yield "Wednesday"
    print("HW Free")
    yield "Thursday "
    print("HW Free")
    yield "Friday "
    print("HW Free")
    yield "Saturday"
    print("HW Free")
    yield "Sunday"


g1 = generator1()
try:
    print(next(g1))
    print(next(g1))
    print(next(g1))
    print(next(g1))
    print(next(g1))
    print(next(g1))
    print(next(g1))
    print(next(g1))
except StopIteration as s:
    print(s, "Week is finished")


def generator2():
    a = 0
    while a != 10:
        yield a + 1
        a += 1


g2 = generator2()
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))

g3 = (x for x in range(1, 10))
print(next(g3))
print(next(g3))
print(next(g3))
print(next(g3))

"""Задача 2 10 баллов:
Написать свою реализацию функции reduce() с описанием ее работы в однострочных и многострочных комментариях.
def my_reduce(): моя реализация. (постарайтесь по памяти реализовать.)"""


def my_reduce(function, iterable, initializer=None):
    it = iter(iterable)  # Перетворюєм ітерабельний об'єкт в ітератор
    if initializer is None:  # Якщо initializer відсутній
        value = next(it)  # Бере перший об'єкт value запускаєм ітератор
    else:
        value = initializer  # #Якщо initializer присутній то перезначаем його і бере його як перший обʼєкт
    for element in it:  # Перебирає елементи ітератора
        value = function(value, element)  # Перезначає value викликом атрибутної функції , та приймає в аргумент value
        # ,і element .
    return value


def funk_reduce(a, b):
    return (a + b) ** b


progression = my_reduce(funk_reduce, (1, 2, 3, 4, 5, 6))
print(progression)

factor_six = (1, 2, 3, 4, 5, 6)
factor = my_reduce(lambda a, b: a * b, factor_six)
print(factor)

user = my_reduce(lambda a, b: a.upper() + b, ("p", "a", "l", "i", "i"), "ihor ")
print(user)

"""Задача 3 30 баллов:
Написать функцию которая с помощью assert будет тестировать ваш самопистный reduce"""


def funk_password(value: str) -> str:
    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = lowers.upper()
    if len(value) < 8:
        return "Too Weak"
    if all(e in digits for e in value) or all(e in lowers for e in value) or all(e in uppers for e in value):
        return "Weak"
    if any(e in digits for e in value) and any(e in lowers for e in value) and any(e in uppers for e in value):
        return "Very Good"
    if (any(e in digits for e in value) and any(e in lowers for e in value)) or (any(e in lowers for e in value) and
                                                                                 any(e in uppers for e in value)) or (
            any(e in digits for e in value) and
            any(e in uppers for e in value)):
        return "Good"


if __name__ == '__main__':
    assert funk_password('') == "Too Weak"
    assert funk_password('1234567') == "Too Weak"
    assert funk_password('QWdafe') == "Too Weak"
    assert funk_password('qwe12') == "Too Weak"
    assert funk_password('QWERTYU') == "Too Weak"
    assert funk_password('123456789') == "Weak"
    assert funk_password('asdfghjkl') == "Weak"
    assert funk_password('ASDFGHJKL') == "Weak"
    assert funk_password('qddffdgdgfgd') == "Weak"
    assert funk_password('1234qwer') == "Good"
    assert funk_password('qwer1234') == "Good"
    assert funk_password('12QWqweuj') == "Very Good"
    assert funk_password('poIU123JL') == "Very Good"

"""**Задача 4. 30 баллов:** 
Збудувати класс з методом котрий повертає всі атрибути єкземпляра класса.
В конструкторі __init__ вашого класу зробити довільну реалізацію.
"""


class Human:
    def __init__(self, age, gender, color, special=None):
        self.age = age
        self.gender = gender
        self.color = color
        self.spesial = special

    def get(self):
        return self.__dict__


adam = Human(25, 'male', 'white', 'protect')
eva = Human(23, 'female', 'black', 'cook')
print(eva.get())
print(adam.get())

