#Manipulacion de listas en Python: Creacion, Indexacion y Métodos Básicos
to_do = ["Diriginos al hotel",
         "Ir a almorzar",
         "Visitar un museo",
         "Volver al hotel"]

print(to_do)
numbers = [1,2,3,4, "Cinco"]
print(type(numbers))
mix = ["uno" , 2 , 3.14 , True, [1,2,3]]
print(mix)
print(len(mix))
print("Primer Elementos" , mix[0])
print("Segundo Elemento" , mix[1])
print("Ultimo Elemento" , mix[-1])
string = "Hola mundo"
print("Primer Elemento" , string[0])
print("Segundo Elemento" , string[1])
print("Ultimo elemento:" , string[-1])
print(mix[:])
print(mix)
mix.append(False)
print(mix)
mix.append(["a" , "b"])
print(mix)
mix.insert(1,["a","b"])
print(mix)
print(mix.index(["a","b"]))
numbers = [1,2,100,90.45,3,4,5]
print(numbers)
print("Mayor" , max(numbers))
print("Mayor" , min(numbers))
del numbers[-1]
print(numbers)
del numbers[:2]
print(numbers)
