"""Tu tarea es escribir un programa que tome una tupla de números, encuentre el segundo número más grande 
e imprima ese número, la tupla es --numbers = (10, 5, 8, 20, 15)--"""
numbers = (10, 5, 8, 20, 15)
list1 = list(numbers)
list1.sort()
print(f'The secund number more big is: {list1[3]}')


"""for i in list1:
maximo = max(numbers)
print(maximo)"""
   