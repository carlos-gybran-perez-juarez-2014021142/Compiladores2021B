CC = gcc # Flag for implicit rules
CFLAGS = -lfl -o
.DEFAULT_GOAL := run

flexeo:
	flex hw.l
.PHONY: flexeando

compic: flexeo
	$(CC) lex.yy.c $(CFLAGS) s.out
.PHONY: compilado

run: compic
	./s.out
.PHONY: ejecutando

clean:
	rm *.out *.c
.PHONY: basura recogida
