class Pila:
    def __init__(self):
        self.datos = []
        
    def apilar(self,valor):
        self.datos.append(valor)
        
    def desapilar(self):
        if(self.len()):
            return str(self.datos.pop())
        else:
            return None
              
    def len(self):
        return len(self.datos)
    
    def top(self):
        if(self.len()):
            return str(self.datos[-1])
        else:
            return None

    def __str__(self):
        return str(self.datos)