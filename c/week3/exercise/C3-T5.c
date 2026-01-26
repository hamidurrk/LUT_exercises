#include <stdio.h>
#include <string.h>

int main() {
    char str[201];  
    char *token;
    
    printf("Please enter a string:\n");
    scanf("%s", str);
    
    printf("Splitting the string by vowels:\n");
    
    token = strtok(str, "aeiouAEIOU");
    
    while (token != NULL) {
        printf("%s\n", token);
        token = strtok(NULL, "aeiouAEIOU");
    }
    
    return 0;
}
