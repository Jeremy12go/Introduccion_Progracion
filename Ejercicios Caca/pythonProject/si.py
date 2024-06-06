import random

def newMatrix(m,n):
    list_f = []
    i=0
    k=0
    while i<m:
        list_c = []
        j=0
        while j<n:
            list_c.append(k)
            j+=1
            k+=1
        list_f.append(list_c)
        i+=1
    return list_f

def encontrarList_InMatrix(matrix, list):
    condicional = False
    filas = len(matrix)
    columnas = len(matrix[0])
    i=0
    while(i<filas):
        j=0
        contador = 0
        while (j<columnas):
            k=0
            while (k<len(list)):
                if(matrix[i][j]==list[k]):
                    contador+=1
                k+=1
            j+=1
        i+=1
        if(contador>=len(list)):
            condicional = True
            break
    if(condicional):
        print("Lista esta en la matrix")
    else:
        print("Lista no esta en la matrix")

def encontrarN_InMatrix(matrix, n):
    condicional = False
    contador = 0
    filas = len(matrix)
    columnas = len(matrix[0])
    i=0
    while(i<filas):
        j=0
        while (j<columnas):
            if(matrix[i][j]==n):
                print(f"{n} esta en la matrix")
                condicional = True
                break
            j+=1
        i+=1

    if(not condicional):
        print(f"{n} no esta en la matrix")

def busca_de_numeros(matriz, lista):
    condi = False
    fila = 0
    while fila < len(matriz) :
        columna = 0
        cuento = 0
        while columna < len(matriz[fila]) :
            k = 0
            while k < len(lista) :
                if matriz[fila][columna] == lista[k]:
                    print(f"Elemento en la lista:{lista[k]} == {matriz[fila][columna]}:Elemento Matrix")
                    cuento += 1
                k += 1
            columna += 1
        fila += 1
        if cuento >= len(lista):
            condi = True

    if(condi):
        print("Listas iguales encontradas")
    else:
        print("No hay listas iguales")

def printMatrix(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

i=0
j=0
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

n = 4

list_2 = [2,1,3]

#encontrarList_InMatrix(matriz, list_2)
#encontrarN_InMatrix(matriz, n)
#print(matriz[0][0])
#print(len(matriz[1]))
#print(len(matriz))

list = [1,2,3,4,5,6,7]

#printMatrix(matriz)
#nuevaMatrix = newMatrix(3,3)
#printMatrix(nuevaMatrix)

#busca_de_numeros(matriz, list_2)

def k(s):
    max = 0
    indice = 0
    i = 0
    while i < len(s):
        if s[i] > max:
            max = s[i]
            indice = i
        i+=1

    print(f"Max:{max} esta en el indice {indice}")


s = [1,131,90,523,234,123,]
k(s)
