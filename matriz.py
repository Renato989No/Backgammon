import users as us
import dados as dd
import os
import time

fichasX = {'X':15, 'Capturadas':0}
fichasO = {'O':15, 'Capturadas':0}

arreglo = {1:11,2:10,3:9,4:8,5:7,6:6,7:5,8:4,9:3,10:2,11:1,12:0,13:0,14:1,15:2,16:3,17:4,18:5,19:6,20:7,21:8,22:9,23:10,24:11,'X':2,'O':1}

def generarMatriz():
    matriz = []
    for i in range(10):
        lista = []
        for j in range(12):
            if (i < 5 and j == 0) or (i>6 and j==4) or (i>4 and j==6) or (i<2 and j==11):
                lista.append(1)
            elif (i > 4 and j==0) or (i<3 and j==4) or (i<5 and j==6) or (i>7 and j==11):
                lista.append(2)
            else:
                lista.append(0)
        matriz.append(lista)
        lista = []
    return matriz

def imprimirMatriz(matriz):
    print(f"  Fichas X  |  Liberadas:{fichasX['X']}  |  Capturadas:{fichasX['Capturadas']}")
    print("==============================================")
    for i in range(13,25):
        print(i, end="  ")
    print()
    for i in range(len(matriz)//2):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 1:
                print("O", end= "   ")
            elif matriz[i][j] == 2:
                print("X", end="   ")
            else:
                print(" ", end="   ")
        print()
    print("==============================================")
    for i in range(5,len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 1:
                print("O", end= "   ")
            elif matriz[i][j] == 2:
                print("X", end="   ")
            else:
                print(" ", end="   ")
        print()
    for i in range(12,0,-1):
        if i < 10:
            print(f"0{i}", end="  ")
        else:
            print(i, end="  ")
    print()
    print("==============================================")
    print(f"  Fichas O  |  Liberadas:{fichasO['O']}  |  Capturadas:{fichasO['Capturadas']}")


def buscar(player, posicion, matriz):
    if posicion >= 13:
        for i in range(len(matriz)//2):
            if matriz[i][arreglo[posicion]] == arreglo[player[4]]:
                return True
    else:
        for i in range(len(matriz)-1,len(matriz)//2,-1):
            if matriz[i][arreglo[posicion]] == arreglo[player[4]]:
                return True

    return False
    

def abajo(player, matriz, col):
    for i in range(len(matriz)-1,len(matriz)//2-1,-1):
        if matriz[i][col] == 0:
            matriz[i][col] = arreglo[player[4]]
            return
    abajo(player, matriz, col+1)
def arriba(player, matriz, col):
    for i in range(len(matriz)//2):
        if matriz[i][col] == 0:
            matriz[i][col] = arreglo[player[4]]
            return
    arriba(player, matriz, col+1)

def eliminar(matriz, posicion):
    if 1 <= posicion < 13:
        for i in range(len(matriz)//2,len(matriz)):
            if matriz[i][posicion] != 0:
                matriz[i][posicion] = 0
                return
    else:
        for i in range(len(matriz)//2,0,-1):
            if matriz[i][posicion] != 0:
                matriz[i][posicion] = 0
                return



def moverO(player, posicion, move,matriz):
    if 1 <= (posicion-move) <= 13:
        abajo(player, matriz, arreglo[posicion-move])
    elif (posicion-move) < 1:
        arriba(player,matriz,arreglo[(24-(move-posicion))])
    else:
        arriba(player,matriz,arreglo[(posicion-move)])

def moverX(player, posicion, move,matriz):
    if 1 <= (posicion+move) <= 12:
        abajo(player, matriz, arreglo[posicion+move])
    elif (posicion+move) > 24:
        abajo(player,matriz,arreglo[1 + (move-(24-posicion))])
    else:
        arriba(player,matriz,arreglo[(posicion+move)])


def moverse(player, matriz):
    print(f"------ Turno de jugador {player[0]} ------")
    dados = list(dd.lanzarDados())
    posicion = []
    print(f"Dados: {dados[0]},{dados[1]}")
    while True:
        move1 = int(input(f"Posición de ficha a mover {dados[0]} posiciones [1-24]:"))
        if 1 <= move1 <= 24:
            if buscar(player, move1, matriz):
                posicion.append(move1)
                break
    while True:
        move2 = int(input(f"Posición de ficha a mover {dados[1]} posiciones [1-24]:"))
        if 1 <= move1 <= 24:
            if buscar(player, move2, matriz):
                posicion.append(move2)
                break
    
    for i in range(len(dados)):
        eliminar(matriz,arreglo[posicion[i]])
        if player[4] == 'O':
            moverO(player, posicion[i], dados[i],matriz)
        else:
            moverX(player, posicion[i], dados[i],matriz)
    imprimirMatriz(matriz)
    #time.sleep(2)
    #os.system('cls')
    return


def Backgammom( bool ):
    matriz = generarMatriz()
    if bool:
        print("------ SE INICIA BACKGAMMOM ------")
        print("El turno de juego es el siguiente:")
        for i in range(2):
            if us.playerOrden[f"jugador {i+1}"][4] == "O":
                n = 1
            else:
                n = 24
            print(f'- El jugador {us.playerOrden[f"jugador {i+1}"][0]} debe mover todas las fichas {us.playerOrden[f"jugador {i+1}"][4]} hasta la posición {n}')
    else:
        print("Establecer turnos!!")
        return
    
    imprimirMatriz(matriz)
    cont = 0
    while True:
        moverse(us.playerOrden[f"jugador {cont%2+1}"], matriz)
        cont += 1
   

