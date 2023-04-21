from ejercicio3 import *

a, b, c, d = (10, 5, 0, "Hola")

print("Suma:")
try:
    resultado = suma(a, b)
    print(f"{a} + {b} = {resultado}")
except TypeError:
    print("Error: Tipo de dato no válido.")

try:
    resultado = suma(a, d)
    print(f"{a} + {d} = {resultado}")
except TypeError:
    print("Error: Tipo de dato no válido.")
    
print("Resta:")
try:
    resultado = resta(b, d)
    print(f"{b} - {d} = {resultado}")
except TypeError:
    print("Error: Tipo de dato no válido.")
    
print("Producto:")
try:
    resultado = producto(b, b)
    print(f"{b} * {b} = {resultado}")
except TypeError:
    print("Error: Tipo de dato no válido.")

print("División:")
try:
    resultado = division(a, c)
    print(f"{a} / {c} = {resultado}")
except ZeroDivisionError:
    print("Error: No es posible dividir entre cero.")
    
try:
    resultado = division(b, d)
    print(f"{b} / {d} = {resultado}")
except TypeError:
    print("Error: Tipo de dato no válido.")
except ZeroDivisionError:
    print("Error: No es posible dividir entre cero.")
