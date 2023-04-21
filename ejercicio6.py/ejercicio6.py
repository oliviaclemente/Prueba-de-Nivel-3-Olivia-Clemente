import random

# Creamos una lista de tuplas que representan cada una de las cartas de la baraja española
baraja = [("As", "Espada"), ("2", "Espada"), ("3", "Espada"), ("4", "Espada"), ("5", "Espada"), ("6", "Espada"), 
          ("7", "Espada"), ("Sota", "Espada"), ("Caballo", "Espada"), ("Rey", "Espada"), 
          ("As", "Basto"), ("2", "Basto"), ("3", "Basto"), ("4", "Basto"), ("5", "Basto"), ("6", "Basto"), 
          ("7", "Basto"), ("Sota", "Basto"), ("Caballo", "Basto"), ("Rey", "Basto"), 
          ("As", "Copa"), ("2", "Copa"), ("3", "Copa"), ("4", "Copa"), ("5", "Copa"), ("6", "Copa"), 
          ("7", "Copa"), ("Sota", "Copa"), ("Caballo", "Copa"), ("Rey", "Copa"), 
          ("As", "Oro"), ("2", "Oro"), ("3", "Oro"), ("4", "Oro"), ("5", "Oro"), ("6", "Oro"), 
          ("7", "Oro"), ("Sota", "Oro"), ("Caballo", "Oro"), ("Rey", "Oro")]

# Creamos una pila (lista) de cartas aleatorias del mazo
mazo = random.sample(baraja, len(baraja))

# Creamos cuatro pilas (listas) vacías, una por cada palo
espadas = []
bastos = []
copas = []
oros = []

# Iteramos sobre cada carta del mazo y la agregamos a la pila correspondiente según su palo
for carta in mazo:
    if carta[1] == "Espada":
        espadas.append(carta)
    elif carta[1] == "Basto":
        bastos.append(carta)
    elif carta[1] == "Copa":
        copas.append(carta)
    elif carta[1] == "Oro":
        oros.append(carta)

# Ordenamos la pila de espadas de manera creciente según su número
espadas.sort(key=lambda x: x[0])

# Imprimimos las cuatro pilas resultantes
print("Pila de espadas: ", espadas)
print("Pila de bastos: ", bastos)
print("Pila de copas: ", copas)
print("Pila de oros: ", oros)
