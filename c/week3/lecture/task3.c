#include <stdio.h>

int main() {
    int input, digit, result = 0;

    printf("Give the number: \n");
    scanf("%d", &input);

    while(input != 0) {
        digit = input % 10;
        input = input / 10;

        if (digit == 1) continue;
        if (digit == 7) break;

        // printf("%d\n", digit);
        result = result + digit * digit * digit;
    }
    printf("Result: %d\n", result);
}