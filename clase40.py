'''x = 100 #Variable Global

def local_function():
    x = 10 #Variable local
    print(f"El valor de la variable es {x}")

def show_global():
    print(f'El valor de la variable global es {x}')

local_function()
print(x)'''

'''x = 'global'

#Funcion Externa
def outer_function():
    x = 'enclosing'

    #Funcion Interna
    def inner_function():
        x = 'local' #Variable local
        print(x)

    inner_function()
    print(x)

outer_function()
print(x)'''

'''x = 5

def modify_global():
    global x 
    x += 3
    print(f'Valor modificado: {x}')

modify_global()
print(x)'''

def outer_function():
    x = 'enclosing'
    def inner_function():
        nonlocal x
        x = 'modified'
        print(f'El valor en inner es: {x}')
    inner_function()
    print(f'El valor outer: {x}')
outer_function()