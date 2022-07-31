ex: list = ['add', 'clear', 'copy', 'difference', 'discard', 'intersection', 'isdisjoint', 'issubset', 'issuperset',
            'pop',
            'remove', 'union', 'update']
ex2: list = ['bread', 'milk', 'water']
ex3: list = [1, 2, 3, 3, 3, 2, 4, 5, 1, 2, 3, 4, 5]
ex4: list = ['add', 'clear', 'copy', 'difference', 'discard', 'intersection', 'isdisjoint', 'issubset', 'issuperset',
             'pop',
             'remove', 'union', 'update', 'add', 'clear', 'copy', 'difference', 'discard', 'intersection', 'isdisjoint',
             'issubset']
print("1) 5 примеров list comprehension\n")
a_list: list = [i for i in range(10)]
b_list: list = [i ** i for i in range(10, 1, -1)]
c_list: list = [i for i in ex[::-2]]
d_list: list = [i.upper() for i in ex]
e_list: list = [i[::-1] for i in ex]
print(a_list, b_list, c_list, d_list, e_list, sep="\n")

print("2) 5 примеров with DICT comprehension\n")
a_dict: dict = {i: "method_list" for i in ex}
b_dict: dict = {i: i ** i for i in range(10)}  # цікаво ,що  0**0 = 1, це як так?)
c_dict: dict = {i.upper(): i.lower() for i in ex if isinstance(i, str)}
d_dict: dict = {i: 'None' for i in ex}
e_dict: dict = {i: [j for j in ex2] for i in ex}
print(a_dict, b_dict, c_dict, d_dict, e_dict, sep='\n')

print("3) 5 примеров с set comprehensions\n")
a_set: set = {i for i in ex3}
b_set: set = {i for i in ex4}
c_set: set = {i * 2 for i in ex3}
d_set: set = {i.upper() for i in ex4}
e_set: set = {ex3[i] for i in range(len(ex3))}
print(a_set, b_set, c_set, d_set, e_set, sep="\n")
