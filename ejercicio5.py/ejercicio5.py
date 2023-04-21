import random

class Nodo:
    def __init__(self, valor=None):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar(valor, self.raiz)

    def _agregar(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._agregar(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._agregar(valor, nodo_actual.derecha)

    def buscar(self, valor):
        return self._buscar(valor, self.raiz)

    def _buscar(self, valor, nodo_actual):
        if nodo_actual is None:
            return False
        elif nodo_actual.valor == valor:
            return True
        elif valor < nodo_actual.valor:
            return self._buscar(valor, nodo_actual.izquierda)
        else:
            return self._buscar(valor, nodo_actual.derecha)

    def eliminar(self, valor):
        self.raiz = self._eliminar(self.raiz, valor)

    def _eliminar(self, nodo_actual, valor):
        if nodo_actual is None:
            return None
        elif valor < nodo_actual.valor:
            nodo_actual.izquierda = self._eliminar(nodo_actual.izquierda, valor)
        elif valor > nodo_actual.valor:
            nodo_actual.derecha = self._eliminar(nodo_actual.derecha, valor)
        else:
            if nodo_actual.izquierda is None:
                return nodo_actual.derecha
            elif nodo_actual.derecha is None:
                return nodo_actual.izquierda
            else:
                temp = self._encontrar_min(nodo_actual.derecha)
                nodo_actual.valor = temp.valor
                nodo_actual.derecha = self._eliminar(nodo_actual.derecha, temp.valor)
        return nodo_actual

    def _encontrar_min(self, nodo_actual):
        while nodo_actual.izquierda is not None:
            nodo_actual = nodo_actual.izquierda
        return nodo_actual

    def altura_subarbol_izquierdo(self):
        return self._altura(self.raiz.izquierda)

    def altura_subarbol_derecho(self):
        return self._altura(self.raiz.derecha)

    def _altura(self, nodo_actual):
        if nodo_actual is None:
            return 0
        else:
            return max(self._altura(nodo_actual.izquierda), self._altura(nodo_actual.derecha)) + 1

    def contar_ocurrencias(self, valor):
        return self._contar_ocurrencias(valor, self.raiz)

    def _contar_ocurrencias(self, valor, nodo_actual):
        if nodo_actual is None:
            return 0
        elif nodo_actual.valor == valor:
            return 1 + self._contar_ocurrencias(valor, nodo_actual.izquierda) + self._contar_ocurrencias(valor, nodo_actual.derecha)
        elif valor < nodo_actual.valor:
            return self._contar_ocurrenc
