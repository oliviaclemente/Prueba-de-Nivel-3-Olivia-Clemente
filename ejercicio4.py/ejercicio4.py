import random
import math

def leer_numero(ini, fin, mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < ini or valor > fin:
                raise ValueError
            break
        except ValueError:
            print("Error: el valor debe ser un número entre {} y {}".format(ini, fin))
    return valor

def generador():
    numeros = leer_numero(1, 20, "¿Cuantos números quieres generar? [1-20]: ")
    modo = leer_numero(1, 3, "¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ")
    
    lista_numeros = []
    for i in range(numeros):
        num = random.uniform(0, 100)
        if modo == 1:
            redondeo = math.ceil(num)
        elif modo == 2:
            redondeo = math.floor(num)
        else:
            redondeo = round(num)
        print("Número normal: {:.2f}, número redondeado: {}".format(num, redondeo))
        lista_numeros.append(redondeo)
    
    return lista_numeros
