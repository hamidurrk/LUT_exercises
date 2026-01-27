#include <stdio.h>
#include <string.h>

void toggleCase(char *str) {
    int len = strlen(str);

    for (int i = 0; i < len; i++) {
        if (str[i] >= 'A' && str[i] <= 'Z') str[i] = str[i] + 32;
        else if (str[i] >= 'a' && str[i] <= 'z') str[i] = str[i] - 32;
    }
    return;
}

int shiftRight(char str[], int pos) {
    int len = strlen(str);

    if (pos >= len-1) return 1;
    str[pos]        ^= str[pos + 1];
    str[pos + 1]    ^= str[pos];
    str[pos]        ^= str[pos + 1];
    return 0;
}

int main() {
    char word[100];
    int pos, answer;
    printf("Give a sentence:\n");
    fgets(word, 100, stdin);
    
    printf("Give a position:\n");
    scanf("%d", &pos);
    
    answer = shiftRight(word, pos);
    if (answer == 0) printf("%s", word);
    else printf("Error\n");

    return 0;
}