registro_aeronaves = {}
aeronave = []

for i in range(3):
    aeronave = input(f"Ingrese la aeronave #{i + 1}: ")
    matricula = input(f"Ingrese la matricula del {aeronave}: ")
    modelo = input(f"Ingrese el modelo del {aeronave}: ")
    horas = float(input(f"Ingrese las horas de vuelo del {aeronave}: "))
    motorih = float(input("Ingrese las horas de uso del motor izquierdo: "))
    motoril = float(input("Ingrese las horas limite antes del mantenimiento del motor izquierdo: "))
    motordh = float(input("Ingrese las horas de uso del motor derecho: "))
    motordl = float(input("Ingrese las horas limite antes del mantenimiento del motor derecho: "))
    trenh = float(input("Ingrese las horas de uso del tren de aterrizaje: "))
    trenl = float(input("Ingrese las horas limite antes del mantenimiento del tren de aterrizaje: "))
    alabesh = float(input("Ingrese las horas de uso de los alabes: "))
    alabesl = float(input("Ingrese las horas limite antes del mantenimiento de los alabes: "))
    registro_aeronaves[aeronave] = {"Matricula" : matricula , "Modelo" : modelo , "Horas de la aeronave" : horas , 
                                    "Componentes" : {"Motor izquierdo" : {"Horas de uso" : motorih , "Horas Limite" : motoril} , 
                                                     "Motor derecho" : {"Horas de uso" : motordh , "Horas Limite" : motordl}, 
                                                     "Tren de Aterrizaje" : {"Horas de uso" : trenh , "Horas Limite" : trenl},
                                                     "Alabes" : {"Horas de uso" : alabesh , "Horas Limite" : alabesl}}}
for aeronave, datos in registro_aeronaves.items():
    for componente, info in datos["Componentes"].items():
        horas_uso = info["Horas de uso"]
        horas_limite = info["Horas Limite"]

        nombre_aeronave = aeronave
        nombre_componente = componente
        if horas_uso >= horas_limite:
            print(f"El componente -{nombre_componente}- de el {nombre_aeronave} requiere mantenimiento")