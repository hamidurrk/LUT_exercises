#include <stdio.h>
#include <string.h>

int main() {
    char name[100];
    int age;

    printf("What's your name?: ");
    fgets(name, sizeof(name), stdin);
    name[strcspn(name, "\n")] = '\0';

    printf("What's your age?: ");
    scanf("%d", &age);

    printf("Hello, %s! You are %d years old.\n", name, age);

    return 0;
}