encuesta = True
contador = 0
V = 0
A = 0
I = 0
G = 0

while encuesta:
    notas = input("Ingrese notas:")

    if notas == "0":
        break

    V += int(notas[0:1])
    A += int(notas[1:2])
    I += int(notas[2:3])
    G += int(notas[3:4])

    contador += 1

promedio_v = V/contador
promedio_a = A/contador
promedio_i = I/contador
promedio_g = G/contador

print("Nota promedio del producto V:", promedio_v)
print("Nota promedio del producto A:", promedio_a)
print("Nota promedio del producto I:", promedio_i)
print("Nota promedio del producto G:", promedio_g)

# print(V)
# print(A)
# print(I)
# print(G)



