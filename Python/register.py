import re
import time
import sqlite3
import os
import hashlib
import getpass
from menu import principal

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def priv_contraseña(contraseña):
    return hashlib.sha256(contraseña.encode('utf-8')).hexdigest()

def crear_conexion():
    conn = sqlite3.connect('base_datos.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL UNIQUE,
        contraseña TEXT NOT NULL
    )
    ''')
    return conn, cursor

def Registrar(cursor, conn):
    while True:
        try:
            limpiar()
            usuario = input('Ingrese un usuario (mínimo 4 caracteres): ')
            if len(usuario) < 4:
                print('El nombre de usuario debe tener al menos 4 caracteres.\n')
                time.sleep(1)
            else:
                while True:
                    contraseña = input('Ingrese una contraseña (mínimo 6 caracteres, 1 mayúscula, 1 minúscula, 1 número): ')
                    if (re.search(r'[a-z]', contraseña) and 
                        re.search(r'[A-Z]', contraseña) and 
                        re.search(r'[0-9]', contraseña) and len(contraseña) >= 6):
                        
                        contraseña_hash = priv_contraseña(contraseña)
                        cursor.execute('INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)', (usuario, contraseña_hash))
                        conn.commit()
                        print('Usuario registrado con éxito.\n')
                        time.sleep(1)
                        return
                    else:
                        print('La contraseña no cumple con los requisitos.\n')
                        time.sleep(1)
        except sqlite3.IntegrityError:
            print('El nombre de usuario ya está en uso. Intente otro nombre.\n')
            time.sleep(1)

def verificar_usuario(cursor, usuario, contraseña):
    cursor.execute('SELECT contraseña FROM usuarios WHERE usuario = ?', (usuario,))
    usuario_encontrado = cursor.fetchone()
    
    if usuario_encontrado:
        contraseña_hash = priv_contraseña(contraseña)
        if usuario_encontrado[0] == contraseña_hash:
            return True
    return False

def login(cursor, conn):
    while True:
        limpiar()
        usuario = input('Ingrese su usuario: ')
        contraseña = getpass.getpass('Ingrese su contraseña: ')
        
        if verificar_usuario(cursor, usuario, contraseña):
            print('Usuario y contraseña correctos.\n')
            time.sleep(1)
            principal()
        else:
            print('Usuario o contraseña incorrectos.\n')
            time.sleep(1)

def menu():
    conn, cursor = crear_conexion()
    
    while True:
        try:
            limpiar()
            print('          Menú         ')
            print('-----------------------')
            print('1. Registrar\n2. Iniciar sesión\n3. Salir\n')
            seleccion = int(input('¿Qué acción desea realizar? '))
            
            if seleccion == 1:
                Registrar(cursor, conn)
            elif seleccion == 2:
                login(cursor, conn)
            elif seleccion == 3:
                print('Gracias por usar el sistema. ¡Hasta luego!\n')
                time.sleep(1)
                break
            else:
                print('Opción inválida, intente de nuevo.\n')
                time.sleep(1)
        except ValueError:
            print('Selección no válida, debe ingresar un número.\n')
            time.sleep(1)
    
    conn.close()

if __name__ == '__main__':
    menu()
