'''
import math

#Hallar el area y perimetro de un circulo
radius = 5
area = math.pi * radius ** 2
perimeter = 2 * math.pi * radius
print(area)
print(perimeter)
'''

import random

#Generar un numero entero aleatorio
random_number = random.randint(1,10)
print(random_number)

#Elegir colores aleaotorios
colors = ['Rojo' , 'Azul' , 'Verde']
random_color = random.choice(colors)
print(random_color)

#Barajar una lista de cartas
cards = ['As' , 'Rey' , 'Reina' , 'Jota' , '10']
random.shuffle(cards)
print(cards)