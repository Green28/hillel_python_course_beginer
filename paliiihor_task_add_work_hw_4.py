matr = [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']]
key: str = ''
# Малюєм пусту матрицю
print("Y")
count: int = 4
# Змінив послідовність ітерації , щоб співпадали координати як на малюнку
for i in matr[-1::-1]:
    print("--+---+---+---+---+---+")
    print(count, *i, sep=' | ', end=' |\n')
    count -= 1
print("--+---+---+---+---+---+")
print("    0   1   2   3   4   X")
# Запускаєм цикл
while key != '0':
    value = ""
    print("1) Сделать запись\n2) Получить значение по координатам\n3) Показать все ячейки\n"
          "4) Удалить значение по координатам\n0) Программа завершает работу.")
    key: str = input("Выбери действие: ")
    if key == '1':
        print("Введите значения от 0 - 4: ")
        x: int = int(input("x= "))
        y: int = int(input("y= "))
        value: str = input("value= ")
        if matr[y][x] == ' ':
            print(f"x:{x},y:{y} - ячейка не занята, идет запись")
            matr[y][x] = value
        else:
            print("Ячейка занята! Перезаписать?")
            choice: str = input("Ячейка занята! Перезаписать? \n1) Да.\n2) НЕТ!\nВыбери действие: ")
            if choice == '1':
                matr[y][x] = value
                print("Запись сделана!")
            elif choice == '2':
                continue
    elif key == '2':
        print("Введите значения от 0 - 4: ")
        x: int = int(input("x= "))
        y: int = int(input("y= "))
        if matr[y][x] == ' ':
            print("Пустая ячейка")
        else:
            print(f"value= {matr[y][x]}")
    elif key == '3':
        print("Y")
        count: int = 4
        for i in matr[-1::-1]:
            print("--+---+---+---+---+---+")
            print(count, *i, sep=' | ', end=' |\n')
            count -= 1
        print("--+---+---+---+---+---+")
        print("    0   1   2   3   4   X")
    elif key == '4':
        print("Введите значения от 0 - 4: ")
        x: int = int(input("x= "))
        y: int = int(input("y= "))
        matr[y][x] = ' '
        print("Запись удалена!")
# Все працює цікава задачка, дякую)
