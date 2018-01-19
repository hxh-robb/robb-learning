#include <stdio.h>

main(){
    printf("hello, world\n");
    // printf("\c\n"); // exercise 1-2

    /* P-9 */
    int a = 10;
    short b = 10;
    long c = 10;
    char d = 10;
    printf("%lu,%lu,%lu,%lu\n", sizeof a, sizeof b, sizeof c, sizeof d);
}
