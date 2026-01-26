#include <stdio.h>

int main() {
    int num, count = 0, max = 0, sum = 0;
    float average;
    
    printf("Enter positive integers (0 to stop):\n");
    
    scanf("%d", &num);
    
    while (num != 0) {
        count++;
        sum += num;
        
        if (num > max) {
            max = num;
        }
        
        scanf("%d", &num);
    }
    
    if (count > 0) {
        average = (float)sum / count;
    } else {
        average = 0.0;
    }
    
    printf("Count: %d\n", count);
    printf("Maximum: %d\n", max);
    printf("Average: %.2f\n", average);
    
    return 0;
}
