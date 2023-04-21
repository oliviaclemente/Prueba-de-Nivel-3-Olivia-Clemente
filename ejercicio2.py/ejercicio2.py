class Pedido:
    def __init__(self, solicitante, multiverso, descripcion):
        self.solicitante = solicitante
        self.multiverso = multiverso
        self.descripcion = descripcion


class KhanAlgoritmo:
    def __init__(self):
        self.pila_alta = []
        self.pila_media = []
        self.pila_baja = []

    def atender_pedido(self, pedido):
        if pedido.solicitante == "Gran Conquistador" or \
                pedido.multiverso == "616" or \
                "El que permanece" in pedido.descripcion:
            self.pila_alta.append(pedido)
        elif pedido.solicitante == "Khan que todo lo sabe" or \
                "Carnicero de Dioses" in pedido.descripcion or \
                pedido.multiverso == "838":
            self.pila_media.append(pedido)
        else:
            self.pila_baja.append(pedido)

    def agregar_pedido(self, pedido):
        self.atender_pedido(pedido)

    def siguiente_pedido(self):
        if self.pila_alta:
            return self.pila_alta.pop()
        elif self.pila_media:
            return self.pila_media.pop()
        elif self.pila_baja:
            return self.pila_baja.pop()
        else:
            return None
