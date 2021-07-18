#include <stdio.h>
#define UNUSED(a) ((void) a)

int main(int argc, char *argv[])
{
    UNUSED(argc);
    int rc = 0;
    sscanf(argv[1], "%d", &rc);
    return rc;
}
