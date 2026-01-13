#include <stdio.h>

int main() {
    printf("Size of int is %zu bytes\n", sizeof(int));
    printf("Size of int address is %zu bytes\n", sizeof(int *));
    return 0;
}