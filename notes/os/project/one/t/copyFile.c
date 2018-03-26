#include <stdio.h>
#include <unistd.h>
#include <string.h>
/**
 * 实现的 mv 的部分功能
 * 1. 之前含有文件， 查询
 * 2. 对于路径判断 
 * 3. 实现os 的兼容
 */

#define maxn 1000
char source[maxn];
char dest[maxn];

void path_resolve(char * s, char * name){
    if(name[0] == '/'){ 
        strcpy(s, name);
    }else{
        getcwd(s, sizeof(name));
    }
}

void get_absolute(char * s, char * t){
    path_resolve(source, s);
    path_resolve(dest, t);
}

int main(int argc, char *argv[]) { 
    if(argc < 3){
        printf("Only source and destination are given\n");
        return 0;
    }
    
    get_absolute(argv[1], argv[2]);

    printf("%s \n %s", source, dest);
    
    
    



    printf("handle");
    return 0;
}