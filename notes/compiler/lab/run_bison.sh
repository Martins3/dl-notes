bison -d learn-flex-3.y
flex learn-flex-3.l
clang -o cal learn-flex-3.tab.c lex.yy.c -lfl
./cal
