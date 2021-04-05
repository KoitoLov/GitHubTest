num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
suma = 0


for i in range(num1, num2 + 1, 1):
    if i == 0:
        continue
    suma += i**2

print(suma)