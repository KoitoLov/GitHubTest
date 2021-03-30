num_pruebas = int(input("Ingrese el numero de pruebas: "))
lista_de_notas = []

#Por cada num_pruebas preguntele al usuario una nota.
#Despues agreguelas a la lista: notas.
for numero in range(num_pruebas):
    notas = int((input("Ingrese la nota de dichas pruebas: ")))
    lista_de_notas.append(notas)

#Calcule el promedio
promedio = sum(lista_de_notas)/float(num_pruebas)

#Si el promedio es mayor que 4, entonces diga si aprobo o no.
if promedio >= 40.0:
    print("Usted aprueba con un", promedio)
else:
    print("Usted reprueba con un", promedio)
