from random import randint

"1)без return c pass or ..."

def function_simple1():
    pass


def function_simple2(some: str = "Hi anywere"):
    print(some)
    ...


"2) сделать 5 различных функций на свое усмотрение."


def function1(name_user: str):  # аналог гри орел і рішка
    rand_int: int = randint(1, 100)
    if rand_int % 2 == 0:
        return print(f"{name_user} your side is Eagle")
    else:
        return print(f"{name_user} your side is Tails")


def function2(age_user: int):  # для провірки віку
    if age_user >= 18:
        return print('Pass')


def function3(pocket_money: int, earned: int, spent: int) -> int:  # для підрахунку залишку грошей
    return (pocket_money + earned) - spent


def function4(num: int) -> int:  # повертає плюсове число
    if num >= 0:
        return num
    else:
        return -num


def function5(name: str, age: int):  # перевіряє на валідність
    if age > 120 or age < 1:
        return print("Invalid age")
    print(f"Name: {name}  Age: {age}")


function_simple1()
function_simple2()
function1("Ihor")
function2(18)
print(function3(23, 42, 22))
print(function4(-323))
function5('Ihor', 30)
