%{
# include "./a.tab.h"
%}
%%
"a" { return A; }
"b" { return B; }
"c" { return C; }
[ \t] { /* ignore whitespace */ }
. { printf("Mystery character %c\n", *yytext); }
%%
