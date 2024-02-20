import random

import time
# ___________________________switch___________________________________________________________________

def usoSwitch():
    #declaración de función dentro de una función
    def menu():
        print("\n____________________________Menu__________________________")
        print("#1_______________________Acción 1___________________________")
        print("#2_______________________Acción 2___________________________")
        print("#3_______________________Acción 3___________________________")
        print("#0__________________________Salir_________________________")

    condition = True
    while condition:
        menu()

        eleccion = int(input("\nIngrese el numero que le sigue al # para la opcción deseada:"))

        if (eleccion >= 0 and eleccion < 4):

            match eleccion:
                case 1:
                    print("Realizando acción #1...")
                    time.sleep(2) #realiza un delay de 3s
                    print("Se ha realizado la acción correctamente")
                case 2:
                    print("Realizando acción #2...")
                    time.sleep(2)  # realiza un delay de 3s
                    print("Se ha realizado la acción correctamente")
                case 3:
                    print("Realizando acción #3...")
                    time.sleep(2)  # realiza un delay de 3s
                    print("Se ha realizado la acción correctamente")
                case 0:
                    condition = False
        else:
            print("\n                     ¡Eleccion invalida!")


# ___________________________Valores random___________________________________________________________
def valorRandom_1(n):
     return random.randrange(n) # rango de accion de [0,n[

def valorRandom_2(a, b):
    return random.randint(a, b)  # rango de accion de [a,b]


# ___________________________Ciclo while______________________________________________________________
def contarWhile(n):
    i = 0
    while(i < n): # i debe ser menor al valor n -> [0,9]
        print(f'{i}', end = "") # end determina que habra al final de la impresion
        i+=1 # accion de cambio de la condicional

def tablaMultiplicacionWhileAnidado(n):
    i = 0
    while(i < n): # i debe ser menor al valor n -> [0,9]
        j = 0 # j se declara dentro del ciclo para que vuelva a ser 0 cada vuelta
        while(j < n): # j debe ser menor al valor n -> [0,9]
            print(f'{i*j}', end = "|") # end determina que habra al final de la impresion
            j+=1 # accion de cambio de la condicional
        print("") # salto de linea
        i+=1 # accion de cambio de la condicional


# ___________________________Ciclo for______________________________________________________________
def contarFor(n):
    for i in range(n): #no considera el valor n -> [0,9]
        print(f'{i}', end = "") # end determina que habra al final de la impresion

def tablaMultiplicarForAnidado(n):
    for i in range(n): # i debe ser menor al valor n -> [0,9]
        for j in range(n): # j debe ser menor al valor n -> [0,9]
            print(f'{i*j}', end = "|") # end determina que habra al final de la impresion
        print("") # salto de linea

if __name__ == '__main__':
    #tablaMultiplicarForAnidado(10)
    usoSwitch()