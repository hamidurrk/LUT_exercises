#include <stdio.h>

int main(){
    char sent[101];
    char c;
    char sample_digits[] = "0123456789";
    int digits = 0;
    int chars = 0;
    int is_digit = 0;

    printf("Enter a line of text: ");
    fgets(sent, sizeof(sent), stdin);

    for (int i = 0; sent[i] != '\0'; i++) {
        c = sent[i];

        if ((c == "\n") || (c == "\0")) break;

        for (size_t j = 0; j <= (int)sizeof(sample_digits); j++){
            if (c == sample_digits[j]){
                digits++;
                is_digit = 1;
                continue;
            }
        }
        if (is_digit == 0) {
            chars++;
        } 
        is_digit = 0;
    }
    printf("Total digits: %d", digits);
    printf("Total chars: %d", chars);
    
}