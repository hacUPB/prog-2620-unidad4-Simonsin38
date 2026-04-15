registro_aeronaves = {}

def agregar_aeronave():
    nombre = input("Ingrese el nombre de la aeronave: ")
    matricula = input("Ingrese la matrícula: ")
    modelo = input("Ingrese el modelo: ")
    horas = float(input("Ingrese las horas de vuelo: "))

    registro_aeronaves[nombre] = {
        "Matricula": matricula, "Modelo": modelo, "Horas de la aeronave": horas,
        "Componentes": {}
    }
    print("Se agrego la aeronave")


def eliminar_aeronave():
    nombre = input("Ingrese el nombre de la aeronave a eliminar: ")
    if nombre in registro_aeronaves:
        del registro_aeronaves[nombre]
        print("Aeronave eliminada")
    else:
        print("Aeronave no encontrada")


def agregar_componente():
    nombre = input("Ingrese la aeronave a la que desea agregar componentes: ")
    if nombre in registro_aeronaves:
        componente = input("Nombre del componente: ")
        horas_uso = float(input("Horas de uso: "))
        horas_limite = float(input("Horas límite antes de mantenimiento: "))

        registro_aeronaves[nombre]["Componentes"][componente] = {
            "Horas de uso": horas_uso,
            "Horas Limite": horas_limite
        }
        print("Componente agregado correctamente.")
    else:
        print("Aeronave no encontrada.")


def consultar_mantenimiento():
    for aeronave, datos in registro_aeronaves.items():
        for componente, info in datos["Componentes"].items():
            if info["Horas de uso"] >= info["Horas Limite"]:
                print(f"El componente -{componente}- de la aeronave {aeronave} requiere mantenimiento")
    print()

while True:
    print("Menú")
    print("1. Agregar aeronave")
    print("2. Eliminar aeronave")
    print("3. Agregar componente")
    print("4. Consultar mantenimiento")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_aeronave()
    elif opcion == "2":
        eliminar_aeronave()
    elif opcion == "3":
        agregar_componente()
    elif opcion == "4":
        consultar_mantenimiento()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida.")