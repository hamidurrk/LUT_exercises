#include <stdio.h>

void productUntil() {
    int N;
    long double result = 1;
    printf("Give a positive int: ");
    scanf("%d", &N);
    for(int i = 1; i <= N; i++) result = result * i;
    printf("the product 1 * 2 * ... * N is %.0Lf\n", result);
}

int main() {
    productUntil();
    return 0;
}