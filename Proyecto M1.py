import json
import datetime

# Cargar información de usuarios desde archivo JSON
try:
    with open("usuarios.json", "r") as archivo:
        usuarios = json.load(archivo)
except FileNotFoundError:
    usuarios = {}

def crear_usuario():
    user_log = input("Ingresa tu nombre de usuario: ")
    user_pass = input("Ingresa tu contraseña: ")
    confirm_pass = input("Confirma tu contraseña: ")

    if user_pass == confirm_pass:
        usuarios[user_log] = user_pass
        guardar_usuarios()
        print("Usuario creado con éxito")
    else:
        print("Las contraseñas no coinciden")

def iniciar_sesion():
    user_log = input("Ingresa tu nombre de usuario: ")
    user_pass = input("Ingresa tu contraseña: ")

    if user_log in usuarios and usuarios[user_log] == user_pass:
        print("Inicio de sesión exitoso")
        asistente_virtual()
    else:
        print("Usuario o contraseña incorrectos")

def guardar_usuarios():
    with open("usuarios.json", "w") as archivo:
        json.dump(usuarios, archivo)

def asistente_virtual():
    # Inicializar el asistente
    assistant = {}

    # Leer información del archivo JSON
    try:
        with open("notes.json", "r") as file:
            assistant = json.load(file)
    except FileNotFoundError:
        pass

    print("Hola, me llamo Lucía y soy tu Asistente Virtual")

    # Preguntar por el nombre del usuario
    if "nombre_usuario" not in assistant:
        nombre_usuario = input("¿Cuál es tu nombre? ")
        assistant["nombre_usuario"] = nombre_usuario
    else:
        print("Tu nombre es " + assistant["nombre_usuario"])

    # Preguntar por el color favorito del usuario
    if "color_favorito" not in assistant:
        color_favorito = input("¿Cuál es tu color favorito? ")
        assistant["color_favorito"] = color_favorito
    else:
        print("Tu color favorito es " + assistant["color_favorito"])

    # Preguntar por la canción favorita del usuario
    if "cancion_favorita" not in assistant:
        cancion_favorita = input("¿Cuál es tu canción favorita? ")
        assistant["cancion_favorita"] = cancion_favorita
    else:
        print("Tu canción favorita es " + assistant["cancion_favorita"])

    def save_notes():
        with open("notes.json", "w") as file:
            json.dump(assistant, file)

    # Guardar información
    save_notes()

def menu():
    while True:
        print("1. Crear usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            crear_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            break
        else:
            print("Opción inválida")

menu()
answer = 0
while answer != 6:
    print(f'{usuarios}. ¿En qué puedo ayudarte?')
    print('1 - Averiguar la hora')
    print('2 - Averiguar la fecha')
    print('3 - Jugar piedra, papel o tijera')
    print('4 - Jugar cara o cruz')
    print('5 - Jugar Adivina el número')
    print('6 - Tablas de multiplicar')
    print('7 - Salir')


    answer = int(input('¿Qué opción prefieres? '))
    if answer == 1:
        date_time = datetime.datetime.now()
        print('Hora actual:', date_time.time())
    if answer == 2:
        date_time = datetime.datetime.now()
        print('Fecha actual:', date_time.date())
    if answer == 3:
        import random


        def piedra_papel_tijera():
            print("¿Listo para jugar?")
            opciones = ['piedra', 'papel', 'tijera']
            eleccion_usuario = input("Elige 'piedra', 'papel' o 'tijera': ").lower()

            if eleccion_usuario not in opciones:
                print("Opción inválida. Por favor, elige 'piedra', 'papel' o 'tijera'.")
                return

            eleccion_maquina = random.choice(opciones)
            print(f"Lucia eligió: {eleccion_maquina}")

            if eleccion_usuario == eleccion_maquina:
                print("¡Es un empate!")
            elif (eleccion_usuario == 'piedra' and eleccion_maquina == 'tijera') or \
                    (eleccion_usuario == 'papel' and eleccion_maquina == 'piedra') or \
                    (eleccion_usuario == 'tijera' and eleccion_maquina == 'papel'):
                print("¡Felicidades, ganaste!")
            else:
                print("¡Perdiste!")


        # Ejecutar el juego
        piedra_papel_tijera()

    if answer == 4:
        def cara_o_cruz():
            print("¡Bienvenido al juego de cara o cruz!")
            eleccion_usuario = input("Elige 'cara' o 'cruz': ").lower()

            if eleccion_usuario not in ['cara', 'cruz']:
                print("Opción inválida. Por favor, elige 'cara' o 'cruz'.")
                return

            lanzamiento = random.choice(['cara', 'cruz'])
            print(f"Se lanzó la moneda y salió: {lanzamiento}")

            if eleccion_usuario == lanzamiento:
                print("¡Felicidades! Ganaste.")
            else:
                print("Suerte para la próxima.")


        # Ejecutar el juego
        cara_o_cruz()

    if answer == 5:
        import random

        number = random.randint(1, 100)

        attempts = 0

        while True:
            guess = int(input('Adivina el número del 1 al 100'))
            attempts += 1

            if guess > number:
                print('El número es demasiado grande, ¡inténtalo de nuevo!')
            elif guess < number:
                print('El número es demasiado pequeño, ¡inténtalo de nuevo!')
            else:
                print(f'¡Enhorabuena! ¡Has adivinado el número en {attempts} de intentos!')

            if attempts == 10:
                print('¡Se acabaron los intentos!')
                break
