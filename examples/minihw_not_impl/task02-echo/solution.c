#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char **argv) {
   for(int i = 1; i < argc; i++) {
            if(*argv[i] == '\0') continue;
            if(i != 1) putchar(' ');
            printf("%s", argv[i]);
   }
   putchar('\n');
   return 0;
}

