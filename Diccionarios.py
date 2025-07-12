#Diccionarios 

d1 = {
    "Nombre":"Jorge",
    "Edad":25,
    "Ci":1111111,
    "Ciudad": "La Paz"
}

#print(d1["Nombre"])

d2 = dict([
    ('Nombre','Sara'),
    ('Edad',27),
    ('ci',000000)
])

#print(d2['Nombre'])
d3 = dict(Nombre= "Anna", Edad = 24, ci = 777777 )


#Metodos que se pueden usar con Diccionarios
#Acceder a un elemento de un diccionario

#print(d1["Edad"])
#print(d1.get("Edad"))

#Modificar / Añadir 
d1["Nombre"] = "Alejandro"  #modificar

d1["Pais"] = "Bolivia" #añadimos elementos
#print(d1)

#Iterar Diccionario
"""
for x in d1:
    print(x)

print("-------------")
for x in d2:
    print(d2[x])

print("-------------")

for x,y in d1.items():
    print(x,y)
"""

#Consultas en diccionarios
#get()
print(d1.get("Nombre"))
print("-------------")
#items()
print(d1.items())
print("-------------")
#keys()
print(d1.keys())
print("-------------")
#values()
print(d1.values())