registro_aeronaves = {}
aeronave = []

for i in range(3):
    aeronave = input(f"Ingrese la aeronave #{i + 1}: ")
    matricula = input(f"Ingrese la matricula del {aeronave}: ")
    modelo = input(f"Ingrese el modelo del {aeronave}: ")
    horas = float(input(f"Ingrese las horas de vuelo del {aeronave}: "))
    motorih = float(input("Ingrese las horas de uso del motor izquierdo"))
    motoril = float(input("Ingrese as horas limite antes del mantenimiento del motor izquierdo"))
    motordh = float(input("Ingrese las horas de uso del motor izquierdo"))
    motordl = float(input("Ingrese as horas limite antes del mantenimiento del motor izquierdo"))
    registro_aeronaves[aeronave] = {"Matricula" : matricula , "Modelo" : modelo , "Horas de la aeronave" : horas , 
                                    "Componentes" : {"Motor izquierdo" : {"Horas de uso" : motorih , "Horas Limite" : motoril} , 
                                                     "Motor derecho" : {"Horas de uso" : motordh , "Horas Limite" : motordl}}}

    
print(registro_aeronaves)

