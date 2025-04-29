cant=int(input("Ingrese la cantidad de notas:\n"))
suma=0

for i in range(cant):
    print(f"La cantidad de notas es: {cant}")
    nota=float(input(f"Ingrese la nota {i+1} \n"))
    suma+=nota
    prom=suma/cant
    
print(f"El promedio es: {prom}")
if prom>=4:
    print(f"Felicidades aprovó con un {prom}")
else:
    print(f"Lo lamento, usted reprobó con un {prom}")