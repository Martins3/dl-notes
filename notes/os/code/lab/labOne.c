#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/types.h>
#include<string.h>
#include<sys/wait.h>

/*
1. 管道按照提示是不是关闭了两次
*/
void terminate_children(int sig_no);
void over(int sig_no);


// 创建pipe
int fd[2];
// 申明子线程
pid_t child_one, child_two;
int statusOne[2];

#define size 65

int main(){
    
    char buf[size];
    char buf_two[size];
    if (pipe(fd) == -1) {
        fprintf(stderr, "Pipe Failed" );
        return 1;
    }

    child_one = fork();

    if(child_one == -1){
        printf("create child one process failed !\n");
        exit(-1);
    }

    // 父进程
    else if(child_one !=0){
        child_two = fork();

        if(child_two == -1){
            printf("create child two  process failed !\n");
        }
        
        // 父进程
        else if(child_two != 0){
            if(signal(SIGINT, terminate_children) == SIG_ERR)
                printf("can't catch SIGINT.\n'");
            pause();
        }
        
        // child two
        else{
            // 设置信号处
            close(fd[0]);
            signal(SIGINT, SIG_IGN);
            if(signal(SIGUSR2, over) == SIG_ERR)
                printf("can't catch SIGUSR2.\n");
            int count = 1;

            while(1){
                sprintf(buf, "I send you %d times\n", count);
                write(fd[1], buf, strlen(buf));
                count ++;
                sleep(1);
            }
        }
    }

    // child_one
    else{
            close(fd[1]);
            signal(SIGINT, SIG_IGN);
            if(signal(SIGUSR1, over) == SIG_ERR)
                printf("can't catch SIGUSR1.\n");

            while(1){
                int res = read(fd[0], buf_two, strlen(buf_two));
                if(res > 0)
                    write(STDOUT_FILENO ,buf_two, res);
                // sleep(3);
                // fflush(stdout);
            }

    }

}
void terminate_children(int sig_no) {
    if(sig_no == SIGINT) {
        // 发送消息到两个子进程
        kill(child_one, SIGUSR1);
        kill(child_two, SIGUSR2);
        wait(&statusOne[0]);
        wait(&statusOne[1]);
        close(fd[0]);
        close(fd[1]);
        printf("Parent process is killed !\n");
        exit(0);
    }
}

void over(int sig_no){  
    if(sig_no == SIGUSR1) {
        printf("Child Process 1 is Kill by Parent !\n");
        sleep(1);
        exit(0);
    }else if(sig_no == SIGUSR2){
        sleep(2);
        printf("Child Process 2 is Kill by Parent !\n");
        sleep(1);
        exit(0);
    }
}