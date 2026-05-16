#!/data/data/com.termux/files/usr/bin/python3

import os
import subprocess
import random
import datetime
import shutil
from pathlib import Path

def limpiar_pantalla():
    os.system('clear')

def mostrar_banner():
    print("\033[36m")
    print("╔══════════════════════════════════════════════════════════╗")
    print("║                                                          ║")
    print("║     🚀 SCRIPT INTERACTIVO PARA TERMUX 🚀                ║")
    print("║                                                          ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print("\033[0m")
    print(f"\033[33m📱 Usuario: {os.getlogin()} | 📅 Fecha: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\033[0m")
    print()

def mostrar_menu():
    print("\033[32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
    print("\033[37m                📋 MENÚ PRINCIPAL 📋\033[0m")
    print("\033[32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
    print("\033[36m1.\033[0m 📦 Actualizar sistema")
    print("\033[36m2.\033[0m 🔧 Instalar herramientas básicas")
    print("\033[36m3.\033[0m 🌐 Información de red")
    print("\033[36m4.\033[0m 💾 Información de almacenamiento")
    print("\033[36m5.\033[0m 🧹 Limpiar caché")
    print("\033[36m6.\033[0m 💻 Información del sistema")
    print("\033[36m7.\033[0m 🔑 Generador de contraseñas")
    print("\033[36m8.\033[0m 📝 Calculadora simple")
    print("\033[36m9.\033[0m 🎮 Juego: Adivina el número")
    print("\033[36m0.\033[0m \033[31m❌ Salir\033[0m")
    print("\033[32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")

def actualizar_sistema():
    print("\033[33m📦 Actualizando sistema...\033[0m")
    os.system("pkg update && pkg upgrade -y")
    print("\033[32m✅ Sistema actualizado!\033[0m")
    input("Presiona Enter para continuar...")

def instalar_herramientas():
    print("\033[33m🔧 Instalando herramientas...\033[0m")
    os.system("pkg install -y python python2 git wget curl nano")
    print("\033[32m✅ Herramientas instaladas!\033[0m")
    input("Presiona Enter para continuar...")

def info_red():
    print("\033[36m🌐 Información de red:\033[0m")
    os.system("ifconfig | grep 'inet ' | grep -v 127.0.0.1")
    print("\033[33mIP Pública:\033[0m")
    os.system("curl -s ifconfig.me")
    print()
    input("Presiona Enter para continuar...")

def info_almacenamiento():
    print("\033[36m💾 Almacenamiento:\033[0m")
    os.system("df -h")
    input("Presiona Enter para continuar...")

def limpiar_cache():
    print("\033[33m🧹 Limpiando caché...\033[0m")
    cache_dir = Path.home() / ".cache"
    if cache_dir.exists():
        shutil.rmtree(cache_dir)
        cache_dir.mkdir()
    print("\033[32m✅ Caché limpiada!\033[0m")
    input("Presiona Enter para continuar...")

def info_sistema():
    print("\033[36m💻 Información del sistema:\033[0m")
    print(f"\033[33mSO:\033[0m {os.uname().sysname}")
    print(f"\033[33mArquitectura:\033[0m {os.uname().machine}")
    print(f"\033[33mHostname:\033[0m {os.uname().nodename}")
    input("Presiona Enter para continuar...")

def generar_password():
    import string
    longitud = input("\033[37mLongitud de contraseña (8-20): \033[0m")
    try:
        longitud = int(longitud)
        if longitud < 8:
            longitud = 12
    except:
        longitud = 12
    
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(random.choice(caracteres) for _ in range(longitud))
    print(f"\033[32m✅ Contraseña generada: \033[36m{password}\033[0m")
    input("Presiona Enter para continuar...")

def calculadora():
    print("\033[36m📝 CALCULADORA\033[0m")
    operacion = input("Ingresa operación (ej: 10+5): ")
    try:
        resultado = eval(operacion)
        print(f"\033[32m✅ Resultado: {resultado}\033[0m")
    except:
        print("\033[31m❌ Operación no válida\033[0m")
    input("Presiona Enter para continuar...")

def juego_adivinar():
    print("\033[33m🎮 ADIVINA EL NÚMERO (1-100)\033[0m")
    secreto = random.randint(1, 100)
    intentos = 0
    
    while True:
        try:
            num = int(input("Adivina: "))
            intentos += 1
            if num == secreto:
                print(f"\033[32m✅ ¡Correcto! Lo lograste en {intentos} intentos\033[0m")
                break
            elif num < secreto:
                print("\033[36m📈 El número es MAYOR\033[0m")
            else:
                print("\033[31m📉 El número es MENOR\033[0m")
        except:
            print("Ingresa un número válido")
    
    input("Presiona Enter para continuar...")

def main():
    while True:
        limpiar_pantalla()
        mostrar_banner()
        mostrar_menu()
        
        opcion = input("👉 Selecciona una opción: ")
        
        if opcion == "1":
            actualizar_sistema()
        elif opcion == "2":
            instalar_herramientas()
        elif opcion == "3":
            info_red()
        elif opcion == "4":
            info_almacenamiento()
        elif opcion == "5":
            limpiar_cache()
        elif opcion == "6":
            info_sistema()
        elif opcion == "7":
            generar_password()
        elif opcion == "8":
            calculadora()
        elif opcion == "9":
            juego_adivinar()
        elif opcion == "0":
            print("\033[32m👋 ¡Hasta luego!\033[0m")
            break
        else:
            print("\033[31m❌ Opción no válida\033[0m")
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()