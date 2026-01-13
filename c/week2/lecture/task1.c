#include <stdio.h>

int main(){
    float base;
    int multiplier;
    float result;

    printf("Give a float and integer separated by blank: ");
    scanf("%f %d", &base, &multiplier);
    result = base * multiplier;

    printf("The product of %f and %d is %.2f\n", base, multiplier, result);
    return 0;
}