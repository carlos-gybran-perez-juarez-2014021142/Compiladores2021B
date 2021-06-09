"""
Autor: Carlos Gybran Perez Juarez
En este ejemplo G toma los siguientes valores:
    V: { A, S }
    S: { S }
    P: {
        S->abSA,
        S->bA,
        A->aA,
        A->c
    }
    T: {a,b,c}

    Cadenas aceptadas para prueba: baaaaaaac, abbaaacc
"""
import re
cadena = ""
indice = 0
pertenece=False
def holaMundo():
        print("Actividad: Verificar palindromo basico\t\tAlumno: Carlos Gybran Perez Juarez")
        print("Caracteristicas:\tV: { S, A }\tS: { S }\tT: {a,b,c}\nP: {  S->abSA, S->bA, A->aA, A->c  }\n")
def consumirCaracter(caracter):
    global cadena
    global indice
    try:
        if(cadena[indice] == caracter):
            print("consumiendo: " + caracter)
            indice=indice+1
            return True
        else:
            return False
    except ValueError:
        return False
#Inicial
def S():
    global cadena
    global indice
    global pertenece
    # S -> abSA
    if(consumirCaracter("a")): # a
        if(consumirCaracter("b")): # b
            S()
            A()
    # S -> bA
    elif(consumirCaracter("b")):
        A()
    else:
        pertenece=False

def A():
    global cadena
    global indice
    global pertenece
    # A->aA
    if(consumirCaracter("a")):
        A()
    # A-> c
    elif(consumirCaracter("c")):
        pertenece=True
    else:
        pertenece=False


def main():
    global cadena
    global pertenece
    # Se pide la cadena
    holaMundo()
    cadena = str(input("Ingrese cadena: "))
    S()
    resultado = cadena + (" si pertenece" if(pertenece) else " no es valida")
    print(resultado)
main()