x = int(input("Ingrese un numero: "))
digito = 7

for i in range(x+1):
    if str(digito) in str(i):
        print(i)
    else:
        continue