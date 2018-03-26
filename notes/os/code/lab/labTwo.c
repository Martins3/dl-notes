#include <unistd.h>     /* Symbolic Constants */
#include <sys/types.h>  /* Primitive System Data Types */ 
#include <errno.h>      /* Errors */
#include <stdio.h>      /* Input/Output */
#include <stdlib.h>     /* General Utilities */
#include <pthread.h>    /* POSIX Threads */
#include <string.h>     /* String handling */
#include <semaphore.h>  /* Semaphore */


void adder ( );
void printer ( );


sem_t empty;
sem_t full;
int counter;
int m;
int main()
{
    pthread_t thread_a;
    pthread_t thread_b;
    
     
    sem_init(&empty, 0, 1);      
    sem_init(&full, 0, 0);      
                                
                                 
                                 
    pthread_create (&thread_a, NULL, (void *) &adder, NULL);
    pthread_create (&thread_b, NULL, (void *) &printer, NULL);
    
    pthread_join(thread_a, NULL);
    pthread_join(thread_b, NULL);

    sem_destroy(&empty); 
    sem_destroy(&full); 
                  
  
    exit(0);
} 

void adder (){
    while(counter <= 100){
    sem_wait(&empty);       
    counter++;
    sem_post(&full);     
    }
    pthread_exit(0); 
}

void printer(){
    while(counter <= 99){
    sem_wait(&full);
    m = m + counter;
    printf("%d\n", m);
    sem_post(&empty);
    }
    pthread_exit(0); 
}
