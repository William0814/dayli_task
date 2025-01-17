"""Tu tarea de hoy es sencilla: debes crear un programa que tome una lista de especies de árboles
 que se encuentran en un bosque y cuente cuántas veces aparece cada especie."""
from collections import Counter

trees = ["oak", "pine", "maple", "oak", "birch", "pine", "oak"]
counts = {}

for tree in trees:
    if tree in counts:
        counts[tree] +=1
    else:
        counts[tree] =1

for tree, count in counts.items():
    print(f"{tree}:{count}")

    