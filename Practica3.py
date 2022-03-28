import random


def crear_matriz(m, n):
    return[[i*j for j in range(n)]for i in range(m)]


def rellenar_matriz(m, n, list):
    for i in range(0, m):
        for j in range(0, n):
            if i == 0 or i == m-1:
                list[i][j] = ('-')
            elif j == 0 or j == n-1:
                list[i][j] = ('|')
            else:
                list[i][j] = (' ')
        # tableros[i][j]=5
    return list


def imprimir_matriz(m, n, list):
    for i in range(0, 7):
        for j in range(0, 8):
            print(list[i][j], end=' ')
        print('\n')

# variables


filas = 7
columnas = 8
FANTASMA = '@'
PREMIO = "O"
PARED = 'X'
PACMAN = '<'
matriz = crear_matriz(filas, columnas)
rellenar_matriz(filas, columnas, matriz)
# imprimir_matriz(filas,columnas,matriz)
noParedes = random.randint(5, 10)
nofantasmas = random.randint(1, 6)
noPremios = random.randint(3, 6)
noPac = 1
salir = False
exit = False
Score = 0
vidas = 1
puntajeMaximo = noPremios*10


# imprimir_matriz(filas,columnas,matriz)
# inicio de juego
while salir == False:
    print("======= MENU PRINCIPAL ========")
    print("1. Iniciar Juego")
    print("2. Salir")
    print("================================")
    opcion = input()

    if opcion == '2':
        salir = True
    elif opcion == '1':
        rellenar_matriz(filas, columnas, matriz)
        # Implementando premios y demas
        noParedes = random.randint(5, 10)
        nofantasmas = random.randint(1, 6)
        noPremios = random.randint(3, 6)
        puntajeMaximo = noPremios*10
        noPac = 1
        while noParedes > 0:
            fil = random.randint(1, 5)
            col = random.randint(1, 6)
            if matriz[fil][col].isspace():
                matriz[fil][col] = PARED
                noParedes = noParedes-1

        while nofantasmas > 0:
            fil = random.randint(1, 5)
            col = random.randint(1, 6)
            if matriz[fil][col].isspace():
                matriz[fil][col] = FANTASMA
                nofantasmas = nofantasmas-1

        while noPremios > 0:
            fil = random.randint(1, 5)
            col = random.randint(1, 6)
            if matriz[fil][col].isspace():
                matriz[fil][col] = PREMIO
                noPremios = noPremios-1

        while noPac > 0:    
            fil = random.randint(1, 5)
            col = random.randint(1, 6)
            if matriz[fil][col].isspace():
                matriz[fil][col] = PACMAN
                posActualX = fil
                posActualY = col
                noPac -= 1
                
        vidas = 1
        Score = 0
        
        print('Ingrese nombre de Usuario')
        nombreUsuario = input()
        exit = False
        while exit == False:
                matriz[posActualX][posActualY] = PACMAN
                print('Usuario: ', nombreUsuario)
                print('Punteo: ', Score)
                imprimir_matriz(filas, columnas, matriz)
                posAntiguaX = posActualX
                posAntiguaY = posActualY
                opcion = input()
                opcion = opcion.lower()
                if opcion == 'w':
                    posActualX -= 1
                elif opcion == 'a':
                    posActualY -= 1
                elif opcion == 's':
                    posActualX += 1
                elif opcion == 'd':
                    posActualY += 1
                elif opcion == 'f':
                    exit = True
                else:
                    print('Ingrese una opcion valida')

                if matriz[posActualX][posActualY] == FANTASMA:
                    vidas -= 1
                if vidas == 0:
                    matriz[posActualX][posActualY] = PACMAN
                    matriz[posAntiguaX][posAntiguaY] = ' '
                    imprimir_matriz(filas, columnas, matriz)
                    print('Has Perdido')
                    print('Usuario: ', nombreUsuario)
                    print('Punteo: ', Score)
                    
                    exit = True
                if matriz[posActualX][posActualY] == PREMIO:
                    Score = Score + 10
                if Score == puntajeMaximo:
                    matriz[posActualX][posActualY] = PACMAN
                    matriz[posAntiguaX][posAntiguaY] = ' '
                    imprimir_matriz(filas, columnas, matriz)
                    print('FELICIDADES')
                    print('HAS GANADAO')
                    print('Usuario: ', nombreUsuario)
                    print('Punteo: ', Score)
                    
                    exit = True
                if matriz[posActualX][posActualY] == FANTASMA or matriz[posActualX][posActualY] == PREMIO or matriz[posActualX][posActualY].isspace():
                    matriz[posActualX][posActualY] = PACMAN
                    matriz[posAntiguaX][posAntiguaY] = ' '
                if matriz[posActualX][posActualY] == PARED:
                    posActualX=posAntiguaX
                    posActualY=posAntiguaY
                if matriz[posActualX][posActualY] == '|':
                    if posActualY==7:
                        posActualY=1
                        if matriz[posActualX][posActualY] == FANTASMA:
                            vidas -= 1
                            if vidas == 0:
                                matriz[posActualX][posActualY] = PACMAN
                                matriz[posAntiguaX][posAntiguaY] = ' '
                                imprimir_matriz(filas, columnas, matriz)
                                print('Has Perdido')
                                print('Usuario: ', nombreUsuario)
                                print('Punteo: ', Score)
                                exit = True
                                
                        if matriz[posActualX][posActualY] == PREMIO:
                            Score = Score + 10
                        if Score == puntajeMaximo:
                            matriz[posActualX][posActualY] = PACMAN
                            matriz[posAntiguaX][posAntiguaY] = ' '
                            imprimir_matriz(filas, columnas, matriz)
                            print('FELICIDADES')
                            print('HAS GANADAO')
                            print('Usuario: ', nombreUsuario)
                            print('Punteo: ', Score)
                            exit = True
                        
                        if matriz[posActualX][posActualY] == PARED:
                            posActualX=posAntiguaX
                            posActualY=posAntiguaY
                            
                        else:
                            matriz[posActualX][posActualY]=PACMAN
                            matriz[posAntiguaX][posAntiguaY] = ' '
                    elif posActualY==0:
                        posActualY=6
                        if matriz[posActualX][posActualY] == FANTASMA:
                            vidas -= 1
                            if vidas == 0:
                                matriz[posActualX][posActualY] = PACMAN
                                matriz[posAntiguaX][posAntiguaY] = ' '
                                imprimir_matriz(filas, columnas, matriz)
                                print('Has Perdido')
                                print('Usuario: ', nombreUsuario)
                                print('Punteo: ', Score)
                                exit = True
                                
                        if matriz[posActualX][posActualY] == PREMIO:
                            Score = Score + 10
                        if Score == puntajeMaximo:
                            matriz[posActualX][posActualY] = PACMAN
                            matriz[posAntiguaX][posAntiguaY] = ' '
                            imprimir_matriz(filas, columnas, matriz)
                            print('FELICIDADES')
                            print('HAS GANADAO')
                            print('Usuario: ', nombreUsuario)
                            print('Punteo: ', Score)
                            exit = True
                        
                        if matriz[posActualX][posActualY] == PARED:
                            posActualX=posAntiguaX
                            posActualY=posAntiguaY
                            
                        else:
                            matriz[posActualX][posActualY]=PACMAN
                            matriz[posAntiguaX][posAntiguaY] = ' '
                if matriz[posActualX][posActualY] == '-':
                    if posActualX==6:
                        posActualX=1
                        if matriz[posActualX][posActualY] == FANTASMA:
                            vidas -= 1
                            if vidas == 0:
                                matriz[posActualX][posActualY] = PACMAN
                                matriz[posAntiguaX][posAntiguaY] = ' '
                                imprimir_matriz(filas, columnas, matriz)
                                print('Has Perdido')
                                print('Usuario: ', nombreUsuario)
                                print('Punteo: ', Score)
                                exit = True
                                
                        if matriz[posActualX][posActualY] == PREMIO:
                            Score = Score + 10
                        if Score == puntajeMaximo:
                            matriz[posActualX][posActualY] = PACMAN
                            matriz[posAntiguaX][posAntiguaY] = ' '
                            imprimir_matriz(filas, columnas, matriz)
                            print('FELICIDADES')
                            print('HAS GANADAO')
                            print('Usuario: ', nombreUsuario)
                            print('Punteo: ', Score)
                            exit = True
                        
                        if matriz[posActualX][posActualY] == PARED:
                            posActualX=posAntiguaX
                            posActualY=posAntiguaY
                            
                        else:
                            matriz[posActualX][posActualY]=PACMAN
                            matriz[posAntiguaX][posAntiguaY] = ' '
                    elif posActualX==0:
                        posActualX=5
                        if matriz[posActualX][posActualY] == FANTASMA:
                            vidas -= 1
                            if vidas == 0:
                                matriz[posActualX][posActualY] = PACMAN
                                matriz[posAntiguaX][posAntiguaY] = ' '
                                imprimir_matriz(filas, columnas, matriz)
                                print('Has Perdido')
                                print('Usuario: ', nombreUsuario)
                                print('Punteo: ', Score)
                                exit = True
                                
                        if matriz[posActualX][posActualY] == PREMIO:
                            Score = Score + 10
                        if Score == puntajeMaximo:
                            matriz[posActualX][posActualY] = PACMAN
                            matriz[posAntiguaX][posAntiguaY] = ' '
                            imprimir_matriz(filas, columnas, matriz)
                            print('FELICIDADES')
                            print('HAS GANADAO')
                            print('Usuario: ', nombreUsuario)
                            print('Punteo: ', Score)
                            exit = True
                        
                        if matriz[posActualX][posActualY] == PARED:
                            posActualX=posAntiguaX
                            posActualY=posAntiguaY
                            
                        else:
                            matriz[posActualX][posActualY]=PACMAN
                            matriz[posAntiguaX][posAntiguaY] = ' '
    else:
        print('Ingrese una opcion valida')


# print(nombreUsuario)
