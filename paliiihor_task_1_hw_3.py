""" Задача 1 на 10 балов
    1.Спросить у пользователя год рождения.
    2.Спомощью if -elif-else
     a)Проверить встроенным строковым методом, состоит ли возраст из числа или текста.
     b)Если текст то по попросить ввести число.
     c)Если 21 год вывести “You should visit Holland.”
     d)Если больше 21 вывести “You should visit Vietnam.”
     e)Все остальные варианты. Вывести “Travell everywhere”"""

data_user = input(" Еnter the year of birth: \t")
data_today: int = 2022
if data_user.isdigit():
    age_user = data_today - int(data_user)
    if age_user == 21:
        print("You should visit Holland.")
    elif age_user > 21:
        print("You should visit Vietnam.")
    else:
        print("Travell everywhere")
else:
    print("Incorrect, write a number")

""" Не використовував age: int = int(input()), так як не спрацьовує метод .digit , і якщо намагатись вписати слова або
 літери , при age: int = int(input()), вилітає помилка невірного ввода типа данних, а нам потрібно дати можливість на 
 введення слів або літер, тому якось так."""
