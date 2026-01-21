#include <stdio.h>

int main() {
    int size;
    float sum, price;
    
    printf("What is the size of your apartment?: ");
    scanf("%d", &size);

    if (size <= 15 ) sum = 1.2 * size;
    else if (size <= 30) sum = 1.2 * 15 + 2.5 * (size - 15);
    else  sum = 1.2 * 15 + 2.5 * 15 + 4 * (size - 30);
    
    price = 15 + sum;

    printf("The cost is %.2f EUR this month\n", price);
    
    return 0;
}