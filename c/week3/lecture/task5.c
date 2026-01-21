#include <stdio.h>
#include <string.h>

int main() {
    char str[51];
    char delim[] = ": -, /,.";
    char *token;

    printf("ENter a date: ");
    scanf("%s", str);

    token = strtok(str, delim);

    while(token != NULL){
        printf("%s\n", token);
        token = strtok(NULL, delim);
    }
    return 0;
}