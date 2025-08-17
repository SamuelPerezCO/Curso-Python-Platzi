#Explicacion de chatgpt
# Una list comprehension en Python es una forma rápida y compacta de crear listas nuevas a partir de una secuencia (como otra lista, un rango o cualquier iterable), aplicando operaciones o condiciones en una sola línea

# En vez de usar un for tradicional, la comprensión de listas permite escribirlo de manera más clara.

# La forma general es:

# [expresión for elemento in iterable if condición]


# expresión → qué valor quieres agregar a la lista

# elemento → cada valor tomado del iterable

# iterable → la colección sobre la que se itera (lista, rango, etc.)

# if condición (opcional) → filtra qué elementos incluir

# ¿Quieres que te muestre ejemplos sencillos para entenderlo mejor?


squares = [x**2 for x in range(1,11)]
print("Cuadrados: " , squares)

celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) * 32 for temp in celsius]
print("Temperatura en F:" , fahrenheit)

#Numeros pares
evens = [x for x in range(1,21) if x % 2 == 0]
print(evens)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print(matrix)
print(transposed)

transposed = []
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)