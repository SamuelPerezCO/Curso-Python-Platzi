# Ejemplo de iterador

# Crear una lista
my_list = [1,2,3,4]

# Obtener el iterador
my_iter = iter(my_list)

#usar
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

#Iterar en cadenas
#Creando la cadena
text = "Hola mundo"
#Creando el objeto iterado
iter_text = iter(text)

#Iterar en la cadena
for char in iter_text:
    print(char)

#Crear un iterador para los numeros impares

#liminte
limit = 10

#Crear iterador
odd_itter = iter(range(1, limit + 1,2))

#usar el iterador
for num in odd_itter:
    print(num)

def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)

#Fibonacci
# 0 1 1 2 3 4 8 13 21 ..

def fibonacci(limit):
    a , b = 0 , 1
    while a < limit:
        yield a
        a , b = b , a+b

for num in fibonacci(10):
    print(num)