import json
from Estado import Estado
from Transicion import Transicion

def verFinal(e):
    return True if("esFinal" in e.__dict__) else False

class Automata(object):
    
    def __init__(self, estados=[], alfabeto="", estadoInicial=0, estadoFinal=False, tablaDeTransiciones=[]):
        self.estados = estados
        self.alfabeto = alfabeto
        self.estadoInicial = estadoInicial
        self.estadoFinal=estadoFinal
        if not self.estadoFinal:
            self.estadoFinal=[]
            for e in estados:
                if("esFinal" in e.__dict__):
                    self.estadoFinal.append(e)
        if not estadoFinal:
            print("Debe haber minimo un estado final en el automata")
            exit()
        self.tablaDeTransiciones = tablaDeTransiciones
    
    def mover(estado,token):
        result = list(filter(lambda x: (), self.tablaDeTransiciones)) 
    def leerArchivo(self):
        f = open('automata.json',)
        data = json.load(f)
        
        self.estados = []
        self.alfabeto =data['alfabeto']
        self.estadoInicial = 0
        self.estadoFinal=[]
        
        for e in data['estados']:
            self.estados.append(Estado(e["id"]))
            k=e.keys() # ["id","esFinal"]
            if("esInicial" in k):
                self.estadoInicial = e["id"]
            elif("esFinal" in k):
                self.estadoFinal.append(e["id"])
        
        if not self.estadoFinal and "estadoFinal" in data.keys():
            self.estadoFinal = data["estadoFinal"]
        if(not self.estadoFinal): exit()

        for t in data['tablaDeTransiciones']:
            self.tablaDeTransiciones.append(Transicion(t["estadoActual"], t["estadoDeTransicion"], t["simbolo"]))
        f.close()
    def obtenerEstados(self):
        return self.estados

    def obtenerTablaDeTransiciones(self):
        return self.tablaDeTransiciones
    
    def obtenerAlfabeto(self):
        return self.alfabeto

    def obtenerEstadoInicial(self):
        return self.estadoInicial
    
    def obtenerEstadoFinal(self):
        return self.estadoFinal
    
    def imprimir(self, tipo="Automata Finito"):
        print(tipo + " = {")
        
        cadena=""
        for edo in self.estados:
            cadena += str(edo)
            if(edo != self.estados[-1]):
                cadena += " , "
        print("\tS(Estados) = { " + cadena + " }")
        
        print("\tΣ(Alfabeto) = " + self.alfabeto)
        print("\tq(Estado Inicial) = " + str(self.estadoInicial))
        cadena=""
        for edo in self.estadoFinal:
            cadena+= str(edo)
            if(self.estadoFinal[self.estadoFinal.index(edo)] != self.estadoFinal[-1]):
                cadena+= " ,"
        print("\tQf(Estado final) = { " + cadena + " } ")
        cadena=""
        for transicion in self.tablaDeTransiciones:
            cadena+= "\n\t\t" + str(transicion)
            if(transicion != self.tablaDeTransiciones[-1]):
                cadena += " , "

        print("\tδ(Transiciones) = {" + cadena + "\n\t}")

        print("}")

    def obtenerEstadosApartirDeTabla(self):
        self.estados=[]
        for t in self.tablaDeTransiciones:
            if t.estadoActual not in self.estados: self.estados.append(t.estadoActual)
            if t.estadoDeTransicion not in self.estados: self.estados.append(t.estadoDeTransicion)

    def __str__(self):
        c="\n\t\t--- Automata ---\n\tΣ = " + str(self.alfabeto) + "\n\tS(Estados)= " + str(self.estados)
        c+="\n\tq(Estado Inicial) = q" + str(self.estadoInicial) + "\n\tQf[Estado(s) final(es)] = " + str(self.estadoFinal)
        c+="\n\tδ(Transiciones) = " + str(self.tablaDeTransiciones) + "\n\t\t---------------\n"
        return c

a=Automata(estadoFinal=6)
a.leerArchivo()
a.imprimir()