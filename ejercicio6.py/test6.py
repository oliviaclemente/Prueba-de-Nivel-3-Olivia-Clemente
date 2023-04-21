import unittest
from ejercicio6 import *

class TestCartas(unittest.TestCase):
    
    def setUp(self):
        self.mazo = generar_mazo()
        self.palos = ['espada', 'basto', 'copa', 'oro']
        self.pilas = separar_por_palos(self.mazo)
    
    def test_generar_mazo(self):
        self.assertEqual(len(self.mazo), 40)
    
    def test_separar_por_palos(self):
        for p in self.palos:
            self.assertTrue(all([carta['palo'] == p for carta in self.pilas[p]]))
    
    def test_ordenar_pila(self):
        pila_espada_ordenada = ordenar_pila(self.pilas['espada'])
        self.assertTrue(all([pila_espada_ordenada[i]['numero'] <= pila_espada_ordenada[i+1]['numero'] for i in range(len(pila_espada_ordenada)-1)]))
        
if __name__ == '__main__':
    unittest.main()
