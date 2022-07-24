"""Задача 1. 10 баллов
пользователь вводит пароль первый раз система запоминает и просит повторить пароль проверяет его если нет то просит
 повторить. А если совпал то сообщение."""

password: str = input("Fill up password: ")
while True:
    if password == input("Fill up password again: "):
        print("Correct password\n")
        break
    else:
        continue

"""Задача_2. 5 баллов
Дан список с повторяющимися значениями необходимо из него удалить все определенные значения используя while цикл.
Входные данные: ['bear', 'milk', 'eg', 'eg', 'eg', 'eg'] удалить все eg
Результат: ['bear', 'milk']"""

example_list2: list = ['bear', 'milk', 'eg', 'eg', 'eg', 'eg']
print(example_list2)
del_value: str = input('Fill up value for delete: ')
while True:
    if del_value in example_list2:
        example_list2.remove(del_value)
    else:
        print(f" {example_list2 = }\n")
        break

"""Задача_3. 10 баллов
Тема while and else
дан список произвольный с int нужно вывести "all numbers are even" если все четные и NO если нет
Пример входных данных: [11, 23, 65, 44, 76, 533]
Результат: NO
Пример входных данных: [12, 22, 66, 44, 76, 534]
Результат: all numbers are even"""

exemple_list3: list = [24, 24, 64, 44, 75, 530]
count1: int = 0
for i in exemple_list3:
    if i % 2 != 0:
        print("NO\n")
        break
    else:
        count1 += 1
if count1 == len(exemple_list3):
    print("All numbers are even\n")

"""Задача_4 25 баллов
написать программу которая будет создавать список методов из доступных методов питон объектов. Под 
доступнымиподразумевается методы без подчеркиваний. Фунции dir()
т.е для объекта set должен быть список методов
['add', 'clear', 'copy', 'difference', 'discard', 'intersection', 'isdisjoint', 'issubset','issuperset', 'pop',
'remove','union', 'update']
"""
exemple_list4: list = (dir(set))
list_simple_methods: list = []
for i in exemple_list4:
    for j in i:
        if j.isalpha():
            list_simple_methods.append(i)
            break
        else:
            break
print(list_simple_methods)

"""Задача_6 5 балллов
Написать примеры всех методов из set объекта.
Пример
set1 = {1,2,3}
# add
set1.add(4)
# update
set1.update([2,3,4,5])"""

set_1 = {1, 2, 3, 4}
set_2 = {2, 4, 6, 3}
# clear - видаляє все
set_1.clear()

# add - добавляє тільки один елемент
set_1.add(8)

# update - додає перечень обʼєктів
set_2.update([1, 2, 3, 4, 5, 6])
set_1.update([5, 6, 7, 8, 9, 10])
set_1 |= set_2

# discard - видаляє обʼєкт, якщо такого нема помилку не викликає
set_2.discard(6)

# remove - видаляє обʼєкт, якщо такого нема помилку  викликає
set_2.remove(2)

# pop - видаляє рандомний обʼєкт, який присвоюється в нову перемінну
a = set_2.pop()

# intersection - ті обʼєкти які пересікаються в обидвах множинах
set_1.intersection(set_2)
sec = set_1 & set_2
set_1 &= set_2

# union - обʼєднання множин
set_1.union(set_2)
un = set_1 | set_2

# difference - віднімання однієї множини і іншої, однакових обʼєктів
set_1.difference(set_2)
dif = set_1 - set_2

# copy - робить копію
copy_set1 = set_1.copy()

# isdisjoint - повертае TRUE , якщо спільних елментів нема
set_1.isdisjoint(set_2)

# issubset - повертае TRUE , якщо set_1 повністю лежить у set_2
set_1.issubset(set_2)
s_s1: bool = set_1 <= set_2
s_s2: bool = set_1 < set_2

# issuperset - повертае TRUE , якщо set_2 повністю лежить у set_1
set_1.issuperset(set_2)
s_s3: bool = set_1 >= set_2
s_s4: bool = set_1 > set_2

"""
Задача_7 25 баллов
Тема frozenset.
создать  frozenset (Прочитать что это  где вам удобно)
необходимо посчитать длинну этой коллекции без помощи функции len().
И вывести ее в косноль."""

# перемінну list_simple_methods взяв з 4-го завдання
f_set: frozenset = frozenset(list_simple_methods)
len_f_set: int = 0
for i in f_set:
    len_f_set += 1
print(len_f_set)
