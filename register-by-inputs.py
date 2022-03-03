from turtle import color # Importes
import sockets # Importes
import colorama # Importes
from colorama import Fore, Style # Importes
print(Fore.RED + "[!] ES NECESARIO UN REGITRO") # AVISO

print("\n") # Separación

print(Fore.BLUE + "Su Nombre:", end="") # Imput ·1
nombre = input()
print(Fore.LIGHTMAGENTA_EX + f"[!] Nuevo Dato Registrado {nombre}")  # AVISO

print("\n") # Separación

print(Fore.BLUE + "Su Contraseña:", end="")  # Imput ·2
contraseña = input()
print(Fore.LIGHTMAGENTA_EX + f"[!] Nuevo Dato Registrado {contraseña}")  # AVISO

print("\n") # Separación

print(Fore.BLUE + "Su Fecha De Nacimiento: \n", end="")  # Imput ·3
print(Fore.BLUE + "EJEMPLO: 20/02/1997")
nacimiento = input()
print(Fore.LIGHTMAGENTA_EX + f"[!] Nuevo Dato Registrado {nacimiento}")  # AVISO

print("\n") # Separación

print(Fore.LIGHTYELLOW_EX + "¡¡¡Registro Éxisotoso!!! \n ") # AVISO
print(Fore.LIGHTYELLOW_EX + " Información Resgistrada: \n ") # AVISO
print(f"Tu Nombre: {nombre} \n ") # Guardado
print(f"Tu Contraseña: {contraseña} \n ") # Guardado
print(f"Tu Fecha De Nacimiento: {nacimiento} \n ") # Guardado
print(Fore.LIGHTCYAN_EX + "Developed by: Panda.xyz") # Créditos



