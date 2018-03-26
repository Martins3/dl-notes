#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include<sys/types.h>
#include<sys/wait.h>  /* Semaphore */
#include<sys/stat.h>
#include<sys/sem.h>
#include <sys/stat.h>

/**
 * 内部需不需要进一步的处理对应的 信号灯 和 attach的释放问题
 * 大小设置为 100 的 单个缓冲区的大小
 * 
 */
void V(int semid,int index);
void P(int semid,int index);

int statusOne[2];
//  创建共享内存组；
int       shm_id, index_id, semaphore;
key_t     mem_key;

int main(int argc, char *argv[]){
    char fileOne [] = "/home/martin/X-Brain/Bachelar/Atom/os/code/lab/a.pdf";
    char fileTwo [] = "/home/martin/X-Brain/Bachelar/Atom/os/code/lab/b.pdf";


    mem_key = ftok("/home/martin/AllWorkStation/Atom/os/code/lab/labOne", 'W');
    shm_id = shmget(mem_key, 1000 * sizeof(char), IPC_CREAT | 0666);
    if (shm_id < 0) {
         printf("*** shmget error (server) ***\n");
         exit(1);
    }


    mem_key = ftok("/home/martin/AllWorkStation/Atom/os/code/lab/labTwo", 'W');
    index_id = shmget(mem_key, 2 * sizeof(int), IPC_CREAT | 0666);
    if (index_id < 0) {
         printf("*** shmget error (server) ***\n");
         exit(1);
    }
    

    //创建信号灯；
    mem_key = ftok("/home/martin/AllWorkStation/Atom/os/code/lab/labThree", 'W');


    semaphore = semget(mem_key, 2, IPC_CREAT | 0666);
    
    //信号灯赋初值；
    int kkk =semctl(semaphore, 0, SETVAL, 10); // empty 
    int kkkk = semctl(semaphore, 1, SETVAL, 0); // full
    printf("%d %d\n", kkk, kkkk);
    fflush(stdout);


    // 创建两个进程readbuf、 writebuf;
    pid_t readbuf;
    pid_t writebuf;
    
    readbuf = fork();
    
    if(readbuf == -1){
        printf("Create the readbuf error");
        exit(-1);
    }

    // readbuf
    else if(readbuf == 0){
        FILE * write_file = fopen(fileTwo, "wb");
        char * addr = (char *)shmat(shm_id, NULL, SHM_R);
        int index = 0;
        
        int count;
        int residual;

        // 读取第一份消息
        P(semaphore, 1); // full
        sscanf(addr, "%d %d", &count, &residual);
        printf(" ++ %d %d ++\n", count, residual); fflush(stdout);
        index ++;
        V(semaphore, 0); // empty


        char buf[100];
        while(count){
            P(semaphore, 1); // full
            char * loc = addr + index * 100;
            for(int i = 0; i < 100; i ++){
                buf[i] = *loc;
                loc ++;
            }
            fwrite(buf, sizeof(char), 100, write_file);
            V(semaphore, 0); // empty

            index ++;
            index = index % 10;
            count --;
        }

        if(residual){
            P(semaphore, 1); // full
            char * loc = addr + index * 100;
            for(int i = 0; i < 100; i ++){
                buf[i] = *loc;
                loc ++;
            }
            fwrite(buf, sizeof(unsigned char), residual, write_file);
            V(semaphore, 0); // empty
        }
        


    }else{
        writebuf = fork();
        if(writebuf == - 1){
            printf("Create the writebuf error");
            exit(-1);

        // writebuf
        }else if(writebuf == 0){
            char * addr = (char *)shmat(shm_id, NULL, SHM_W);
            FILE * read_file = fopen(fileOne, "rb");


            struct stat st;
            stat(fileOne, &st);
            int size = st.st_size;
            int block = size / 100;
            int residual = size % 100;
            int count = block;
            char buf[100];
            printf(" -- %d %d --\n", count, residual); fflush(stdout);

            // 开始的位置传送消息
            int index = 0;
            P(semaphore, 0); // empty
            sprintf(addr, "%d %d", block, residual);
            V(semaphore, 1);  // full
            index ++;
            

            count ++;
            while(count){
                fread(buf, sizeof(unsigned char), 100, read_file);

                // fwrite(BufContent, sizeof(unsigned char), BufContentSz, fout);
                char * loc = addr + index * 100;
                P(semaphore, 0); // empty

                // 实在是没有好方法
                for(int i = 0; i < 100; i ++){
                    *loc = buf[i];
                    loc ++;
                }

                V(semaphore, 1);  // full
                index++;
                count --;
                fflush(stdout);
                index = index % 10;
            }
            
           

        }else{
             wait(&statusOne[0]);
             wait(&statusOne[1]);
             //等待两个进程运行结束；
             //删除信号灯；
             //删除共享内存组 
             shmctl (shm_id , IPC_RMID , 0);
             printf("Over");
        }
    }



    return 0;
}

void P(int semid,int index){	   
    struct sembuf sem;	
    sem.sem_num = index;
    sem.sem_op = -1;	
    sem.sem_flg = 0; //操作标记：0或IPC_NOWAIT等
    semop(semid,&sem,1);	//1:表示执行命令的个数	
    return;
}

void V(int semid,int index){	
    struct sembuf sem;	
    sem.sem_num = index;
    sem.sem_op =  1;
    sem.sem_flg = 0;	
    semop(semid,&sem,1);	
    return;
}

