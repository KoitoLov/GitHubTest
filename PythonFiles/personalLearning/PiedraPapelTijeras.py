import random

jugando = True

while jugando:
    computador = random.choice([1, 2, 3])
    print(computador)
    intento = int(input("Piedra(1), papel(2) o tijera(3)? "))
    if intento == computador:
        jugar = input("Ha ganado, quiere jugar de nuevo s/n: ")
        if jugar == "n":
            jugando = False
        else:
            print("Reiniciando juego...")
            print("////////////////////")
    else:
        print("Ha perdido. Terminando programa.")
        jugando = False
