import array

#___________________________Listas___________________________________________________________
def swap_list(list_A, list_B):
    i = 0
    k = len(list_A)-1

    while (i <= k):
        '''
        swap es tan facil como utilizacion de un auxiliar para no perder ningun valor al momento de intercambiar
        cada elemento de las listas
        '''
        aux = list_A[i]
        list_A[i] = list_B[i]
        list_B[i] = aux
        i+=1

def add_elements_list( list_A, list_B):
    i = 0
    k = len(list_B)-1
    while(i <= k):
        '''
        Si tenemos una lista de indice maximo = k ; append(n) agrega el valor de 'n' a en una posicion k+1 de la lista
        '''
        list_A.append(list_B[i])
        i+=1
    return list_A

def delete_element(list):
    '''
    pop(n), elimina el elemento que se encuentra en la posicion 'n', por lo cual dejar el parentesis vacio ( ),
    indica que el indice es 0
    '''
    list.pop()
    return list

def print_list(list):
    i = 0
    print("[", end="")
    while(i <= len(list)-1):
        '''
        Al ser 'i' una variable que comienza en 0, se recorre la lista hasta la limitacion del ciclo
        que debe siempre estar en concordancia con el largo de la lista
        '''
        print(f"{list[i]}", end="")
        if( i == len(list)-1):
            print("]")
        else:
            print(",", end="")
        i+=1


def fizzBuzz(n):
    lista = []
    i = 1
    while(i<=n):
        condicion = 0
        if(i%3==0):
            condicion+=1
        elif(i%5==0):
            condicion+=2

        print(f"i:{i} -- condicion: {condicion}")
        if(condicion==3):
            lista.append("FizzBuzz")
        elif(condicion==2):
            lista.append("Buzz")
        elif(condicion==1):
            lista.append("Fizz")
        else:
            lista.append(i)
        i+=1

    print_list(lista)


if __name__ == '__main__':
    """
    #___________________________Listas___________________________________________________________

    #Las listas pueden ser de distintos tipos de datos

    list_A = ['a', 'b', 'c']

    list_B = [1, 2, 3]
    list_C = ['z', 'y', 'x']
    list_D = [ 3.2, "Perro", 'A', 20, True]


    '''
    Los indices negativos recorren el arreglo de forma inversa, estando desfazandos de los indices
    positivos en 1 y teniendo la limitacion de rango. Por lo cual:
        arreglo_A[-4] es un error al intentar acceder a un indice inexistente
    '''
    print(f"Valor de indice negativo en el arreglo: {list_A[-1]}")

    print("Antes:")
    print_list(list_A)
    print_list(list_B)

    swap_list(list_A, list_B)
    add_elements_list(list_A, list_B)
    delete_element(list_A)
    delete_element(list_B)

    print("\nDespues:")
    print_list(list_A)
    print_list(list_B)

    # ___________________________Arreglos________________________________________________________

    arreglo = array.array('i', [1, 2, 3, 4])
    print(arreglo[0] + arreglo[3])

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
    print(f"{len(personas)}")"""
    fizzBuzz(15)