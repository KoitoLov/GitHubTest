sexo = input("Ingrese su sexo H/M: ")
peso = int(input("Ingrese su peso: "))
altura = int(input("Ingrese su altura: "))
edad = int(input("Ingrese su edad: "))
print("Segun la tabla usted hace:  \na) Pocoo nada de ejercicio \nb) Ejercicio ligero \nc) Ejercicio moderado \nd) Soy deportista \ne) Soy atleta")
alternativa = input("Alternativa: ")
pregunta = True

a = 1.2
b = 1.375
c = 1.55
d = 1.72
e = 1.9

tmb = 0

#Ecuacion por sexo.
if sexo.lower() == "h":
    tmb = 66 + (13.7 * peso) + (5 * altura) - (6.75 * edad)
elif sexo.lower() == "m":
    tmb = 655 + (9.6 * peso) + (1.8 * altura) - (4.7 * edad)

#Evaluar la alternativa que eligio el usuario y en base a la respuesta calcular el tmb
if alternativa == "a":
    tmb = tmb * a
elif alternativa == "b":
    tmb = tmb * b
elif alternativa == "c":
    tmb = tmb * c
elif alternativa == "d":
    tmb = tmb * d
elif alternativa == "e":
    tmb = tmb * e

print("Su TMB es", tmb)

while pregunta:
    #Preguntarle al usuario si quiere seguir dentro del programa.
    print("////////////////")
    print("a) Desea conocer como esta su alimentacion \nb) Desea salir del programa? ")
    seguir = input("Que opcion desea? a/b: ")
    
    #Terminar programa si el usuario eligio b
    if seguir == "b":
        break
    
    #Preguntar al usuario por el consume de sus hidratos, proteinas y grasa
    hidrato = int(input("Cuantos gramos de Hidrato de Carbono consume al dia? "))
    proteinas = int(input("Cuantos gramos de Proteinas consume al dia? "))
    grasa = int(input("Cuantos gramos de Grasa consume al dia? "))
    
    #Calcular su consumo en basea gramos
    hidrato = hidrato * 4
    proteinas = proteinas * 4
    grasa = grasa * 9

    #Calcular su consumo TOTAL
    total = (hidrato + proteinas + grasa)
    print(total)

    #Determinar cuanto peso por dia pierde si el total es menor que el tmb calculado
    if total < tmb:
        print("Usted consume menos calorias de las que gasta.")
        bajar = ((total - tmb) * 30/7000) * -1
        print("Usted bajara", bajar, "cada 30 dias")

    #Determinar cuanto peso por dia gana si el total es menor que el tmb calculado
    elif total <= tmb:
        print("Usted consume mas calorias de las que gasta.")
        subir = (tmb - total) * 30/7000
        print("Usted subira", subir, "cada 30 dias")
