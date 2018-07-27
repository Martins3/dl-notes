#include<stdio.h>
#include<stdlib.h>
#include<signal.h>
#include<unistd.h>

void my_func(int sig_no) {
    if(sig_no == SIGUSR1)
        printf("Receive SIGUSR1.\n");
    if(sig_no == SIGUSR2)
        printf("Receive SIGUSR2.\n");
    if(sig_no == SIGINT) {
        printf("Receive SIGINT.\n");
        exit(0);
    }
}

int main(void) {
    // 预先设置用户的处理
    if(signal(SIGUSR1, my_func) == SIG_ERR)
        printf("can't catch SIGUSR1.\n'");
    if(signal(SIGUSR2, my_func) == SIG_ERR)
        printf("can't catch SIGUSR2.\n'");
    if(signal(SIGINT, my_func) == SIG_ERR)
        printf("can't catch SIGINT.\n'");
    
    // 发送信号, 由于本来就是在自己的位置上面运行的
    while(1);
    return 0;
}