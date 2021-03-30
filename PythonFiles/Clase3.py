nombre  = input("Ingrese su nombre: ")

print("///////////////////")
print("Ingrese los siguientes datos como numeros: ")

diaN    = int(input("Ingrese su dia de nacimiento: "))
mesN  = int(input("Ingrese su mes de nacimiento: "))
yearN   = int(input("Ingrese su año de nacimiento: "))

diaA    = int(input("Ingrese el dia actual: "))
mesA  = int(input("Ingrese el mes actual: "))
yearA   = int(input("Ingrese el año actual: "))


#La funcion abs transforma el valor a un numero de valor absoluto.
resultadoDia = abs(diaA - diaN)
resultadoMes = abs(mesA - mesN)
resultadoYea = abs(yearA - yearN)

#Si el mes actual es menor que el mes de nacimiento, restele 1 al año.
if mesA < mesN:
    resultadoYea -= 1

print("////////////////////")

print(nombre, "tiene", resultadoYea, resultadoMes, resultadoDia, "años")

