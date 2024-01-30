#funciones que devuelve las operaciones entre a y b
def funcion_1(a, b):
    return a + b

#funcion con una condicional
def funcion_2(a,b):
    if(a > b):
        return a - b

#funcion con una condicional y caso contrario
def funcion_3(a,b):
    if(a < b):
        return a * b
    else:
        return a / b

#funcion con condicionales anidadas
def funcion_4(a,b):
    if(a != b):
        if (a < b):
            return a * b
        else:
            return a / b
    else:
        return a**b #a^b


#verifica si el archivo actual se esta ejecutando como el archivo principal
if __name__ == '__main__':

    #se almacena el resultado en c
    c = funcion_1(2,2)
    #se imprime c
    print(f'{c}')

    #notar que la variable c puede ser reasignada tantas veces como sea necesario

    c = funcion_2(2, 2) #notar que como la condicion no se cumple y c se igual la nada, por lo cual es None
    print(f'{c}')
    c = funcion_3(2, 2) #notar que como en python no tiene tipos variables definidas, cambian automaticamente al dato necesario
    print(f'{c}')
    c = funcion_4(2, 2)
    print(f'{c}')