#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(int argc, char **argv) {
    if(argc == 1 || strcmp(argv[1], "hello") == 0) {
        puts("Hello world!");
        return 0;
    }
    if(strcmp(argv[1], "exit") == 0) {
        return atoi(argv[2]);
    }
    if(strcmp(argv[1], "echo") == 0) {
        for(int i = 2; i < argc; i++) {
            if(i != 2) putchar(' ');
            printf("%s", argv[i]);
        }
        return 0;
    }

    return 0;
}