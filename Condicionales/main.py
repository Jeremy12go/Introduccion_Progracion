# ___________________________Función con retorno por caso______________________________________________________
def funcion_mutiplo(valor):
    if(valor % 3):
        return 3
    elif(valor % 5):
        return 5
    else:
        return 1

# ___________________________Funciones que devuelve las operaciones entre a y b________________________
def funcion_1(a, b):
    return a + b

#condicional
def funcion_2(a,b):
    if(a > b):
        return a - b

#condicional y caso contrario
def funcion_3(a,b):
    if(a < b):
        return a * b
    else:
        return a / b

#condicionales anidadas
def funcion_4(a,b):
    if(a != b):
        if (a < b):
            return a * b
        else:
            return a / b
    else:
        return a**b #a^b


#condicionales lineales de distintas condiciones
def funcion_5(a,b):
    if(a != b):
        return a * b
    elif(a < b):
        return a / b
    else:
        return a**b #a^b

#Entradas y salidas de datos
def sumaEntradas():
    '''
    int(...) formatea el dato de entrada a un entero, no formatear los datos
    resulta la concatenación de los datos y no la suma deseada. Debido que en
    python se definen los datos de forma automatica.
    '''
    a = int(input("Ingresar primer valor: "))
    b = int(input("ingresar segundo valor: "))
    c = a+b
    print(f'El resultado es:{c}')

def multiplo_mayor (a, aa):

    if a == 0 or aa == 0:
        print("Lo siento, este programa no admite valores nulos.")
        return 0
    elif a < 0 or aa < 0:
        print("Lo siento, este programa no admite valores negativos.")
        return 0

    if (a >= aa):
        if (a % aa != 0):
            print(f"{a} no es múltiplo de {aa}.")
        else:
            print(f"{a} es múltiplo de {aa}.")
    else:
        if (aa % a != 0):
            print(f"{aa} no es múltiplo de {a}.")
        else:
            print(f"{aa} es múltiplo de {a}.")

def comparadorDe_años(fecha_1, fecha_2):
    print("COMPARADOR DE AÑOS")
    if fecha_1 > fecha_2:
        print(f"Desde el año {fecha_2} han pasado {fecha_1 - fecha_2} años.")
    elif fecha_1 < fecha_2:
        print(f"Para llegar al año {fecha_2} faltan {fecha_2 - fecha_1} años.")
    else:
        print("¡Son el mismo año!")

#comparacion con booleanos
def bool(variable_booleana):
    #True -> verdad && False -> falso
    if(variable_booleana == True):
        print("Es verdad!")
    else:
        print("Es falso!")

def anno(anno):
    if(anno%100 !=0 and anno%4 == 0 or anno%400 == 0):
        print("Anno bisiesto")
    else:
        print("No Anno bisiesto")


#verifica si el archivo actual se esta ejecutando como el archivo principal
if __name__ == '__main__':

    #se almacena el resultado en c
    c = funcion_1(2,2)
    #se imprime c
    print(f'{c}')

    anno(2024)
    #notar que la variable c puede ser reasignada tantas veces como sea necesario

    c = funcion_2(2, 2) #notar que como la condicion no se cumple y c se igual la nada, por lo cual es None
    print(f'{c}')
    c = funcion_3(2, 2) #notar que como en python no tiene tipos variables definidas, cambian automaticamente al dato necesario
    print(f'{c}')
    c = funcion_4(2, 2)
    print(f'{c}')

    #sumaEntradas()
    comparadorDe_años(2300,2100)