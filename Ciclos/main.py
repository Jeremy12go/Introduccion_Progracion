import random

# ___________________________switch___________________________________________________________________



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
    tablaMultiplicarForAnidado(10)
