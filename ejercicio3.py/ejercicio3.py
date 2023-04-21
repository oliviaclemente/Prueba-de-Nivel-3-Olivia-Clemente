def suma(a, b):
    try:
        result = a + b
    except TypeError:
        print("Error: Tipo de dato no válido.")
        result = None
    return result

def resta(a, b):
    try:
        result = a - b
    except TypeError:
        print("Error: Tipo de dato no válido.")
        result = None
    return result

def producto(a, b):
    try:
        result = a * b
    except TypeError:
        print("Error: Tipo de dato no válido.")
        result = None
    return result

def division(a, b):
    try:
        result = a / b
    except TypeError:
        print("Error: Tipo de dato no válido.")
        result = None
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero.")
        result = None
    return result

