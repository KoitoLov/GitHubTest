contador_resto = 0

num = int(input("Numero: "))

for i in range(0,10000001):
    if i == 0:
        continue
    resultado = num % i
    if resultado == 0:
        contador_resto += 1

if contador_resto > 2:
    print("El numero", num, "no es primo.")
elif contador_resto <= 2:
    print("El numero", num, "es primo.")