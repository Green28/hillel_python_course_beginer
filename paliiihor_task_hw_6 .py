"""Task 1. 5 points
сложить словари в один.
использовать for и dict methods.
"""

first = {1: 10, 2: 20}
second = {3: 30, 4: 40}
third = {5: 50, 6: 60}
fourth = {7: 70, 8: 80}
fifth = {9: 90, 10: 100}

list_dicts = [first, second, third, fourth, fifth]
dict_unit = {}
for list_dict in list_dicts:
    dict_unit.update(list_dict)
print(dict_unit)

"""Task 2. 10 points
1. Создать словарь с ключами от 11 до 20 включительно. Значения = квадраты ключей
Пример:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15:225}
"""

dict_1 = {}
for i in range(11, 21):
    dict_1.setdefault(i, i ** 2)
print(dict_1)

"""2. просуммировать все значения(values), делается в одну строку.(look build in functions)
"""

print(sum(dict_1.values()))

"""Task3. 5 points
отсортировать словарь по ключам
"""

dict_mix = dict(set(dict_1.items()))  # Міксанув старий словник
print(dict_mix)
print(dict(sorted(dict_mix.items())))

"""Task 4. 15
Удалить дубликаты из dictionary
пример
"""
before_dict = {'id1':
    {
        'name': 'Ruslan',
        'class': 1,
        'subjects': {'Math', 'Algorithms', 'English'}
    },
    'id2':
        {
            'name': 'Mark',
            'class': 2,
            'subjects': {'Geometry', 'Java', 'Cooking'}
        },
    'id3':
        {
            'name': 'Ruslan',
            'class': 1,
            'subjects': {'Math', 'Algorithms', 'English'}
        }
}
# 1 спосіб
names = []
after_dict=before_dict.copy()
for key,value in before_dict.items():
    if after_dict[key]['name'] not in names:
        names.append(after_dict[key]['name'])
    else:
        after_dict.pop(key)
print(after_dict)
# 2 спосіб
after_dict2 = before_dict.copy()
for key, value in before_dict.items():
    count = 0
    for key2, value2 in after_dict2.items():
        if value == value2:
            count += 1
    if count > 1:
        after_dict2.pop(key)
print(after_dict2)

"""After:
{'id1':
{
'name': 'Ruslan',
'class': 1,
'subjects' : {'Math', 'Algorithms', 'English'}
},
'id2':
{
'name': 'Mark',
'class': 2,
'subjects' : {'Geometry', 'Java', 'Cooking'}
}"""

"""Task 5. 10
Вернуть из dictionary все уникальные values.
Пример
Входные данные = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Результат = {'S001', 'S005', 'S007', 'S002', 'S009'}
Усложнение! +5 points
Вернуть ту же структуру.
После dictionary L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S005"}, {"V":"S009"},{"VIII":"S007"}]"""

list_dicts2 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S002"}, {"VII": "S005"}, {"V": "S009"},
               {"VIII": "S007"}]
uniq = []
L = list_dicts2.copy()
for i in list_dicts2:
    for key, value in i.items():
        if value not in uniq:
            uniq.append(value)
        else:
            L.remove(i)
print(L)

"""Task 6. 15 Посчитать общее количество наименований в списке. И только в списках.
Example:
shedule = {'monday': ['clean house', 'drive car', 'meet with freands'], 'thuesday': None, 'wednesday': ['manicure', 
'hammam', 'beer']}
Результат: 6"""

shedule = {'monday': ['clean house', 'drive car', 'meet with freands'], 'thuesday': None,
           'wednesday': ['manicure', 'hammam', 'beer']}
count = 0
for i, j in shedule.items():
    if isinstance(j, list):
        count += len(j)
print(count)

"""
Найти официальную документацию по Словарям и прикрепить ссылку к домашней работе 5 points
И попробовать прочитать ). Ось почитав, трохи еле буду ще)
https://docs.python.org/3/library/stdtypes.html#mapping-types-dict"""

"""Task 8 . 25 Points 
Познакомиться самостоятельно с термином Хеширование. 

Ознайомився ося на цьому порталі 
https://pythobyte.com/python-hash-function-09311/
"""