n: int =  int(input("n: "))
k: int =  int(input("k: "))
list_1 = list(range(1, n + 1))

while len(list_1) > 1:
    count1 = 0
    a = True
    while a == True:
        for i in list_1:
            count1 += 1
            if count1 == k:
                index_kil = list_1.index(i)
                list_1.remove(list_1[index_kil])
                for j in list_1[:index_kil]:
                    list_1.append(j)
                list_1[:index_kil] = ""
                a = False
                break
print(list_1)
