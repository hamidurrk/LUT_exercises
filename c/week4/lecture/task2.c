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

int main() {
    char *word;
    printf("Give a sentence:\n");
    fgets(word, 100, stdin);
    toggleCase(word);
    printf("%s\n", word);
    return 0;
}