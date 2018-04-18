/* recognize tokens for the calculator and print them out */
%{
enum yytokentype {
NUMBER = 258,
ADD = 259,
SUB = 260,
MUL = 261,
DIV = 262,
ABS = 263,
EOL = 264
};
int yylval;
%}
%%
"+" { return ADD; }
"-" { return SUB; }
"*" { return MUL; }
"/" { return DIV; }
"|" { return ABS; }
[0-9]+ { yylval = atoi(yytext); return NUMBER; }
\n { return EOL; }
[ \t] { /* ignore whitespace */ }
. { printf("Mystery character %c\n", *yytext); }
%%
/*
似乎如果含有返回值，那么yylex，每次实行return 为 yylex() 的返回值
当含有的数值yylval的数值
*/
int main(int argc, char **argv) {
    int tok;
    while(tok = yylex()) {
        printf("tok is %d", tok);
        if(tok == NUMBER) printf("NUMBER = %d\n", yylval);
        else printf("\n");
    }
}

