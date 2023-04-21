class Node:
    def __init__(self, question, yes_node, no_node):
        self.question = question
        self.yes_node = yes_node
        self.no_node = no_node

    def ask(self):
        print(self.question)
        answer = input("Ingrese 's' para sí o 'n' para no: ")
        if answer == 's':
            return self.yes_node
        else:
            return self.no_node


def get_superhero_for_mission():
    khan = Node("¿Es una misión intergaláctica en equipo?", Node("Khan", None, None), Node("¿Se requiere infiltrarse con personas del lugar?", Node("The Winter Soldier", None, None), Node("¿Se requiere no ser detectado?", Node("Ant-Man", None, None), Node("¿Es una misión de destrucción?", Node("The Incredible Hulk", None, None), Node("¿Es una misión de defensa o recuperación?", Node("¿Se requiere ética incorruptible?", Node("Captain América", None, None), Node("¿Se requiere planear la misión y tecnología avanzada?", Node("Iron Man", None, None), Node("¿Es necesario moverse rápidamente de un lugar a otro?", Node("Nick Fury", None, None), Node("¿Es una misión intergaláctica?", Node("Capitana Marvel", None, None), Node("¿Es necesario destruir ejércitos completos?", Node("Thor", None, None), Node("Khan", None, None)))))))))))

    current_node = khan
    while current_node.question is not None:
        current_node = current_node.ask()

    return current_node.question
