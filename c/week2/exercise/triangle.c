#include <stdio.h>

int main() {
    int h;

    scanf("%d", &h);

    for (int i=1; i < h; i++) {
            for (int k=1; k <= h-i; k++) printf(" ");
            for (int l=1; l <= i; l++) printf("*");
            printf("\n");
        }
    }
