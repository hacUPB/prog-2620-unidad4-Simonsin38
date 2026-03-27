#INSERT-REMOVE-POP

#INSERT
print("Añadir animales en orden de tamaño (menor a mayor)")
lista = ["Hormiga", "Perro", "Elefante", "Ballena Azul"]
print(lista)

for i in range(3):
    lugar = int(input("Ingrese la posición en la lista: "))
    animal = input("Ingrese el animal: ")
    lista.insert(lugar, animal)
print(lista)

#REMOVE



