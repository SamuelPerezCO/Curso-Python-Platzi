def divide(a: int, b:int) -> float:
    #Validar que ambos parametros sean enteros
    if not isinstance(a , int) or not isinstance(b, int):
        raise TypeError('Ambos parámetros deben ser entero.')
    #Verificamos que el divisor no sea cero
    if b == 0:
        raise ValueError('El divisor no puede ser cero')
    
    return a/b


#Ejemplo de uso
try:
    res = divide(10 , '2') #Error de tipo
    print(res)
except TypeError as e:
    print(f'Error: {e}')

#Ejemplo ded uso
try:
    res = divide(10 , 0) #Error de tipo
    print(res)
except TypeError as e:
    print(f'Error: {e}')


#Ejemplo ded uso
try:
    res = divide(10 , 2) #Error de tipo
    print(res)
except (ValueError,TypeError) as e:
    print(f'Error: {e}')