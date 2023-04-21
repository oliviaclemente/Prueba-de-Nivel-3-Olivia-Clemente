import ejercicio4

# Test de la función leer_numero
def test_leer_numero():
    # Caso de éxito
    assert ejercicio4.leer_numero(1, 10, "Introduce un número del 1 al 10: ") == 5
    
    # Caso de fallo
    assert ejercicio4.leer_numero(1, 10, "Introduce un número del 1 al 10: ") == None
    
# Test de la función generador
def test_generador():
    # Caso de éxito
    numeros = 5
    modo = 2
    result = ejercicio4.generador(numeros, modo)
    assert len(result) == numeros
    assert all(isinstance(x, int) for x in result)
    
    # Caso de fallo
    numeros = 25
    modo = 4
    result = ejercicio4.generador(numeros, modo)
    assert result == None

if __name__ == "__main__":
    test_leer_numero()
    test_generador()
    print("Todos los tests han pasado correctamente")
