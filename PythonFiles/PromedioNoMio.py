import sys 

print('Bienvenido. Porfavor ingrese las notas requeridas con punto. Por ejemplo, si la nota de la prueba 1 es 6.2, ingresarla de esta misma forma.')
prueba1 = float(input('Ingrese nota de la prueba 1: '))
prueba2 = float(input('Ingrese nota de la prueba 2: '))
prueba3 = float(input('Ingrese nota de la prueba 3: '))
numtareas = int(input('Ingrese el numero de tareas: '))

conttareas=0
tareas=[]
while conttareas<numtareas:
    conttareas+=1
    tareas.append(float(input('Ingrese nota de la tarea '+str(conttareas)+': ')))


numcontroles = int(input('Ingrese el numero de controles: '))

contcontroles=0
controles=[]

while contcontroles<numcontroles:
    contcontroles+=1
    controles.append(float(input('Ingrese nota del control '+str(contcontroles)+': ')))

proyecto = float(input('Ingrese nota del proyecto: '))

notafinal=(prueba1+prueba2)*0.2
notafinal+=(prueba3*0.25)

promediotareas=0

for tarea in tareas:
    promediotareas+=tarea

promediotareas/=numtareas

notafinal+=(promediotareas*0.1)


notafinal+=(proyecto*0.1)

promediocontroles=0

for control in controles:
    promediocontroles+=control

promediocontroles/=numcontroles


notafinal+=(promediocontroles*0.15)

if (3.5<=notafinal<4):
    notarepechaje=float(input('Su promedio se encuentra entre 3.5 y 4.0, ingrese la nota del examen de repechaje: '))
    if notarepechaje>=4:
        notafinal=4
    else:
        notafinal=notarepechaje

if notafinal>=4:
    print('Aprueba el curso con nota final: '+str(notafinal))
else:
    print('Reprueba el curso con nota final: '+str(notafinal))