numbers = {1:"uno" , 2:"dos", 3:"tres"}
print(numbers[2])
information = {"nombre":"samuel",
                "Apellido":"Perez",
                "Altura":1.80,
                "Edad":21}

print(information)
del information["Edad"]
print(information)
claves = information.keys()
print(claves)
print(type(claves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)

contacts = {"Samuel":{"Apellido":"Perez",
                    "Altura":1.80,
                    "Edad":21},
            "Diego":{"Apellido":"Antezana",
                        "Altura":1.80,
                        "Edad":32}}
print(contacts["Samuel"])