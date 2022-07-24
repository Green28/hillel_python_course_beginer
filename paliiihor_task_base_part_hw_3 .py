"""1_Создать файл (модуль) с примерами всех методов строк."""
exemple_list: list = ['23', '245', '33']
exemple_str: str = "Hello my dear friend"
    
#  join
print(f"\n**join** \n{'$'.join(exemple_list)}")
#   upper,lower, swapcase, capitalize

print(
    "\n**upper,lower, swapcase, capitalize**"
    f"\n{exemple_str.upper()} \n{exemple_str.lower()} \n{exemple_str.swapcase()} \n{exemple_str.capitalize()} ")
#   count
print(f"\n**count** \n{exemple_str.count('e')}")

#   find
print(f"\n**find** \n{exemple_str.find('my')} \n{exemple_str[exemple_str.find('my')]} "
      f"\n{exemple_str[exemple_str.find('my')::]}")

#   replace
print(f"\n**replace** \n{exemple_str.replace('l', '&', 1)}")

#   strip
print(f"\n**strip** \n{exemple_str.strip('Hello,friend')}")

#   slit
print(f"\n**split** \n{exemple_str.split()}")

"""2_Создать по 3 варинта  всех уже изученных  объектов в Пайтоне."""

# str
ex_str1: str = "Whatever your specialty may be, we're here to guide you along the way."
ex_str2: str = "Hello world of python"
ex_str3: str = "User_32423"

# int
ex_int1: int = -23123123
ex_int2: int = 28
ex_int3: float = 2.3232301

# list
ex_list1: list = [1, 2, 3, 4, 5]
ex_list2: list = [1, 'a', 2, 'b', 3, 'c']
ex_list3: list = [1, 'a', 2, [1, 4, 5], ('ip', 'id', 'ios'), {'name': 'London'}]

# dict
ex_dict1: dict = {'user': 'Ivan', 'password': 'qwerty'}
ex_dict2: dict = {'1': '2', '23': '323'}
ex_dict3: dict = {'ex_dict1': {'user': 'Ivan', 'password': 'qwerty'},
                  'ex_dict2': {'1': '2', '23': '323'}}

# tuple
ex_tuple1: tuple = (1, 2, 3, 4, 5)
ex_tuple2: tuple = (1, 'a', 2, 'b', 3, 'c')
ex_tuple3: tuple = (1, 'a', 2, [1, 4, 5], ('ip', 'id', 'ios'), {'name': 'London'})

"""3_Написать 3 примера использования max(), min()."""
print(f"\nmin and max ex_list1: \n{min(ex_list1), max(ex_list1)}")
print(f"\nmin (1, 2, 3, 4, 5): \n{min(1, 2, 3, 4, 5)}")
print(f"\nmax (1, 2, 3, 4, 5): \n{max(1, 2, 3, 4, 5)}\n")

"""5_Написать 3 примера различных с оператором in."""
print("your" in "Whatever your specialty may be, we're here to guide you along the way.")
print("Hi" in "Whatever your specialty may be, we're here to guide you along the way.")
print("may be" in ex_str1)

"""6_написать 3 примера условия if elif else"""
print("\nTask1")

age: int = 19
if 75 > age >= 18:
    print("Pass free")
elif age >= 75:
    print("You cant pass")
else:
    print("So young")
print("Task2")
car_model: str = "BMW"

if car_model == "BMW" or "Mersedes":
    print("You are lucky , it's premium car")
elif car_model == "VAZ" or "UAZ" or "Moskvich":
    print("You are not lucky guy")
else:
    print("You are lucky but not like owners BMW or Mersedes")
print("\nTask3")
friends: int = 4
    
if 0 < friends <= 4:
    print("Its OK")
elif friends > 4:
    print("You are happy")
else:
    print("Alone")
