CC = gcc # Flag for implicit rules
CFLAGS = -lfl
.DEFAULT_GOAL := run
NOMBRE = hw

bison: $(NOMBRE).y
	bison --defines=y.tab.h $(NOMBRE).y
flexeo: $(NOMBRE).l
	flex -o lex.yy.c $(NOMBRE).l
compilex: bison flexeo
	$(CC) $(CFLAGS) -c lex.yy.c
compison: compilex
	$(CC) $(CFLAGS) -c $(NOMBRE).tab.c
construccion: compison
	$(CC) $(CFLAGS) -o ejecutable lex.yy.o $(NOMBRE).tab.o

.INTERMEDIATE: $(NOMBRE).tab.o lex.yy.o lex.yy.c $(NOMBRE).tab.c *.tab.h

run: construccion
	./ejecutable

clean:
	rm *.o *.yy.c *.tab.? ejecutable