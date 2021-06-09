class Nodo:
    def __init__(self, simbolo):
        self.izquierdo = None
        self.derecho = None
        self.simbolo = simbolo

class Arbol:
    def __init__(self):
        self.raiz = None
    def insertar(self, raiz, simbolo):
        if self.raiz == None:
            self.raiz = Nodo(simbolo)
        elif raiz == None:
            raiz = Nodo(simbolo)
        else:
            if simbolo <= raiz.simbolo:
                raiz.izquierdo = self.insertar(raiz.izquierdo, simbolo)
            elif simbolo > raiz.simbolo:
                raiz.derecho = self.insertar(raiz.derecho, simbolo)
        return raiz
    def inorden(self, raiz):
        if raiz == None:
            return
        self.inorden(raiz.izquierdo)
        print(raiz.simbolo)
        self.inorden(raiz.derecho)


arbol = Arbol()

arbol.insertar(arbol.raiz, 8)
arbol.insertar(arbol.raiz, 3)
arbol.insertar(arbol.raiz, 10)
arbol.insertar(arbol.raiz, 1)
arbol.insertar(arbol.raiz, 6)
arbol.insertar(arbol.raiz, 4)
arbol.insertar(arbol.raiz, 7)
arbol.insertar(arbol.raiz, 14)
arbol.insertar(arbol.raiz, 13)
arbol.inorden(arbol.raiz)