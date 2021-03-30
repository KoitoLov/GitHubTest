import random

numero_random = random.randint(1,100)
frases_muy_alto = ["Te has pasado", "El numero elegido es muy alto", "Apestas para este juego..."]
frases_muy_bajo = ["Te falta", "Muy abajo", "Menuda mierda de jugador"]

intento_limite = 7
jugando = True
print(numero_random)

while intento_limite > 0:
    intento = int(input("Elija un numero del 1 al 100: "))

    if intento == numero_random:
        print("Has acertado el numero!")
        break
    if intento != numero_random:
        intento_limite -= 1
        print("Incorrecto. Le quedan", intento_limite, "intentos.")
    if intento > numero_random:
        print(random.choice(frases_muy_alto))
    else:
        print(random.choice(frases_muy_bajo))

    

print("///////////////////////////////////////")
print("/////FIN DEL JUEGO/////")
print("El numero correcto era:", numero_random)



