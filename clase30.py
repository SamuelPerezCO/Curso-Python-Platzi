#Leer un archivo linea por linea
"""with open('cuento.txt', "r") as file:
    for lineas in file:
        print(lineas.strip())"""

#Leer todas las líneas en una lista
"""with open("cuento.txt" , "r") as file:
    lines = file.readlines()
    print(lines)"""

#Añadir texto
"""with open("cuento.txt" , "a") as file:
    file.write("\n\nBy:Samuel")"""

#Sobreecribir el texto
with open("cuento.txt" , "w") as file:
    file.write("\n\nBy:Samuel")