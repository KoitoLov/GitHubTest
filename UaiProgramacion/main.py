num = input("")
lista_num = []
lista_nueva = []


for n in num:
    lista_num.append(int(n))

#Convertir al numero una lista de sucesores
for i in range(len(lista_num)):
    for e in range(len(lista_num)+ 1):
        if e != i and e != 0:
            if num[i:e] != '':
                lista_nueva.append(int(num[i:e]))

contador = 0
primo = 0

#Ver si la lista_nueva tiene primos y contar cuantos
for i in lista_nueva:
    if i != 1:
        for e in range(i+1):
            if e != 0:
                if i % e == 0:
                    contador += 1
        
        if contador == 2:
            primo += 1
            contador = 0
        else:
            contador = 0
            continue

print(primo)