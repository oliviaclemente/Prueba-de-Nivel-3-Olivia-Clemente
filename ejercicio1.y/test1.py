from ejercicio1 import get_superhero_for_mission


def main():
    print("¡Bienvenido a la Agencia S.H.I.E.L.D.!")
    mission = input("Por favor, describe la misión: ")
    print("Buscando al superhéroe adecuado para la misión: " + mission)
    superhero = get_superhero_for_mission()
    print("El superhéroe adecuado para la misión " + mission + " es: " + superhero)


if __name__ == "__main__":
    main()


