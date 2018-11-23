%{
#  include <stdio.h>
%}

/* declare tokens */
%token A B C

%%

%%
int main(){
  printf("> ");
  yyparse();
  return 0;
}

void yyerror(char *s){
  fprintf(stderr, "error: %s\n", s);
}
