"""Su tarea es escribir un programa que limpie los datos eliminando los espacios
adicionales, convirtiendo todos los nombres a mayúsculas y minúsculas (por ejemplo, Alice)
y eliminando los duplicados.
Por último, muestre la lista limpia en orden alfabético."""

messy_names = ["  alice ", "Bob", " charlie", "Alice", "BOB ", "eve  ", " Eve", "eve"]

# Eliminar espacios adicionales
clean_names = [name.strip() for name in messy_names]

# Convertir a mayúsculas y minúsculas
clean_names = [name.upper() for name in clean_names]

# Eliminar duplicados
clean_names = list(set(clean_names))

# Mostrar la lista limpia en orden alfabético
clean_names.sort()
print('Cleaned and Sorted Name: ')
for name in clean_names:
    print(f'{name}')