#include <stdio.h>
#include  <string.h>
#include  <sys/types.h>
#include <sys/wait.h>
#include <zconf.h>
#include <unistd.h>
#include <stdlib.h>
#include <signal.h>
int main_a();
int main_b();
int main_c();
int main_d();
int main_e();

int main(){
    main_e();
    return 0;
}

int main_a() {

    pid_t  pid;
    int    i;
    char   buf[100];

    fork();
    pid = getpid();
    for (i = 1; i <= 100; i++) {
        sprintf(buf, "This line is from pid %d, value = %d\n", pid, i);
        write(1, buf, strlen(buf));
    }
    return 0;
}

int  main_b(){
    pid_t child;
    // 进程号, 对于父进程返回值为 pid, 对于子进程返回值为 0
    int i = 2;
    if((child = fork()) == -1){
        printf("fork error");
        exit(0);
    }
    if(child == 0){
        i = i + 3;
        printf(" child %d\n", child);
        printf(" pid %d\n", getpid());
        printf("i = %d \n", i);
    }else {
        printf("so what is the child %d\n", child);
        printf("waht is the pid %d\n", getpid());
        i = i + 5;
        printf("i=%d\n", i);
    }
    // 不是很懂为什么有时候只有一个数值被print
    return 0;
}

int main_c(){
    if(fork() == 0){
        printf("amazing ! this is %d\n", getpid());
        fflush(stdout); // 虽然含有执行, 但是似乎也清空了缓冲区间
        execlp("./single", NULL);
        printf("b");
    }

    printf("remain part is %d\n", getpid());
    return 0;
}

int main_d(){
    pid_t pid;
    int status;
    pid = fork();
    if(pid == 0){
        for(int i = 0; i < 10; i++){
            printf("A");
            sleep(1);
            fflush(stdout);
        }
        exit(0);
    }else{
        for(int i = 0; i < 10; i++){
            printf("B");
            sleep(1);
            fflush(stdout);
        }
    }
    
    wait(&status);
    
    for(int i = 0; i < 10; i++){
        printf("C");
        fflush(stdout);
    }
    return 0;
}

int main_e(void){
    int NUMPROC = 5;
    pid_t child[NUMPROC];
    int status[NUMPROC];
    int i;
  
    printf("parent = %d\n", getpid());
  
    for(i=0;i<NUMPROC;++i) {
      if(fork() == 0) {
        sleep(i);
        printf("i=%d, %d\n",i, getpid());
        fflush(stdout);
        _exit(0);
      }
    }
  
    for(i=0;i<NUMPROC;++i)
      child[i] = wait(&status[i]);
  
    for(i=0;i<NUMPROC;++i)
      printf("Exit = %d, child = %d\n", WEXITSTATUS(status[i]), child[i]);
    
    return 0;
}
