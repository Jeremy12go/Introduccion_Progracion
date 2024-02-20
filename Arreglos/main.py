#___________________________Arreglos___________________________________________________________
def swap_arreglos(arreglo_A, arreglo_B):
    i = 0
    k = len(arreglo_A)-1

    while (i <= k):
        '''
        swap es tan facil como utilizacion de un auxiliar para no perder ningun valor al momento de intercambiar
        cada elemento de los arreglos
        '''
        aux = arreglo_A[i]
        arreglo_A[i] = arreglo_B[i]
        arreglo_B[i] = aux
        i+=1

def add_arreglos(arreglo_A, arreglo_B):
    i = 0
    k = len(arreglo_B)-1
    while(i <= k):
        '''
        Si tenemos una arreglo de indice maximo = k ; append(n) agrega el valor de 'n' a en una posicion k+1
        '''
        arreglo_A.append(arreglo_B[i])
        i+=1
    return arreglo_A

def delete_unElemento(arreglo_A):
    '''
    pop(n), elimina el elemento que se encuentra en la posicion 'n', por lo cual dejar el parentesis vacio ( ),
    indica que el indice es 0
    '''
    arreglo_A.pop()
    return arreglo_A

def imprimir_arreglo(arreglo):
    i = 0
    print("[", end="")
    while(i <= len(arreglo)-1):
        '''
        Al ser 'i' una variable que comienza en 0, se recorre el arreglo hasta la limitacion del ciclo
        que debe siempre estar en concordancia con el largo del arreglo
        '''
        print(f"{arreglo[i]}", end="")
        if( i == len(arreglo)-1):
            print("]")
        else:
            print(",", end="")
        i+=1


if __name__ == '__main__':

    #___________________________Arreglos___________________________________________________________

    #Los arreglos pueden ser de distintos tipos de datos
    arreglo_A = ['a', 'b', 'c']
    arreglo_B = [1, 2, 3]
    arreglo_C = ['z', 'y', 'x']

    '''
    Los indices negativos recorren el arreglo de forma inversa, estando desfazandos de los indices
    positivos en 1 y teniendo la limitacion de rango. Por lo cual:
        arreglo_A[-4] es un error al intentar acceder a un indice inexistente
    '''
    print(f"Valor de indice negativo en el arreglo: {arreglo_A[-1]}")

    print("Antes:")
    imprimir_arreglo(arreglo_A)
    imprimir_arreglo(arreglo_B)

    #swap_arreglos(arreglo_A, arreglo_B)
    #add_arreglos(arreglo_A, arreglo_B)
    delete_unElemento(arreglo_A)
    delete_unElemento(arreglo_B)

    print("\nDespues:")
    imprimir_arreglo(arreglo_A)
    imprimir_arreglo(arreglo_B)

    # ___________________________Tuplas___________________________________________________________

    tupla_A = ("Auto", "Barco", "Avion")
    tupla_B = (2.71, 3.14, 6.63)

    '''
    Las tuplas cumplen el mismo sistema de indices que los arreglos
    '''
    print(f"Tupla[0]: {tupla_A[0]}")
    print(f"Tupla[-1]: {tupla_A[-1]}")
    print(f"Largo de la tupla: {len(tupla_A)}")

    # ___________________________Diccionarios_____________________________________________________

    #Declaración

    auto = {
        "Marca" : "Ford",
        "Modelo" : "Mustang",
        "Año": 1964,
    }

    personas = [
        {
            "Nombre" : "Juan",
            "Apellido" : "Carlos",
            "Edad" : 21,
        },
        {
            "Nombre": "Jarod",
            "Apellido": "Concha",
            "Edad": 20,
        },
        {
            "Nombre": "Jesús",
            "Apellido": "Correa",
            "Edad": 21,
        }
    ]

    print(f"{auto['Modelo']}")

    auto['Modelo'] = "ALGO"
    print(f"{auto['Modelo']}")
    print(f"{len(auto)}")

    print(f"{personas[0]['Nombre']}")
    personas[0]['Nombre'] = "Pedro"
    print(f"{personas[0]['Nombre']}")
    print(f"{len(personas)}")