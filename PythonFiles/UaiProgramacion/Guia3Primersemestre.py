#Primer problema.
#  for i in range(0,21):
#     if i % 2 != 0:
#         print(i)



#Segundo problema V.1
# for i in range(0,1001):
#     if i % 3 == 0:print("Reiniciando juego...")
#         print(i)
#     elif i % 4 == 0:
#         print(i)

#Segundo problema V.2
# for i in range(0,1001):
#     if i % 3 == 0 and i % 4 == 0:
#         print(i)



#Tercer problema
# rango = int(input("Ingrese un numero: "))
# contador = 0

# for i in range(rango + 1):
#     if i % 3 == 0 and i % 4 == 0:
#         contador += 1
#         print(i)

# print("Cantidad de numeros:", contador)



#Cuarto problema.
# n = int(input("Numero: "))
# i = 0

# for sumatoria in range(n + 1):
#         i += sumatoria
#         print(i)


#Quinto problema.
# n = int(input("Numero: ")) 
# i = 1

# for sumatoria in range(n + 1):
#     if sumatoria > 0:
#         i *= sumatoria
#         print(i)



#Sexto problema.
# n = int(input("Numero: "))
# i = 0

# for sumatoria in range(n + 1):
#     if sumatoria % 2 == 0:
#         i += sumatoria
#         print(i)



#Septimo problema.
# n = int(input("Numero: ")) 
# i = 1

# for sumatoria in range(n + 1):
#     if sumatoria % 2 != 0
#         if sumatoria > 0:
#             i *= sumatoria
#             print(i)



#Octavo problema NO RESUELTO.

# contador_resto = 0

# num = int(input("Numero: "))

# for i in range(0,10000001):
#     if i == 0:
#         continue
#     resultado = num % i
#     if resultado == 0:
#         contador_resto += 1

# if contador_resto > 2:
#     print("El numero", num, "no es primo.")
# elif contador_resto <= 2:
#     print("El numero", num, "es primo.")
    



#Noveno problema NO RESUELTO.

contador_resto = 0

rango = int(input("Numero: "))

for i in range(rango):
    if i == 0:
        continue
    for e in range(10):
        if e == 0:
            continue
        resultado = i % e
        if resultado == 0:
            contador_resto += 1
            print(i)
    if contador_resto <= 2:
        print(i)






# #Decimo problema.
# num = int(input("Numero: "))

# while True:
#     if num < 7:
#         print("Ningun resultado.")
    
#     if 






