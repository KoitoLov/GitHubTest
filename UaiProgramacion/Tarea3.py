num = input(int())

lista_num = []
contador = 0
otro_contador = 0
otros_primos = 0
primos = 0


for n in str(num):
    lista_num.append(int(n))


for i in lista_num:
    if i != 1:
        for e in range(1000):
            if e != 0:
                if i % e == 0:
                    contador += 1


        if contador <= 2:
            contador = 0
            primos += 1
        


finished = False

for i in lista_num:
    for e in range(10):
        if e != 0:
            if (lista_num.index(i) + 1) == len(lista_num):
                finished = True
                break

            siguiente = (lista_num[(lista_num.index(i) + 1)])
            string_siguiente = str(i) + str(siguiente)
            numero_siguiente = int(string_siguiente)

            if numero_siguiente % e == 0:
                otro_contador += 1

    if otro_contador <= 2 and finished == False:
        otros_primos += 1
        otro_contador = 0
    else:
        otro_contador = 0
        continue

print(primos + otros_primos)