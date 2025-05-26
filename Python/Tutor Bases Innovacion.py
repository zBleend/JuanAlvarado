from os import system
import time
import webbrowser

def limpiar():
    system('cls')

def mostrar_menu():
    print("\n=== Menú Principal ===")
    print("1. Tutor paso a paso")
    print("2. Ver bibliografía")
    print("3. Salir del programa")
    return input("Elige una opción (1-3): ")

Explicador = {
    "powerpoint": [
        "1. Abre PowerPoint desde el menú de inicio.",
        "2. Selecciona 'Presentación en blanco'.",
        "3. Usa la pestaña 'Insertar' para añadir texto, imágenes o vídeos.",
        "4. Aplica transiciones y animaciones desde la pestaña 'Transiciones'.",
        "5. Guarda el archivo con Ctrl+S o en 'Archivo > Guardar como'."
    ],
    "zoom": [
        "1. Descarga e instala Zoom desde su sitio oficial.",
        "2. Abre Zoom e inicia sesión con tu cuenta.",
        "3. Haz clic en 'Nueva reunión' para iniciar una videollamada.",
        "4. Usa 'Invitar' para compartir el enlace con tus estudiantes.",
        "5. Comparte pantalla y graba la sesión si lo deseas."
    ],
    "canvas": [
        "1. Ingresa a tu plataforma Canvas con usuario y contraseña.",
        "2. Selecciona el curso en el que estás inscrito.",
        "3. Revisa los módulos, tareas y materiales disponibles.",
        "4. Usa 'Tareas' para entregar trabajos.",
        "5. Participa en foros desde la sección 'Discusión'."
    ],
    "word": [
        "1. Abre Microsoft Word desde el escritorio o menú de inicio.",
        "2. Crea un nuevo documento en blanco.",
        "3. Escribe tu contenido usando el teclado.",
        "4. Da formato con las herramientas: negrita, tamaño de fuente, alineación, etc.",
        "5. Guarda el archivo con Ctrl+S o en 'Archivo > Guardar como'."
    ],
    "gmail": [
        "1. Abre tu navegador y entra en www.gmail.com.",
        "2. Inicia sesión con tu correo y contraseña.",
        "3. Haz clic en 'Redactar' (botón azul).",
        "4. Escribe el correo del destinatario, asunto y cuerpo del mensaje.",
        "5. Haz clic en 'Enviar'."
    ],
    "youtube": [
        "1. Entra en www.youtube.com desde tu navegador.",
        "2. Usa la barra de búsqueda para buscar temas educativos.",
        "3. Puedes buscar canales como 'Educatina' o 'Khan Academy'.",
        "4. Crea una lista de reproducción para guardar tus videos favoritos.",
        "5. Activa los subtítulos y velocidad lenta si lo necesitas para aprender mejor."
    ]
}

def tutor_paso_a_paso():
    try:
        while True:
            print("\nTemas disponibles:", ', '.join(Explicador.keys()))
            tema = input("Escribe el nombre de la herramienta que quieres aprender: ").strip().lower()
            
            pasos = Explicador.get(tema)
            if pasos:
                print(f"\n--- Tutor para {tema.capitalize()} ---")
                for paso in pasos:
                    print(paso)
                break
            else:
                print("Lo siento, no tengo información sobre ese tema aún. Intenta con otro.")
    except (ValueError, Exception):
        print("Opcion no valida")

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            limpiar()
            tutor_paso_a_paso()
        elif opcion == "2":
            limpiar()
            print("No disponible por ahora.\nPero aqui te abro el navegador para mas informacion\nsobre los temas disponibles")
            webbrowser.open("https://chatgpt.com/share/6834ee32-b654-8002-a395-eccef803c0a3")
            time.sleep(1)
        elif opcion == "3":
            limpiar()
            print("Gracias por usar el tutor educativo. ¡Hasta pronto!")
            break 
        else:
            print("Opción inválida. Por favor, elige una opción del 1 al 3.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Ha ocurrido un error inesperado:", e)
