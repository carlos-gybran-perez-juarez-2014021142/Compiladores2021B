"""
una gramática libre de contexto (o simplemente gramática) 
consiste en terminales, no terminales, un símbolo inicial y producciones.

Un lenguaje que puede generarse mediante una gramática se 
considera un lenguaje libre de contexto


LL(1)

    L - Left to Right: la lectura de los tokens
        se hace de izquierda a derecha
    L - Leftmost derivation: se busca la derivación
        por la izquierda.
    1 - Número de símbolos de anticipación

LL(1)

    - Método descendente
        Es la versión no recursiva  de analizador sintáctico de Descenso
    - Método tabular:
        Primero se construye una tabla (tabla LL(1))
    - La tabla codifica el automata de pila
    - Cada gramática tiene su tabla
    - El análisis de cadenas usa la misma tabla

----------------------------

obtener toda la información acerca de las gramáticas que sirrven para el análisis sintáctico, entre ellos está LL1

Se usan 2 funciones auxiliares (FIRST() y FOLLOW())

    Primero(X): Aquellos símbolos terminales | épsilon
                que aparecen como primer símbolo de una cadena derivada X.

        X -> .. -> .. -> aA

    Siguiente(N): Aquellos símbolos terminales | fin de entrada
                que pueden aparecer inmediatamente después de N,
                durante alguna derivación.

-------------------------------

PRIMERO

Reglas para calcular PRIMERO(X) X puede ser Terminal(T) o No Terminal(N)
    1. cuando X es T
    2. cuando X es N
    3. cuando X -> épsilon

Para calcular PRIMERO(X1 X2 X3 --- XN)
    1. Aplicar 'algo' parecido a regla 2 de PRIMERO de X

SIGUIENTE       N es No Terminal
    1. Si N es inicial
    2. Si X -> alfa N beta  (N enmedio de 'algo')
    3. Si X -> alfa N       (N al final de 'algo', posiblemente epsilon)
    4. Si X -> alfa N beta
                    PRIMERO(beta) contiene a epsilon

-------------------------------

Construcción de tablas LL(1)

    Las tablas LL(1) son concentraciones de información
    de una G.L.C. Si la tabla tiene entradas múltiples
    la G.L.C. NO es gramática LL(1).
    Si la tabla NO contiene entredas múltiples, es gramática LL(1).

Ejemplo: COnstruye la tabla LL(1) de la G.L.C.

    G(S,N,T,P)
    L(G) = {id...}

    E   -   T E'        (1)
    E'  -   + T E'      (2)
    E'  -   épsilon     (3)
    T   -   F T'        (4)
    T'  -   * F T'      (5)
    T'  -   épsilon     (6)
    F   -   ( E )       (7)
    F   -   id          (8)

Nota:       $ significa FIN de la entrada, es decir, el analizador léxico ya no tiene
            más tokens que enviar.

    Tabla LL(1)

    No terminales: 
        E
        E'
        T
        T'
        F
    Terminales:
        +
        *
        (
        )
        id
        $

        En tabla:

            |       +       |       *       |       (       |       )       |       id      |   $
        E   |                                       (1)                             (1)
        E'  |       (2)                                             (3)                         (3)
        T   |                                       (4)                             (4)
        T'  |       (6)            (5)                              (6)                         (6)
        F   |                                       (7)                             (8)

Para cada produycción debemos hacer los pasos
Calcular solo los terminales que aparezcan en PRIMERO(alfa),

    E   -   T E'        (1)
    E'  -   + T E'      (2)
    E'  -   épsilon     (3)
    T   -   F T'        (4)
    T'  -   * F T'      (5)
    T'  -   épsilon     (6)
    F   -   ( E )       (7)
    F   -   id          (8)
-------------------------------


Tabla LL(1)

    No terminales: 
        S,A,B,D
    Terminales:
        a,d,b,$

        En tabla:

            |   a   |   b   |   d   |   $
        S   |   (1)     (2)
        A   |   
        B   |
        D   |

    S   ->  aBD         (1)
    S   ->  BDa         (2)
    D   ->  bAD         (3)
    D   ->  d           (4)
    B   ->  b           (5)
    A   ->  aBD         (6)
    A   ->  SS          (7)
"""