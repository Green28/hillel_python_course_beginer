"""Задача 1. 10 баллов
тема Срезы и условие if.
написать программку которая будет состоять из первых двух и последних символов предоставленной строки.
Если длинна строки меньше двух символов напечатать строку типа.
'Ваша строка слишком короткая - СТРОКА ' . Через метод форматирования строк с %.
Входная строка : 'Hillel school'
Результат1 : 'Hiol'
или
Результат2 : 'Ваша строка слишком короткая - и ваша строка'
"""
print("Задача 1")
cut_string: str = input("Enter a string of at: ")
if len(cut_string) < 2:
    print("Your string is too short - %s" % cut_string)
else:
    print(f"{cut_string[:2]}{cut_string[-2:]}")

"""Задача 2. 15 баллов
Тема Dict
Написать программу, которая подсчитывает количество символов в строке
и формирует dict в котором key = буква, value= количество их в слове:
Входная строка : 'Hillel school'
Результат :  {'H': 1, 'i': 1, 'l': 3, 'e': 1, ' ': 1, 's': 1, 'c': 1, 'h': 1, 'o': 2}
"""

print("Задача 2")
b: list = list('Hillel school')
voc: dict = {}
for i in b:
    voc[i] = int(b.count(i))
print(voc)

"""Задача 3. 15 баллов
Тема list и его методы. Строки и срезы.
Программа принимает список продуктов и принтит самое длинное слово и его длинну.
Ипользовать ''.format() для вывода строки и аргументов.
Входные данные: ['bread', 'milk', 'kolbasa']
Результат: 'Самое длинное название продукта kolbasa длинна 7 символов'
"""
print("Задача 3")
products: list = ['bread', 'milk', 'kolbasa', 'pechenushki']
long_word = ""
for i in products:
    if len(i) > len(long_word):
        long_word = i
print("The longest product name {0} is {1} letters.".format(long_word, len(long_word)))

"""Задача 4. 5 баллов
Пользователь водит свое имя.
Возвращается тектс в БОЛЬШОМ и маленьком регистре. Использовать ' '.format().
Для вставки аргументов в текст.
Входные данные: Apollo
Результат: APPOLLO apollo
"""
print("Задача 4")
name: str = input("Your name: ")
print("{0} {1}".format(name.upper(), name.lower()))

"""Задача 5. 15 баллов.
Тема приведение типов. Работа со списком. Расчленение строки и ее соединение.
Пользователь вводит через запятую последовательность слов например цвета или продукты.
Программа возвращает уникальные слова отсортированные по алфавиту.
Входные данные: red, white, black, red, green, black
Результат: black, green, red, white"""

print("Задача 5")
colors1: list = input("Write colors: ").split(", ")
colors2: list = []
for i in colors1:
    if i not in colors2:
        colors2.append(i)
print(*sorted(colors2), sep=", ")

"""Задача 6. 5 баллов
Тема Кортеж и работа сним.
Удалить элемент из кортежа.
Входные данные: (1, 2, 3)
Результат: (1, 2)Задача 6. 5 баллов
Тема Кортеж и работа сним.
Удалить элемент из кортежа.
Входные данные: (1, 2, 3)
Результат: (1, 2)
"""

print("Задача 6")
d: tuple = (1, 2, 3)
d: list = list(d)
d.remove(d[-1])
d: tuple = tuple(d)
print(d)

"""Задача 7. 10 баллов
Написать программу которая данный список кортежей переведет в список списков
Входные данные: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
Результат: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]
"""

print("Задача 7")
e1: list = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
for i in range(len(e1)):
    val = list(e1.pop())
    e1.insert(i, val)
print(e1[::-1])

"""
Задача 8. 15 баллов
Тема range
Есть последовательность от -99 до 99. Ее шаг 3. т.е. [-99, -96]
напечатать все элементы последовательности которые делятся на 3 без остатка.
напечатать в формате 'это <<ЧИСЛО>> делится без остатка на 3'
использовать метод редактирования строки f' строки'"""

print("Задача 8")
for i in range(-99, 100, 3):
    print(f"It's number {i} is evenly divisible by 3")

"""
Задача 9. 10 баллов
Тема Листы
Даны два списка элементов если хоть один елемент совпадает отпринтить True.
print(Тrue) не слово! а объект подставить."""

print("Задача 9")
a: list = ['bread', 'milk', 'kolbasa']
b: list = ['potatos', 'candy', 'milk', 'kolbasa']
c: list = []
if len(a) > len(b):
    for i in a:
        if i in b:
            c.append(i)
elif len(b) > len(a):
    for i in b:
        if i in a:
            c.append(i)
if len(c) == 0:
    print("lists don't match")
else:
    print(*c, sep=", ", end=".")
