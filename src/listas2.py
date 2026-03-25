from random import randint
lista = []
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
for i in range(12):
    dato = randint(20, 80)
    lista.append(dato)
print(lista)
 
mayor = max(lista)
mes = lista.index(mayor)
veces = lista.count(mayor)
if veces > 1:
    lista_meses = []
    for i in range(len(lista)):
        if lista[i] == mayor:
            lista_meses.append(i)
    print("Ventas mayores en: ")
    for mes in lista_meses:
        print(f" {meses[mes]}")
else:
    mes = lista.index(mayor)
    print(f"Mayor venta en {meses[mes]}")