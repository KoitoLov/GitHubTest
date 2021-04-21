num = input("Ingrese un numero: ") #1582
lista_num = []
lista_nueva = []

def hacer_lista():
    for n in str(num):
        lista_num.append(int(n))
    return lista_num

hacer_lista()

for i in range(len(lista_num)):
    for e in range(len(lista_num)+ 1):
        if e != i and e != 0:
            if num[i:e] != '':
                lista_nueva.append(int(num[i:e]))
print(lista_nueva)

contador = 0
primo = 0

for i in lista_nueva:
    if i != 1:
        for e in range(i):
            if e != 0:
                if i % e == 0:
                    contador += 1
        
        if contador == 2:
            primo += 1
            contador = 0
            print(i)
        else:
            contador = 0
            continue

print("Cantidad de primos:", primo)
