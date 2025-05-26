# Hacer un promedio de notas dependiendo de la cantidad de estudiantes




def promedio():
    alumnos=int(input("Ingrese la cantidad de alumnos:\n"))
    promTotal = 0
    promCant = 0
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
        promTotal+=prom
    promedioGeneral=promTotal/alumnos
        # promCant += 1
    return promedioGeneral

def promedio_final(promTotal, promCant):
    promfinal = promTotal/promCant
    print(f"El promedio final es: {promfinal}")

if __name__ == "__main__":
    promTotal, promCant = promedio()
    promedio_final()