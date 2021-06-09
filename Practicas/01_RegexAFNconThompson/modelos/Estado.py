class Estado(object):
    def __init__(self, id,esInicial=False,esFinal=False):
        self.id = id
        if(esFinal): self.esFinal = esFinal
        if(esInicial): self.esInicial = esInicial
    def comparar(self,e):
        return True if(e.id==self.id) else False
    def __str__(self):
        return "".join(str(self.id))
