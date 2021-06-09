import re
from Pila import Pila

def getPrioridad(e):
    if(re.findall("[*]", e)):
        return 2
    elif(re.findall("[?|\.]", e)):
        return 1
    elif(re.findall("[()]", e)):
        return 0
    else:
        return False

def parentesis(cadena):
    print(cadena)
    infija = ""
    a=0
    print("cadena\t\t\tarmado")
    if(re.findall("[()]", cadena)):
        while(a<len(cadena)):
            if(re.findall("[a-z]", cadena[a])):
                infija += cadena[a]
                if(a+1 in range(len(cadena))):
                    if(re.findall("[a-z(]", cadena[a+1])):
                        infija += "."
                a+=1
            elif(re.findall("[|]", cadena[a])):
                infija += cadena[a]
                b=a+1
                if(cadena[b]!="("):
                    infija += "("
                while(re.findall("[a-z]", cadena[b])):
                    
                    infija += cadena[b]
                    if(re.findall("[a-z(]", cadena[b+1])):
                        print(cadena + "\t\t" + infija + "-------------")
                        infija += "."
                    b+=1
                    print(cadena + "\t\t" + infija)
                a=b
                if(re.findall("[^*?]", cadena[b])):
                    if(cadena[b]!="("):
                        infija += ")"
                    print(cadena+"\t\t" + infija+"\t>>>>>>>>>>>>>>>>><")
                else:
                    infija += cadena[a]
                    a=b+1
                    if(cadena[b]!=")"):
                        infija += ")"
            elif(re.findall("[*]", cadena[a])):
                infija += cadena[a]
                if(re.findall("[a-z]", cadena[a+1])):
                    infija += "."
                a+=1
                
            else:
                infija += cadena[a]
                a+=1
            print(cadena + "\t\t" + infija)
        cadena = infija
        print("\nFinal:\t" + infija)
    return infija

class Expresion(object):
    def __init__(self, regex):
        if(re.findall("[^a-z*()?|E]", regex)):
            print("LA EXPRESION REGULAR QUE INGRESO NO ES VALIDA")
            print("Los caracteres validos son a-z, (, ), *, ?, E, y |")
            self.regex = None
            exit()
        else:
            self.regex = regex

    def setRegex(self,cadena):
      self.regex = cadena
    
    def getRegex(self):
      return self.regex

    # Algoritmo Shunting Yard para pasar la expresion regular Infija a Posfija
    # Ejemplo de aplicacion del algoritmo paso a paso:
    # https://gregorycernera.medium.com/converting-regular-expressions-to-postfix-notation-with-the-shunting-yard-algorithm-63d22ea1cf88
    def getPosfija(self):
      cadena = self.regex
      posfija = ""
      pila = Pila()

      while cadena:
          token = cadena[0]
          cadena = cadena.replace(cadena[0], '', 1)
          if(re.findall("[a-zE]", token)):
              posfija += token
          elif(re.findall("[*?|\.]", token)):
              while (pila.len() and ((getPrioridad(token)<getPrioridad(pila.top())) or (getPrioridad(token)==getPrioridad(pila.top()) and getPrioridad(token)==1)) and (pila.top() != "(")):
                  posfija += pila.desapilar()
              pila.apilar(token)
          elif(token == "("):
              pila.apilar(token)
          elif(token == ")"):
              while(pila.len() and (pila.top() != "(")):
                  posfija += pila.desapilar()
              if(pila.top()=="("):
                  pila.desapilar()
      if(not cadena):
          while(pila.len()):
              if(re.findall("[^()]", pila.top())):
                  posfija += pila.desapilar()
              else:
                  print("Los parentesis no estan balanceados, la pila termino asi: " + str(pila))
                  pila = Pila()
                  posfija = None
      return posfija
"""
a(c|ba)*c
"""
e = Expresion("(ab)*(c|d)*a")
pos = e.getPosfija()
print( pos if(pos) else "")