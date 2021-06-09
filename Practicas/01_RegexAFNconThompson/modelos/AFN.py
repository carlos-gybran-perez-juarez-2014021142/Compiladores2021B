from Automata import Automata
from Expresion import Expresion
from Transicion import Transicion

listaNombresEstados=[]
listaNombresEstados.extend(range(ord('a'),ord('z')+1))
listaNombresEstados.extend(range(ord('A'),ord('Z')+1))

class AFN(Automata):
    def __init__(self, estados=[], alfabeto="",estadoInicial=0,estadofinal=False,tablaDeTransiciones=[]):
        Automata.__init__(self, estados=estados, alfabeto=alfabeto,estadoInicial=estadoInicial,estadoFinal=estadofinal,tablaDeTransiciones=tablaDeTransiciones)
    
    

    def generarDeRegex(self, regex):
        regex = Expresion(regex)
        posfija = regex.getPosfija()

        return
    
    """  REGLAS PARA PASAR DE REGEX A AFN   """
    # 1. Transicion Epsilon
    def generarAfnEpsilon(self):
        estadoInicial=0
        estadoFinal=1
        estados=[0,1]
        tablaDeTransiciones=[
            Transicion(0,"E",1)
        ]
        # 0 (Inicial)    --      E      -->  1 (Final)
        return AFN(estadoInicial=estadoInicial,estadoFinal=estadoFinal,estados=estados,tablaDeTransiciones=tablaDeTransiciones)
    # 2. Transicion de simbolo
    def generarAfnSimbolo(self,simbolo):
        estadoInicial=0
        estadoFinal=1
        estados=[0,1]
        tablaDeTransiciones=[
            Transicion(0,str(simbolo),1)
        ]
        # 0 (Inicial)    --      simbolo      -->  1 (Final)
        return AFN(estadoInicial=estadoInicial,estadoFinal=estadoFinal,estados=estados,tablaDeTransiciones=tablaDeTransiciones)
    # 3. Varias opciones ( | )
    def generarAfnOr(self,afn1,afn2):
        nuevoInicial=0
        contador=0
        equivalentes=[]
        """
            
        """

        nuevosEstados=[]
        nuevaTabla=[]
        # Agregamos afn1
        for e in afn1.estados:
            equivalentes.append((e,chr(listaNombresEstados[contador])))
            contador+=1
        for i in range(len(afn1.tablaDeTransiciones)):
            for eq in equivalentes:
                if(afn1.tablaDeTransiciones[i].estadoActual==eq[0]):
                   afn1.tablaDeTransiciones[i].estadoActual=eq[1]
                if(afn1.tablaDeTransiciones[i].estadoDeTransicion==eq[0]):
                   afn1.tablaDeTransiciones[i].estadoDeTransicion=eq[1]
        
        #            /-- afn1 (inicial) 
        #  0 (Inicial)                  
        #            \-- afn2 (inicial) 
        nuevaTabla.append(Transicion(0,chr(listaNombresEstados[0]),"E"))
        nuevaTabla.append(Transicion(0,chr(listaNombresEstados[contador]),"E"))
        auxiliar = list(map(lambda x: x[1], equivalentes))
        equivalentes=[]
        for e in afn2.estados:
            equivalentes.append((e,listaNombresEstados[contador]))
            contador+=1
        for i in range(len(afn2.tablaDeTransiciones)):
            for eq in equivalentes:
                if(afn2.tablaDeTransiciones[i].estadoActual==eq[0]):
                   afn2.tablaDeTransiciones[i].estadoActual=eq[1]
                if(afn2.tablaDeTransiciones[i].estadoDeTransicion==eq[0]):
                   afn2.tablaDeTransiciones[i].estadoDeTransicion=eq[1]
        
        auxiliar.extend(list(map(lambda x: x[1], equivalentes)))
        print("OR ANTES:" + str(auxiliar))
        
        nuevaTabla.append(Transicion(chr(listaNombresEstados[contador]),contador,"E"))
        nuevaTabla.append(Transicion(chr(listaNombresEstados[contador]),contador,"E"))
        nuevoFinal=contador
        #                       nfa1
        #            /-- afn1 (inicial) -- simbolo1  -- afn1 (final)  --\
        #  0 (Inicial)                                                1 (Final)
        #            \-- afn2 (inicial) -- simbolo1  -- afn2 (final)  --/
        return AFN(estadoInicial=nuevoInicial,estadoFinal=nuevoFinal,estados=nuevosEstados,tablaDeTransiciones=nuevaTabla)
    
    # 4. Concatenacion ( ab / a?b )
    # 5. Cerradura Kleene ( * )


    def cambiarDeEstadoAFN(self):

        return
    def buscarEnAlfabeto(self,c):
        return True if(c in self.alfabeto) else False
    def agregarTransicion(self, nuevaTransicion):
        self.tablaDeTransiciones.append(nuevaTransicion)
    def eliminarTransicion(self, transicion):
        if(transicion in self.tablaDeTransiciones):
            self.tablaDeTransiciones.pop(self.tablaDeTransiciones.index(transicion))
    def agregarSimboloAlAlfabeto(self,c):
        self.alfabeto+=c
    def eliminarEstado(self,e):
        aux = self.estados.pop(self.estados.index(e))
"""
https://github.com/juricaKenda/Finite-Automata/blob/master/regex/RegexDFA.java
AFN():Automata(){};
    AFN(std::string archivo, std::string tipo):Automata(archivo, tipo){};
    bool cambiarDeEstadoAFN(std::vector<Estado*> estados, std::vector<Transicion*> tablaDeTransiciones, Estado* estadoActual, std::string cadena, char simbolo, int indice);
    void renumerarEstados(AFN* subafn, int numero);
    void copiarAlfabeto(AFN* afn, AFN subafn);
    void agregarTransicionEpsilon(AFN* afn, Estado* estado1,Estado* estado2);
    void agregarTransiciones(AFN* afn, std::vector<Transicion*> tablaDeTransiciones);
    void agregarEstados(AFN* afn, std::vector<Estado*> estados);
    void eliminarEstadoFinal(AFN* afn);
    void eliminarEstadoInicial(AFN *afn);
    void modificarTransiciones(AFN* afn, int antiguo, int nuevo);
    void swapTransiciones(AFN* afn, int antiguo, int nuevo);
    void renumerarEstado(AFN *afn, int antiguo, int nuevo);
    void concatenar(AFN* afn, char simbolo, bool esEpsilon);
    void unir(AFN* afn, AFN subafn);
    void aplicarCerraduraKleenAFN(AFN *afn);
    void aplicarCerraduraKleen(AFN* afn, char c, bool esEpsilon);
    void aplicarCerraduraPositivaAFN(AFN *afn);
    void aplicarCerraduraPositiva(AFN* afn, char c, bool esEpsilon);
    Estado* obtenerEstado(int id);
"""