#include <stdio.h>
#include <string.h>

void swapElements(char str[], int index1, int index2) {
    char temp = str[index1];
    str[index1] = str[index2];
    str[index2] = temp;
}

int main() {
    char inputStr[100];
    int index1, index2;
    
    printf("Enter a string:\n");
    fgets(inputStr, sizeof(inputStr), stdin);
    inputStr[strcspn(inputStr, "\n")] = '\0';
    
    printf("Enter first index:\n");
    scanf("%d", &index1);
    
    printf("Enter second index:\n");
    scanf("%d", &index2);
    
    int length = strlen(inputStr);
    
    if (index1 < 0 || index1 >= length || index2 < 0 || index2 >= length) {
        printf("Indices are out of bounds.\n");
    } else {
        swapElements(inputStr, index1, index2);
        printf("Modified string: %s\n", inputStr);
    }
    
    return 0;
}