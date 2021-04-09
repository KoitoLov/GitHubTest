num1 = int(input())
num2 = int(input())
suma = 0


for i in range(num1, num2 + 1, 1):
    if i == 0:
        continue
    suma += i**2

print(suma)