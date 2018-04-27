#include <stdio.h>
#include <sys/stat.h>
#include <netinet/in.h>

int main( void ) {
    printf("%d\n", htonl(INADDR_ANY));
    printf("%d\n", htonl(16));
    printf("%d\n", htons(13));
    return 0;
}
