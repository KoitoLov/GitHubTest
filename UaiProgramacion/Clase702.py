# calcular nuestra nota final dependiendo de las notas que obtengamos
# P = (P1 + P2)*0.2 + 0.25*P3 + 0.15*C + 0.1*T + 0.1*P
p1 = float(input("Ingrese nota prueba 1: "))
p2 = float(input("Ingrese nota prueba 2: "))
p3 = float(input("Ingrese nota prueba 3: "))
c = float(input("Ingrese nota final de controles: "))

cantidad_tareas = int(input("Ingrese el numero de tareas: "))
contador = 1

notas_tareas = 0

for tareas in range(cantidad_tareas):
    print("Ingrese la nota de la tarea", contador, ":")
    nota_tarea = float(input("Nota: "))

    notas_tareas += nota_tarea
    contador += 1

promedio_tarea = notas_tareas/cantidad_tareas
print(promedio_tarea)

p = float(input("Ingrese nota final de proyecto: "))
print((p1+p2)*0.2+p3*0.25+c*0.15+promedio_tarea*0.1+p*0.1)
