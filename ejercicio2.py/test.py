from ejercicio2 import PriorityQueue

from ejercicio2 import KhanAlgorithm


def test_khan_algorithm():
    khan = KhanAlgorithm()

    # Agregamos algunos pedidos a la cola
    khan.add_order("Khan 1", "Multiverso 616", "Pedido de alta prioridad")
    khan.add_order("Khan 2", "Multiverso 838", "Pedido de prioridad media")
    khan.add_order("Khan 3", "Multiverso 1610", "Pedido de baja prioridad")
    khan.add_order("Gran Conquistador", "Multiverso 616", "Pedido de alta prioridad")
    khan.add_order("Khan 4", "Multiverso 616", "Pedido de alta prioridad")
    khan.add_order("Khan 5", "Multiverso 1610", "Pedido de baja prioridad")
    khan.add_order("Khan 6", "Multiverso 1610", "Pedido de baja prioridad")
    khan.add_order("Khan 7", "Multiverso 838", "Pedido de prioridad media")
    khan.add_order("Khan 8", "Multiverso 838", "Pedido de prioridad media")
    khan.add_order("Khan 9", "Multiverso 1610", "Pedido de baja prioridad")
    khan.add_order("Khan 10", "Multiverso 838", "Pedido de prioridad media")
    khan.add_order("Khan 11", "Multiverso 1610", "Pedido de baja prioridad")
    khan.add_order("Gran Conquistador", "Multiverso 999", "Pedido de alta prioridad")
    khan.add_order("Khan 12", "Multiverso 1610", "Pedido de baja prioridad")
    khan.add_order("Khan 13", "Multiverso 838", "Pedido de prioridad media")

    # Atendemos la cola y comprobamos que los pedidos de alta prioridad son atendidos primero
    bitacora = PriorityQueue()
    while not khan.is_empty():
        order = khan.next_order()
        bitacora.put(order)

    assert bitacora.get()[2] == "Pedido de alta prioridad"
    assert bitacora.get()[2] == "Pedido de alta prioridad"
    assert bitacora.get()[2] == "Pedido de alta prioridad"
    assert bitacora.get()[2] == "Pedido de prioridad media"
    assert bitacora.get()[2] == "Pedido de prioridad media"
    assert bitacora.get()[2] == "Pedido de prioridad media"
    assert bitacora.get()[2] == "Pedido de baja prioridad"
    assert bitacora.get()[2] == "Pedido de baja prioridad"
    assert bitacora.get()[2] == "Pedido de baja prioridad"
    assert bitacora.get()[2] == "Pedido de baja prioridad"
    assert bitacora.get()[2] == "Pedido de baja prioridad"
    assert bitacora.get()[2] == "Pedido de baja prioridad"
    assert bitacora.get()[2] == "Pedido de baja prioridad"
    assert bitacora.get()[2] == "Pedido de baja prioridad"
    assert bitacora.get()[2] == "Pedido de baja prioridad"
