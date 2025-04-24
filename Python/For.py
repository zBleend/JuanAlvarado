# Hacer un promedio de notas dependiendo de la cantidad de estudiantes
alumnos=int(input("Ingrese la cantidad de alumnos:\n"))
for j in range(alumnos):
    cant=int(input(f"Ingrese la cantidad de notas del alumno {j+1}:\n"))
    suma=0
    for i in range(cant):
        print(f"La cantidad de notas es: {cant}")
        nota=float(input(f"Ingrese la nota {i+1} \n"))
        suma+=nota
    prom=suma/cant
    print(f"El promedio del alumno {j+1} es: {prom}")
    if prom>=4:
        print(f"Felicidades aprovó con un {prom}")
    else:
        print(f"Lo lamento, usted reprobó con un {prom}")