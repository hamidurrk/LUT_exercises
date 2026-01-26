#include <stdio.h>

int main() {
    int number, digit, sum = 0;
    
    printf("Give the integer:\n");
    scanf("%d", &number);
    
    while (number > 0) {
        digit = number % 10; 
        
        if (digit == 8) {
            break;
        }
        
        if (digit == 4) {
            number = number / 10;
            continue;
        }
        
        sum += digit * digit;
        number = number / 10;  
    }
    
    printf("The summation is %d.\n", sum);
    
    return 0;
}
