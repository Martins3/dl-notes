#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
void thread();
int main(){
    pthread_t id;
    int ret = pthread_create(&id, NULL, (void *)thread, NULL); // suprise 

    if(ret !=0 ){
        printf("Create pthread error !\n");
        exit(1);
    }

    for(int i = 0; i < 3; i++){
        printf("this is the main thread\n");
        fflush(stdout);
        sleep(1);
    }
    pthread_join(id, NULL);

    for(int i = 0; i < 3; i++){
        printf("OMG !\n");
        fflush(stdout);
        sleep(1);
    }
    return 0;
}

void thread(){
    for(int i = 0; i < 3; i++){
        printf("this is the pthread\n");
        fflush(stdout);
        sleep(1);
    }
}