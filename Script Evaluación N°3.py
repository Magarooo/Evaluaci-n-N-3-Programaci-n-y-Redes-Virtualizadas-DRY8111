## Script Evaluación N°3


Alumnos = []

i=0
n=int(input("Ingrese numero estudiantes: "))

for i in range(i,n):
    nombre=input("Ingrese nombre estudiante: ")
    if Alumnos:
        Alumnos.append(nombre)
    else:
        Alumnos.insert(i, nombre)
    
    
print("Los alumnos que rendirán la evaluación 3 serán los siguientes: \n")

i=0

for i in range(i,n):
    print("Estudiante n°",i+1,":", Alumnos[i])
print("Programa Finalizado") 
