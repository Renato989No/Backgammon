import dados as dd
baseUsuarios = {}
playerOrden = {}

def registrarUser():
    while True:
        user = input("Ingrese su usuario:")
        if user not in baseUsuarios:
            password = input("Ingrese su contraseña:")
            baseUsuarios[user] = password
            print(f"Usuario {user} creado exitosamente")
            break
        else:
            print("Error!! Usuario ya existe")


def verificar(user, password):
    if user in baseUsuarios:
        if baseUsuarios[user] == password:
            return True
    return False

def establecerSigno(player1, player2):
    print(f"Jugador {player1[0]}, elige la ficha [X u O]:")
    ficha = input("")

    player1.append(ficha)
    if ficha == "O":
        player2.append("X")
    else:
        player2.append("O")


def asignarDados():
    for i in playerOrden.keys():
        d1,d2 = dd.lanzarDados()
        playerOrden[i].append(d1)
        playerOrden[i].append(d2)
        playerOrden[i].append(d1+d2)
        print(f"Dados para {i}: {playerOrden[i][1]}, {playerOrden[i][2]}")

def establecerOrden():
    for i in range(2):
        print(f"Jugador {i+1}")
        user = input("Ingrese su usuario:")
        password = input("Ingrese contraseña:")
        if verificar(user, password):
            playerOrden[f'jugador {i+1}'] = [user]
        else:
            print("¡Datos incorrectos!")
            print("Por favor vuelva a ingresar usuario")
            return False
    
    while True:
        asignarDados()
        if playerOrden['jugador 1'][3] > playerOrden['jugador 2'][3]:
            establecerSigno(playerOrden['jugador 1'], playerOrden['jugador 2'])
            break
        elif playerOrden['jugador 1'][3] == playerOrden['jugador 2'][3]:
            continue
        else:
            establecerSigno(playerOrden['jugador 2'], playerOrden['jugador 1'])
            break

    for i in range(2):
        print(f"El jugador {playerOrden[f'jugador {i+1}'][0]} jugara con la ficha {playerOrden[f'jugador {i+1}'][4]}")
    return True


        

