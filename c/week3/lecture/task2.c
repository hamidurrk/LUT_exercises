#include <stdio.h>

int main(void) {
    int temp;
    int sum = 0;
    int N = 0;
    float avg = 0;

    printf("Give the measured temperatures (-999) to stop:\n");
    scanf("%d", &temp);
    
    while (temp != -999) {
        if (temp == -60) {
            printf("Give the measured temperatures (-999) to stop:\n");
            scanf("%d", &temp);
            continue;
        }
        
        N = N + 1;
        sum = (float)sum + temp;

        printf("Give the measured temperatures (-999) to stop:\n");
        scanf("%d", &temp);
    }

    avg = sum / N;
    printf("There were %d observations.\n", N);
    printf("Their average is %0.2f \n", avg);
    return 0;
}