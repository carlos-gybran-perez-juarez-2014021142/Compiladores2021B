class Transicion(object):
    def __init__(self, estadoActual, estadoDeTransicion, simbolo, esTransicionEpsilon=False):
        self.estadoActual = estadoActual
        self.estadoDeTransicion = estadoDeTransicion
        self.simbolo = simbolo
        self.esEpsilon = True if(simbolo == "E") else esTransicionEpsilon

    def comparar(self,t):
        return True if((t.simbolo == self.simbolo) and (self.estadoActual==t.estadoActual) and (self.estadoDeTransicion == t.estadoDeTransicion)) else False


    def __str__(self):
        return "\t" + str(self.estadoActual) + "\t--\t" + self.simbolo + "\t-->\t" + str(self.estadoDeTransicion)