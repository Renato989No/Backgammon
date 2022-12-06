import users as us
import matriz as mt
import os
import time


bool = False
while True:
    print("Seleccione una de las siguientes opciones:\n1.\tRegistrar Jugador\n2.\tEstablecer Turno\n3.\tIniciar Backgammon\n0.\tSalir")
    n = int(input("Ingrese la opción deseada:"))
    os.system("cls")
    if n == 0: break
    elif n == 1:
        us.registrarUser()
        time.sleep(1.5)
        os.system("cls")
    elif n == 2:
        bool = us.establecerOrden()
        time.sleep(3)
        os.system("cls")
    elif n == 3:
        mt.Backgammom(bool)



