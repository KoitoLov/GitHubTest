import time
import random

jugando = True
puntos = 0

while jugando:
    colores = ["rojo", "verde", "azul", "amarillo"]

    print("Memoriza los colores...")
    print("Tienes 4 segundos...")

    random.shuffle(colores)
    colores_random = random.sample(colores, 4)

    print(colores_random)

    time.sleep(4)

    for i in range(14):
        print("///////////////")
    
    primero = input("Ingresa el nombre del primer color: ")
    segundo = input("Ingresa el nombre del segundo color: ")
    tercero = input("Ingresa el nombre del tercer color: ")
    cuarto = input("Ingresa el nombre del cuarto color: ")

    if primero == colores_random[0] and segundo == colores_random[1] and tercero == colores_random[2] and cuarto == colores_random[3]:
        puntos += 1
        print("Acertaste, ganas 1 punto. Tu total de puntos es:", puntos)
    else:
        print("No acertaste. Perdiste el juego.")
        jugando = False


