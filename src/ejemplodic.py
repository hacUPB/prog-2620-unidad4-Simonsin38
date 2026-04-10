libro = {"Comida": ["Pizza", "Hamburguesa", "Papas"]
         ,"Edad": 10,
         "Pais": "Colombia",
         "Año": 2026,
         "Cosas" : [["Barco", "Avión", "Carro"], ["Lunes", "Martes", "Miércoles"], ["Camisa", "Zapatos", "Sombrero"]],
         "Año": 2021}
print(libro["Año"])
print(f"Diccionario Inicial: \n {libro}")
comida = {libro["Comida"][2]}
print(comida)
Cosa = {libro["Cosas"][2][1]}
print(Cosa)

print({libro["Edad"]})

libro["Edad"] = 19

print({libro["Edad"]})

libro["Planeta"] = "Júpiter"
print(libro)

seccion = input("Sección del Diccionario: ")
print(libro.get(seccion, "Sección No Válida"))
borrar = input("Borrar Sección: ")
if borrar in libro:
    del libro[borrar]
else:
    print("No se borró nada")
print(libro)

libro["Comida"].append("Perro")


aeronaves = {"Boeing" : {"Matricula" : 123213213, "Modelo" : "a340", "horas" : 500000000}}

print(aeronaves["Boeing"]["Matricula"])