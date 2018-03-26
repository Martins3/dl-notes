#include <stdio.h>
int main(int argc, char const *argv[]) {
  int i = 0x7fffffff;
  if(i != (int)(float)i){
    printf("%x\n",(int)(float)i);
  }
  return 0;
}
