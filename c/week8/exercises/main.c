#include <stdio.h>
#include "add.h"
#include "subtract.h"
#include "multiply.h"
#include "divide.h"

int main() {
    int num1, num2;

    printf("Enter number 1:\n");
    scanf("%d", &num1);

    printf("Enter number 2:\n");
    scanf("%d", &num2);

    printf("Addition: %d\n", add(num1, num2));
    printf("Subtraction: %d\n", subtract(num1, num2));
    printf("Multiplication: %d\n", multiply(num1, num2));

    if (divide(num1, num2) != 0.0) {
        printf("Division: %.2f\n", divide(num1, num2)); 
    }

    return 0;
}