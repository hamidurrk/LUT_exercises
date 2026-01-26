#include <stdio.h>
#include <string.h>

int main() {
    char sentence[201];  
    int vowel_count = 0, char_count = 0;
    int i;
    
    printf("Enter a sentence:\n");
    fgets(sentence, sizeof(sentence), stdin);
    
    int len = strlen(sentence);
    if (len > 0 && sentence[len - 1] == '\n') {
        sentence[len - 1] = '\0';
        len--;
    }
    
    for (i = 0; i < len; i++) {
        char c = sentence[i];
        
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
            vowel_count++;
        }
        char_count++;
    }
    
    printf("Number of vowels: %d\n", vowel_count);
    printf("Number of characters: %d\n", char_count);
    
    return 0;
}