# Tu playlist de Bad Bunny
# playlist = ["Tití Me Preguntó", "Moscow Mule", "Ojitos Lindos"]

# for cancion in playlist:
#     print(cancion)

# print("\n\n")

# for n in range (len(playlist)):
#     print(playlist[n])

# Agregar una canción nueva
# cancion_nueva = input("Pon una cancion:\n")
# playlist.append(cancion_nueva)

# # # Ver una canción específica (posición 0, 1, 2...)
# # print(playlist[0])  # "Tití Me Preguntó"
# # print(playlist[1])  # Moscow Mule
# # # Cambiar una canción
# # playlist[1] = "Efecto"
# # print(playlist[1])  # Efecto

# for cancion in playlist:
#     print(cancion)

# print("\n\n")

# for n in range (len(playlist)):
#     print(playlist[n])
# # Eliminar una canción
# playlist.remove("Ojitos Lindos")

# for cancion in playlist:
#     print(cancion)

# print("\n\n")

# for n in range (len(playlist)):
#     print(playlist[n])

# playlist = ["Canción 1", "Canción 2", "Canción 3"]

# cancion_nueva = input("Pon una cancion:\n")
# playlist.append(cancion_nueva)

# for cancion in playlist:
#     print(cancion)

# for n in range (len(playlist)):
#     print(playlist[n])


# Lista de frutas

# frutas = ["Banana", "Manzana"]

# fruta_nueva = input("Ingresa tu fruta:\n")
# frutas.append(fruta_nueva)

# for n in range (len(frutas)):
#     print(frutas[n].upper(), "\n")

# for fruta in frutas:
#     print(fruta.upper(), "\n")

# while True:
#     fruta_eliminada = input("Elige la fruta para borrar:\n")
    
#     if fruta_eliminada not in frutas:
#         print("Esa fruta no está aqui")
    
#     else:
#         frutas.remove(fruta_eliminada)
#         print("Fruta borrada")
#         break

# for fruta in frutas:
#     print(fruta.upper(), "\n")



# Diccionarios

# alumnos = [
#     {
#     "Nombre" : "Juan",
#     "Edad" : 22,
#     "Curso" : "Primer Semestre Universidad",
#     "Estudiando" : True
# },
#     {
#     "Nombre" : "Antonia",
#     "Edad" : 19,
#     "Curso" : "Primer Semestre Universidad",
#     "Estudiando" : True
#     }
# ]

# for alumno in alumnos:
#     for c, v in alumno.items():
#         print(c, ":", v)

# for alumno in alumnos:
#     alumno["Promedio"] = 6.0

# alumnos[0]["Promedio"] = 6.5

# nuevo_promedio = float(input("Ingresa el promedio de Juan:\n"))

# alumnos[0]["Promedio"] = nuevo_promedio

# for alumno in alumnos:
#     for c, v in alumno.items():
#         print(c, ":", v)



d1 = {
  "Nombre": "Sara",
  "Edad": 27,
  "Documento": 1003882
}

print(d1)

nombre = input("Ingresa un nombre")

d1['Nombre'] = nombre


direccion = input("Ingresa un nombre")

d1["Direccion"] = direccion

#{'Nombre': Laura', 'Edad': 27, 'Documento': 1003882}

#{'Nombre': 'Sara', 'Edad': 27, 'Documento': 1003882}

for k, v in d1.items():
    print(f"{k} = {v}")