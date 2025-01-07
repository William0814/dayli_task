list1 = [5, 3, 8, 6, 3]
list2 = [7, 2, 5, 9, 8]
new_list = []

for i1, i2 in zip(list1, list2):
    if i1 not in new_list:
        new_list.append(i1)
    if i2 not in new_list:
        new_list.append(i2)

new_list.sort()
print('The new list combine and Sort: ', new_list)
