numbers = [3, 1, 2, 3, 4, 1, 5, 2]
new_lista = []
for i in numbers:
    if i not in new_lista:
        new_lista.append(i)
new_lista.sort()
print(new_lista)