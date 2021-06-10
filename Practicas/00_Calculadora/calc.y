%token    NUMERO VARIABLE
%left    '+' '-'
%left    '*' '/'
 
%{
    #include <stdio.h>   
    void yyerror(char*);
    int yylex(void);
    int sym[26];
%}
 
%%
programa:
    programa declaracion '\n'
    |
    ;
declaracion:
     expresion    {printf("%d\n", $1);}
     |VARIABLE '=' expresion    {sym[$1] = $3;}
     ;
expresion:
    NUMERO
    |VARIABLE{$$ = sym[$1];}
    |expresion '+' expresion    {$$ = $1 + $3;}
    |expresion '-' expresion    {$$ = $1 - $3;}
    |expresion '*' expresion    {$$ = $1 * $3;}
    |expresion '/' expresion    {$$ = $1 / $3;}
    |'('expresion')'    {$$ = $2;}
    ;
 
%%
 
void yyerror(char* s)
{
    fprintf(stderr, "Hubo un error: %s\n", s);
}
 
int main(void)
{
    printf("\n\t\t _ Ejercicio calculadora _\n\t\tCarlos Gybran Perez Juarez\n");
    yyparse();
    return 0;
}