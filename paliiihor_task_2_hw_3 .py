"""Задача 2 на 25 балов
    1.Приветствует пользователя в произвольном виде:
        a)Принимает на ввод его никнейм, пол, возраст. 
    2.Если никнейм содержит admin, выводит: "Привет, повелитель!", не прекращая работу.
    3.Если возраст больше 10 и меньше 14 и пол М или больше 30 и пол М: Выводит "Советую Вам посмотреть "StarWars" или
    'Мандалорец'"
    4.Если возраст больше 22 и меньше 32 и пол Ж: Рекомендация "Советую Вам посмотреть "Трансформеры""
    5.Если возраст меньше 16 и пол Ж: Рекомендация "Советую Вам посмотреть "Инсургент""
    6.Если никнейм 'Женя': Рекомендация "Советую Вам посмотреть 'TENET'"
    7.Если возраст до 11 и пол М: Рекомендация "Советую Вам посмотреть "TMNT""
    8.Если никнейм Guido: Кроме рекомендации, выводит 'Огромное спасибо!'"""

print("Hi ", " and ", " welcome", sep="❤", end=" 😊\n")
user_name: str = input("Your nickname :").lower()
gender: str = input("Your gender,write male or female: ").lower()
age: int = int(input("Your age: "))
    
if "admin" in user_name:
    print("Привет, повелитель!", end="😎\n")
elif "женя" in user_name:
    print(f"Советую {user_name.capitalize()} посмотреть 'TENET'", end="😩\n")
elif "guido" in user_name:
    print("Огромное спасибо!", end="😎\n")
    
if "male" in gender:
    if age < 11:
        print(f"Советую {user_name.capitalize()} посмотреть \"TMNT\"", end="😏\n")
    elif 10 < age < 14 or age > 30:
        print(f"Советую {user_name.capitalize()} посмотреть \"StarWars\" или \"Мандалорец\"", end="⭐\n")
        
if "female" in gender:
    if age < 16:
        print(f"Советую {user_name.capitalize()} посмотреть \"Инсургент\"", end="😩\n")
    elif 22 < age < 32:
        print(f"Советую {user_name.capitalize()} посмотреть \"Трансформеры\"", end="😩\n")
        
