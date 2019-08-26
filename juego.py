"""
Para que el computador pueda jugar escoger un número al azar entre 1 y 3, si es 1 entonces en piedra, si es
2 entonces papel y 3 tijera.
python juego.py piedra
Computador juega tijera
Ganaste
"""
import sys
from random import randint

if len(sys.argv) < 2:
    print("Escriba piedra, papel o tijera!")
    exit()

jugador = sys.argv[1]

if not(jugador == "piedra" or jugador == "papel" or jugador == "tijera"):     
    print("Argumento inválido: Debe ser piedra, papel o tijera.")
    exit()

computador = randint(0, 2)

if computador == 1:
    computador = "piedra"
elif computador == 2:
    computador = "papel"
else:
    computador = "tijera"   

print("El usuario eligio {}".format(jugador))
#print("El computador eligio {}".format(computador))

#computador tijera
if jugador == "piedra" and computador == "tijera":
    print("Computador juega {}".format(computador))
    print("Ganaste")

if jugador == "tijera" and computador == "tijera":
    print("Computador juega {}".format(computador))
    print("Empataste")

if jugador == "papel" and computador == "tijera":
    print("Computador juega {}".format(computador))
    print("Perdiste")

#computador papel
if jugador == "piedra" and computador == "papel":
    print("Computador juega {}".format(computador))
    print("Perdiste")

if jugador == "tijera" and computador == "papel":
    print("Computador juega {}".format(computador))
    print("Ganaste")

if jugador == "papel" and computador == "papel":
    print("Computador juega {}".format(computador))
    print("Empataste")

   #computador piedra
if jugador == "piedra" and computador == "piedra":
    print("Computador juega {}".format(computador))
    print("Empataste")

if jugador == "tijera" and computador == "piedra":
    print("Computador juega {}".format(computador))
    print("Perdiste")

if jugador == "papel" and computador == "piedra":
    print("Computador juega {}".format(computador))
    print("Ganaste") 