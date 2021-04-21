nombre = input("Ingrese su nombre: ")

a1 = ("La solicitud de", nombre, "ha sido aprobada!")
a2 = ("Revisa antecendentes manualmente.")
a3 = ("La solicitud de", nombre, "no ha sido aprobada.")


# c2 = input("Se comprobo identidad (SI/NO) ")
# c3 = input("El monto prestamo es menos que sueldo mes? (SI/NO) ")
# c4 = input("Monto prestamo mayor que el sueldo mes? (SI/NO) ")
# c5 = input("Proposito del prestamo? Comprar casa(1) Pagar impuestos(2) Otro(3) ")
# c6 = input("Es propietario de la casa? (SI/NO) ")

        

c1 = input("Se comprobo direccion? (SI/NO) ")
if c1.lower() == "si":
    c2 = input("Se comprobo identidad (SI/NO) ")
    if c2.lower() == "si":
        c3 = input("El monto prestamo es menos que sueldo mes? (SI/NO) ")
        if c3.lower() == "si":
            print(a1)
        
        else:
            c4 = input("Monto prestamo mayor que el sueldo mes? (SI/NO) ")
            if c4 .lower()== "si":
                c5 = input("Proposito del prestamo? Comprar casa(1) Pagar impuestos(2) Otro(3) ")
                if c5 == "2":
                    print(a1)
                if c5 == "3":
                    print(a2)
            else:
                c6 = input("Es propietario de la casa? (SI/NO) ")
                if c6.lower() == "si":
                    print(a1)
                else:
                    print(a3)  
    else:
        print(a3)
else:
    print(a3)
