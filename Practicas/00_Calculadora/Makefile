CC = gcc
CFLAGS = -lm
.DEFAULT_GOAL := run
NOMBRE = calc

bison: $(NOMBRE).y
	bison -d $(NOMBRE).y
flexeo: $(NOMBRE).l
	flex $(NOMBRE).l
compilex: bison flexeo
	$(CC) -o calc lex.yy.c $(NOMBRE).tab.c $(CFLAGS) 
run: compilex
	./calc
clean:
	rm *.o *.yy.c *.tab.? ejecutable
#Guia para entender cada parte de la calculadora
#https://programmersought.com/article/84234429961/