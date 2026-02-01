#include <stdio.h>

char asciiToChar(int asciiValue) {
    return (char)asciiValue;
}

int charToAscii(char c) {
    return (int)c;
}

int main() {
    int choice;
    
    do {
        printf("Menu:\n");
        printf("1. Convert ASCII value to character\n");
        printf("2. Convert character to ASCII value\n");
        printf("0. Exit\n");
        printf("Enter your choice:\n");
        scanf("%d", &choice);
        
        if (choice == 1) {
            int asciiValue;
            printf("Enter an ASCII value:\n");
            scanf("%d", &asciiValue);
            char result = asciiToChar(asciiValue);
            printf("The character for ASCII value %d is '%c'.\n", asciiValue, result);
            printf("\n");
        } 
        else if (choice == 2) {
            char character;
            printf("Enter a character:\n");
            scanf(" %c", &character); 
            int result = charToAscii(character);
            printf("The ASCII value for character '%c' is %d.\n", character, result);
            printf("\n");
        }
        else if (choice == 0) {
            printf("Exiting the program. Goodbye!\n");
        }
        
    } while (choice != 0);
    
    return 0;
}