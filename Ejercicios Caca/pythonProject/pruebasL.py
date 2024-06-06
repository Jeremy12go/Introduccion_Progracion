def sumar(cadena):
    suma = 0
    aux = ""
    for caracter in cadena:
        if caracter == ",":
            if aux:
                suma += int(aux)
                aux = ""
        else:
            aux += caracter
    if aux:
        suma += int(aux)

    print(suma)

def decimal_a_binario_fraccionario(numero):
    parte_entera, parte_decimal = str(numero).split(".")
    parte_entera_binaria = ""
    entero = int(parte_entera)
    while entero > 0:
        parte_entera_binaria = str(entero % 2) + parte_entera_binaria
        entero //= 2
    parte_decimal_binaria = ""
    decimal = float("0." + parte_decimal)
    for _ in range(8):
        decimal *= 2
        parte_decimal_binaria += str(int(decimal))
        decimal -= int(decimal)
    numero_binario = parte_entera_binaria + "." + parte_decimal_binaria

    return numero_binario

numero_fraccionario = float(input("ingrese un decimal la parte decimal con un punto:"))
resultado_binario = decimal_a_binario_fraccionario(numero_fraccionario)
print(f"El número {numero_fraccionario} en binario es: {resultado_binario}")



