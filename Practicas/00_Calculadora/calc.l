%option noyywrap
 
%{
    /* Un archivo lex para calculadora */
    void yyerror(char*);
    #include "calc.tab.h"
%}
 
%%
 
     /* las letras de la a-z son variables */   
[a-z]   {
            yylval = *yytext - 'a';
            return VARIABLE;
        }
 
    /* cualquier numero entra aca */
[0-9]+  {
            yylval = atoi(yytext);
            return NUMERO;
        }
 
    /* Simbolos de operadores */
[-+()=/*\n] {return *yytext;}
 
         /* Espacios son ignorados */
[ \t]    ;
 
    /* Otros caracteres son ilegales */
.    yyerror("La entrada tiene caracteres que no son validos");
 
%%