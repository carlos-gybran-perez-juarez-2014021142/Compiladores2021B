"""
Autor: Carlos Gybran Perez Juarez
En este ejemplo G toma los siguientes valores:
    V: { A, B, C, D, E, F }
    S: { A }
    P: {
        A->BCDEa,
        B->bCD,     B->a,
        C->cA,      C->f,
        D->d,
        E->e
    }
    T: {a,b,c,d,e,f}

    Cadenas validas: bcafdeadfdea, bfdfdea
"""
import re
cadena = ""
indice = 0
pertenece=False
def holaMundo():
        print("Actividad: Analizador Sintactico de descenso recursivo [ Programa 3 ]\nAlumno: Carlos Gybran Perez Juarez")
        print("Caracteristicas:\tV: {A,B,C,D,E,F}\tS: { A }\tT: {a,b,c,d,e,f}\nP: { A->BCDEa, B->bCD, C->cA, D->d, E->e, C->f, B->a  }\n")
        print("Ingrese \"salir\" para terminar el programa")
def consumirCaracter(caracter):
    global cadena
    global indice
    try:
        if(cadena[indice] == caracter):
            #print("\tconsumiendo: " + caracter)
            indice=indice+1
            return True
        else:
            return False
    except (RuntimeError, TypeError, NameError, ValueError,IndexError):
        return False
def pedirCadena():
    global cadena
    cadena = str(input("Ingrese cadena: "))
    if(cadena == ""):
        print("no se ha ingresado ninguna cadena.")
#Inicial
def A():
    global pertenece
    # A->BCDEa
    B()
    C()
    D()
    E()
    pertenece = consumirCaracter("a")
def B():
    global pertenece
    #B->bCD
    if(consumirCaracter("b")):
        C()
        D()
    # B->a
    elif(consumirCaracter("a")):
        pertenece = True
    else:
        pertenece = False
def C():
    global pertenece
    #C -> cA
    if(consumirCaracter("c")):
        A()
    #C -> f
    elif(consumirCaracter("f")):
        pertenece=True
    else:
        pertenece=False

def D():
    #D->d
    global pertenece
    pertenece = consumirCaracter("d")
def E():
    global pertenece
    #E->e
    pertenece = consumirCaracter("e")
def main():
    global cadena
    global pertenece
    # Se pide la cadena
    holaMundo()
    pedirCadena()
    while(cadena!="salir"):
        if(cadena):
            A()
            resultado = cadena + (" si pertenece" if(pertenece) else " no es valida")
            print(resultado)
        pedirCadena()
main()
