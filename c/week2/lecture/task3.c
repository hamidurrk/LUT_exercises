#include <stdio.h>

int main() {
    char name[51];
    int year;
    int age;

    printf("Give your last name: ");
    scanf("%s", name);
    
    printf("Give your birth year: ");
    scanf("%d", &year);

    age = 2026 - year;

    printf("Hello %s, you will turn %d this year\n", name, age);

    return 0;
}