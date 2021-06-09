"""
Autor: Carlos Gybran Perez Juarez
Practica para revision de palindromo con las especificaciones:

Una gramatica independiente del contexto es una cuadrupla G= (V, T, P, S), 
tal que V y T son conjuntos finitos de variables y terminales, respectivamente y VnT=0. 
P es un conjunto finito de producciones o reglas y todos los miembros del conjunto 
son de la forma A -> a, donde "A" es una variable y "a" es una cadena de simbolos en(VuT)∗.
S es una variable especial que denominaremos simbolo inicial.

En este ejemplo G toma los siguientes valores:

    V: { A, B }
    S: { A }
    P: {
        A -> aBa ,
        B -> bAb ,
        B -> c
    }
    T: {a,b,c}

"""
import re
lista = []
pertenece=False
#Funcion inicial A
def A():
    global lista
    global pertenece
    if(len(lista)):
        # aBa
        if(lista[0] == "a"):
            lista.pop(0)
        else:
            pertenece = False
            return    
        # Llamada a produccion B
        B()
        lista = lista if(len(lista)) else [""]
        pertenece = True if(lista[0] == "a") else False
    else:
        pertenece = False
        return
#Producciones B        
def B():
    global lista
    global pertenece
    if(len(lista)):
        # B -> bAb
        if(lista[0] == "b"):
            lista.pop(0)
            # Llamada a produccion A
            A()
            lista = lista if(len(lista)) else [""]
            pertenece = True if(lista[0] == "b") else False
        # B -> c
        elif(lista[0] == "c"):
            pertenece = True
            return
        else:
            pertenece = False
    else:
        pertenece = False
#Programa para ver si los caracteres ingresados pertenecen a T
def validarAlfabeto(cadena):
    if(re.findall("[a-c]+", cadena) and len(cadena)):
        return True
    else:
        print(str(re.findall("[^abc]", cadena)) + " no pertenece a los caracteres validos")
        return False
def holaMundo():
        print("Actividad: Verificar palindromo basico\t\tAlumno: Carlos Gybran Perez Juarez")
        print("Caracteristicas:\tV: { A, B }\tS: { A }\tT: {a,b,c}\nP: {  A->aBa ,\tB->bAb ,B->c  }\n")
def main():
    global lista
    global pertenece
    # Se pide la cadena
    holaMundo()
    cadena = str(input("Ingrese cadena: "))
    #Validamos el alfabeto     
    if(validarAlfabeto(cadena)):        
        lista = [e for e in cadena]
        A()
    else:
        print(cadena + " solo puede contener los caracteres \"abc\"")
        return
    resultado = cadena + (" si pertenece" if(pertenece) else " no es valida")
    print(resultado)
main()